from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Project
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup
import csv
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
import html
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors



##saved projects
try:
    admin.site.unregister(Project)
except admin.sites.NotRegistered:
    pass

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('get_project_details', 'user',)
    readonly_fields = ('get_project_details',)

    def get_project_details(self, obj):
        # Using BeautifulSoup to clean the content
        soup = BeautifulSoup(obj.content, features="html.parser")

        # Remove the 'Save Project' button and any other unwanted elements
        for button in soup.find_all('button'):
            button.decompose()

        # Optionally remove other unwanted elements here

        # Construct the clean HTML
        clean_html = ''.join(str(tag) for tag in soup)

        # Return safe HTML for the admin interface
        return mark_safe(clean_html)

    get_project_details.short_description = 'Project Details'

    # This makes the custom 'get_project_details' method be used on the detail view as well
    def get_readonly_fields(self, request, obj=None):
        if obj:  # This is the detail view
            return ('get_project_details',)
        else:  # This is the list view
            return self.readonly_fields
        
    ##export_to_csv_or pdf
    
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('export-csv/', self.export_csv, name='export_csv'),
            path('export-pdf/', self.export_pdf, name='export_pdf'),
        ]
        return my_urls + urls
    
    
    @admin.action(description='Export selected to CSV')
    def export_csv(self, request):
        queryset = self.model.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=projects.csv'
        writer = csv.writer(response)

        # Write the header.
        writer.writerow(['ID', 'Project Details', 'User'])

        for obj in queryset:
            # Use BeautifulSoup to parse the HTML content
            soup = BeautifulSoup(obj.content, features="html.parser")

            # Initialize an empty list to collect text lines
            details_lines = []

            # Iterate over paragraph tags or any other logical division of content
            for content in soup.find_all(['p', 'h1', 'h2', 'h3', 'div', 'li']):  # Add or remove tags as needed
                # Extract the text from each content section
                content_text = content.get_text(separator=" ", strip=True)
                # Unescape HTML entities like '&amp;' to '&'
                content_text = html.unescape(content_text)
                details_lines.append(content_text)

                # If there's an <a> tag, add its text and href as a new line
                for link in content.find_all('a', href=True):
                    link_text = f"{link.text} ({link['href']})"
                    details_lines.append(link_text)

            # Join all the details with a newline character
            project_details = "\n".join(details_lines)

            # Get the user associated with the project
            user = obj.user.get_full_name() if obj.user else 'Anonymous'

            # Write row to CSV
            writer.writerow([obj.pk, project_details, user])

        return response

    @admin.action(description='Export selected to PDF')
    def export_pdf(self, request):
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        
        # Define a Paragraph style for hyperlinks
        styles.add(ParagraphStyle(name='Link', textColor=colors.blue, underline=True))
        
        elements = []

        queryset = self.model.objects.all()
        for obj in queryset:
            soup = BeautifulSoup(str(self.get_project_details(obj)), features="html.parser")

            # Extract text and links from the soup object
            content_pieces = []
            for elem in soup.recursiveChildGenerator():
                if elem.name == 'a':
                    # Make sure the link is complete (e.g., starts with http)
                    link = elem['href'] if elem.has_attr('href') else ''
                    # Only add text and a hyperlink if there's an actual link
                    if link:
                        content_pieces.append(Paragraph(f'<a href="{link}" color="blue">{elem.text}</a>', styles['Link']))
                elif elem.name is None:  # NavigableString objects have None as their name
                    text = str(elem).strip()
                    if text:
                        content_pieces.append(Paragraph(text, styles['Normal']))
            
            # Add each piece of content to the elements list
            for content_piece in content_pieces:
                elements.append(content_piece)
                elements.append(Spacer(1, 0.05 * inch))

            # Add extra space after each project
            elements.append(Spacer(1, 0.2 * inch))

        # Build the PDF
        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="projects.pdf"'
        response.write(pdf)

        return response
admin.site.register(Project, ProjectAdmin)




##keywords
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import KeywordsForm
from .models import KeywordUploadProxy
from django.urls import path
from django.conf import settings
import json
import os

@admin.register(KeywordUploadProxy)
class KeywordsConfigAdmin(admin.ModelAdmin):
    change_list_template = "admin/keywords_config_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('edit-keywords/', self.admin_site.admin_view(self.edit_keywords), name='edit_keywords'),
        ]
        return my_urls + urls

    def edit_keywords(self, request):
        # Load keywords from JSON file
        file_path = os.path.join(settings.BASE_DIR, 'config', 'keywords_config.json')
        with open(file_path, 'r') as file:
            keywords = json.load(file)

        if request.method == 'POST':
            form = KeywordsForm(request.POST, keywords=keywords)
            if form.is_valid():
                # Save updated keywords to JSON file
                updated_keywords = [kw.strip() for kw in form.cleaned_data['keywords'].split(',')]
                with open(file_path, 'w') as file:
                    json.dump(updated_keywords, file)
                self.message_user(request, 'Keywords updated successfully.')
                return HttpResponseRedirect(request.path_info)
        else:
            form = KeywordsForm(keywords=keywords)

        context = self.admin_site.each_context(request)
        context['opts'] = self.model._meta
        context['form'] = form
        return render(request, "admin/keywords_edit.html", context)