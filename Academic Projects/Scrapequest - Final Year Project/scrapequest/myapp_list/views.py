from django.shortcuts import render
from django.shortcuts import redirect
import datetime

##mongo_to_render
from pymongo import MongoClient
client = MongoClient("mongodb+srv://sharams:Su9860797972@atlascluster.abktl4t.mongodb.net/")
db = client['SCRAPEQUEST']

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # User will be inactive until approved
            user.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')  # Redirect to a home page or dashboard
                else:
                    messages.error(request, 'Your account has not been approved yet.')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class'] += ' border-red-500'
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    else:
        # Optionally, handle incorrect usage:
        return HttpResponseNotAllowed(['POST'])



#fetching data from MongoDB
#UNDP
UNDP = db['UNDP']
UNFAO = db['UNFAO']
USAID = db['USAID']
WB = db['WB']
ADB = db['ADB']
JICA = db['JICA']
UKAID = db['UKAID']
SDC = db['SDC']

from django.contrib.auth.decorators import login_required

@login_required
def display_data(request):
    
    # Fetch data from the collection
    UNDPprojects = list(UNDP.find({}, {'_id': 0}))
    
    for UNDPproject in UNDPprojects:
        UNDPproject['Name'] = UNDPproject.pop('Name of the Project')
        UNDPproject['Link'] = UNDPproject.pop('Link to the project')
    pass
    
    # Fetch data from the collection
    UNFAOprojects = list(UNFAO.find({}, {'_id': 0}))
    for UNFAOproject in UNFAOprojects:
        UNFAOproject['Name'] = UNFAOproject.pop('Name of the Project')
        UNFAOproject['Duration'] = UNFAOproject.pop('Duration of the Project')
        UNFAOproject['Link'] = UNFAOproject.pop('Link to the project')
    pass
    # Fetch data from the collection
    USAIDprojects = list(USAID.find({}, {'_id': 0}))
    for USAIDproject in USAIDprojects:
        USAIDproject['Name'] = USAIDproject.pop('Name of the Project')
        USAIDproject['Duration'] = USAIDproject.pop('Duration of the Project')
        USAIDproject['Sector'] = USAIDproject.pop('Sector')
    pass
    # Fetch data from the collection
    WBprojects = list(WB.find({}, {'_id': 0}))
    for WBproject in WBprojects:
        WBproject['Name'] = WBproject.pop('Name of the Project')
        WBproject['Project_Link'] = WBproject.pop('Link to the project')
        WBproject['Details'] = WBproject.pop('Procurement Details')
        WBproject['Procurement_Link'] = WBproject.pop('Link to the Procurement')
        WBproject['Published_Date'] = WBproject.pop('Date of Publishment')
    pass
    # Fetch data from the collection
    ADBprojects = list(ADB.find({}, {'_id': 0}))
    for ADBproject in ADBprojects:
        ADBproject['Name'] = ADBproject.pop('Name of the Project')
        ADBproject['Link'] = ADBproject.pop('Link to the project')
        ADBproject['Status'] = ADBproject.pop('Project Status')
        ADBproject['Desc'] = ADBproject.pop('Project Description')
    pass    
    # Fetch data from the collection
    JICAprojects = list(JICA.find({}, {'_id': 0}))
    for JICAproject in JICAprojects:
        JICAproject['Name'] = JICAproject.pop('Name of the Project')
        JICAproject['Link'] = JICAproject.pop('Link to the project')
    pass    
    # Fetch data from the collection
    UKAIDprojects = list(UKAID.find({}, {'_id': 0}))
    for UKAIDproject in UKAIDprojects:
        UKAIDproject['Name'] = UKAIDproject.pop('Name of the Project')
        UKAIDproject['Link'] = UKAIDproject.pop('Link to the project')
        UKAIDproject['Date'] = UKAIDproject.pop('Start Date')
        UKAIDproject['Desc'] = UKAIDproject.pop('Project Details')
    pass    
    # Fetch data from the collection
    SDCprojects = list(SDC.find({}, {'_id': 0}))
    for SDCproject in SDCprojects:
        SDCproject['Name'] = SDCproject.pop('Name of the Project')
        SDCproject['Link'] = SDCproject.pop('Link to the project')
        SDCproject['Duration'] = SDCproject.pop('Duration of the Project')
        SDCproject['Desc'] = SDCproject.pop('Project Details')
    pass        
    # Pass data to the template
    context = {'UNFAOprojects': UNFAOprojects, 
               'UNDPprojects': UNDPprojects,
               'USAIDprojects': USAIDprojects,
               'WBprojects':WBprojects,
               'ADBprojects': ADBprojects,
               'JICAprojects': JICAprojects,
               'UKAIDprojects': UKAIDprojects,
               'SDCprojects': SDCprojects,
               }  
    
    return render(request, 'List.html', context)


collections = ['UNDP', 'UNFAO', 'USAID', 'WB', 'ADB', 'JICA', 'SDC', 'UKAID']

organization_fields = {
    'UNDP': ['Name of the Project', 'Link to the project'],
    'UNFAO': ['Name of the Project', 'Duration of the Project', 'Link to the project'],
    'USAID': ['Name of the Project', 'Duration of the Project', 'Sector'],
    'WB': ['Name of the Project', 'Link to the project', 'Procurement Details', 'Link to the Procurement', 'Date of Publishment'],
    'ADB': ['Name of the Project', 'Link to the project', 'Project Status', 'Project Description'],
    'JICA': ['Name of the Project', 'Link to the project'],
    'SDC': ['Name of the Project', 'Link to the project', 'Duration of the Project', 'Project Details'],
    'UKAID': ['Name of the Project', 'Link to the project', 'Project Details', 'Start Date'],
}


def parse_date(project, organization):
    date_str = None
    formats = []  # Initialize formats to an empty list

    if organization == 'UNFAO':
        # Extract the start date from the duration using " - " as the separator
        duration = project.get('Duration of the Project', '')
        if " - " in duration:
            date_str = duration.split(" - ")[0]
        formats = ['%d-%b-%Y', '%b %Y']  # 20-Jun-2022, Jul 2019
    elif organization == 'USAID':
        # Check if the duration field is not empty and use " - " as the separator
        duration = project.get('Duration of the Project', '')
        if duration and " - " in duration:
            date_str = duration.split(" - ")[0]
        formats = ['%Y-%m-%d']  # 2006-09-29
    elif organization == 'WB':
        date_str = project.get('Date of Publishment', '')
        formats = ['%B %d, %Y']  # March 12, 2023
    elif organization == 'SDC':
        date_str = project.get('Duration of the Project', '')
        formats = ['%d.%m.%Y']  #- 31.12.2026
    elif organization == 'UKAID':
        date_str = project.get('Start Date', '')
        formats = ['%Y-%m-%d'] #2023-4-1  
    elif organization == 'ADB':
        # Extract the date after "Posting date:"
        description = project.get('Project Description', '')
        marker = "Posting date:"
        if marker in description:
            start_index = description.find(marker) + len(marker)
            end_index = description.find(".", start_index)
            if end_index > start_index:
                date_str = description[start_index:end_index].strip()
        formats = ['%d %b %Y']  # 10 Aug 2022

    for fmt in formats:
        if date_str:  # Ensure date_str is not None or empty
            try:
                return datetime.datetime.strptime(date_str, fmt)
            except ValueError:
                continue

    return None

def sort_projects(projects):
    # This function will place None values at the end when sorting in descending order
    return sorted(projects, key=lambda x: (x['Date'] is not None, x['Date']), reverse=True)

from django.contrib.auth.decorators import login_required
from django.conf import settings
import json

@login_required
def list_projects_by_keyword(request):
    # Load keywords from the configuration file
    keywords = load_keywords()

    #handling requests
    keyword = request.GET.get('keyword', '')  # Get the keyword from the request
    results = {}  
    
    
    #logic for fetching and organizing projects
    results = {keyword: {'full_matches': [], 'partial_matches': []} for keyword in keywords}

    for organization, fields in organization_fields.items():
        collection = db[organization]
        for keyword in keywords:
            # Define additional search fields based on the organization
            search_fields = ['Name of the Project']
            if organization == 'WB':
                search_fields.append('Procurement Details')
            elif organization == 'ADB':
                search_fields.append('Project Description')
            elif organization == 'SDC':
                search_fields.append('Project Details')
            elif organization == 'UKAID':
                search_fields.append('Project Details')
            
            # Perform searches on all designated fields
            for field in search_fields:
                full_keyword_query = {field: {"$regex": f"\\b{keyword}\\b", "$options": "i"}}
                projects = collection.find(full_keyword_query)

                for project in projects:
                    project_info = {field: project.get(field, 'N/A') for field in fields}
                    project_info['Organization'] = organization
                    project_info['Date'] = parse_date(project, organization)  # Parse the date

                    if project_info not in results[keyword]['full_matches']:
                        results[keyword]['full_matches'].append(project_info)

                # Partial keyword search
                for word in keyword.split():
                    partial_keyword_query = {field: {"$regex": f"{word}", "$options": "i"}}
                    projects = collection.find(partial_keyword_query)

                    for project in projects:
                        project_info = {field: project.get(field, 'N/A') for field in fields}
                        project_info['Organization'] = organization
                        project_info['Date'] = parse_date(project, organization)  # Parse the date

                        if project_info not in results[keyword]['full_matches'] and project_info not in results[keyword]['partial_matches']:
                            results[keyword]['partial_matches'].append(project_info)
                             
    for keyword in results:
        results[keyword]['full_matches'] = sort_projects(results[keyword]['full_matches'])
        results[keyword]['partial_matches'] = sort_projects(results[keyword]['partial_matches'])
        
    
        return render(request, 'project_details.html', {'results': results})

def load_keywords():
    with open(settings.BASE_DIR / 'config/keywords_config.json', 'r') as file:
        return json.load(file)


##search functionality
search_collections = {
     'UNDP': ['Name of the Project'],
    'UNFAO': ['Name of the Project', 'Duration of the Project'],
    'USAID': ['Name of the Project', 'Duration of the Project', 'Sector'],
    'WB': ['Name of the Project', 'Procurement Details', 'Date of Publishment'],
    'ADB': ['Name of the Project', 'Project Status', 'Project Description'],
    'JICA': ['Name of the Project'],
    'SDC': ['Name of the Project', 'Project Details', 'Duration of the Project'],
    'UKAID': ['Name of the Project', 'Project Details', 'Start-Date'],

}

for collection_name, fields in search_collections.items():
    # Create a list of tuples for the fields to be indexed
    index_fields = [(field, 'text') for field in fields]

    # Get the collection object
    collection = db[collection_name]
    
    # Get current text indexes on the collection
    current_indexes = collection.index_information()

    # Prepare a set of fields for the new index for comparison
    new_index_fields = set(index_fields)

    # Flag to determine if an equivalent index exists
    index_exists = False

    # Check each existing index
    for index in current_indexes.values():
        if 'key' in index and set(index['key']) == new_index_fields:
            # An equivalent index exists
            index_exists = True
            break

    # If an equivalent index does not exist, create it
    if not index_exists:
        collection.create_index(index_fields)
    
from django.http import HttpResponseNotAllowed, JsonResponse
from django.template.loader import render_to_string

def custom_search(request):
    search_query = request.GET.get('search', '').strip()
    results = {}

    if search_query:
         for collection_name, fields in search_collections.items():
            if collection_name in db.list_collection_names():
                collection = db[collection_name]
                # Perform a text search
                projects = collection.find(
                    {"$text": {"$search": search_query}},
                    {'_id':0}
                ).sort([('textScore', {'$meta': 'textScore'})])
                results[collection_name] = list(projects)
                
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        html = render_to_string('partials/search_results.html', {'results': results})
        return JsonResponse({'html': html})
    else:
        return render(request, 'base.html', {'results': results})






# save_projects
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Project
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def save_project(request):
    content = request.POST.get('content')
    user = request.user
    
    # Create a new Project instance and save the form data
    try:
        project = Project(content=content, user=user)
        project.save()
        return JsonResponse({"success": True, "message": "Project saved successfully."})
    except Exception as e:
        # Log the error or handle it as per requirements
        return JsonResponse({"success": False, "message": "Failed to save the project."}, status=400)

from django.shortcuts import render
from .models import Project
from django.contrib.auth.decorators import login_required

@login_required
def view_saved_projects(request):
    projects = Project.objects.filter(user=request.user)  # Fetch all projects from the database
    return render(request, 'view_saved_projects.html', {'projects': projects})



#visualization for homepage
from collections import Counter
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    collections = ['UNDP', 'UNFAO', 'USAID', 'WB', 'ADB', 'JICA', 'SDC', 'UKAID']
    project_counts = {collection: db[collection].count_documents({}) for collection in collections}

    keywords = load_keywords()

    # Aggregate data for keywords across all collections
    keyword_counts = Counter()
    for collection in collections:
        for keyword in keywords:
            keyword_counts[keyword] += db[collection].count_documents({'$text': {'$search': keyword}})
    
    # Count projects for 2023 and 2024
    years = [str(year) for year in range(2012, 2025)]  # Years from 2012 to 2024
    yearly_counts = {year: 0 for year in years}

    for year in years:
        for collection_name in collections:
            collection = db[collection_name]
            # Use the text index to search for the year as a keyword
            count = collection.count_documents({"$text": {"$search": year}})
            yearly_counts[year] += count

    context = {
        'project_counts': project_counts,
        'keyword_counts': dict(keyword_counts),
        'yearly_counts': yearly_counts,
    }
    return render(request, 'home.html', context)


