from django import template

register = template.Library()

# Define a dictionary mapping organization names to specific colors
ORG_COLORS = {
    'UNDP': '#3498db',
    'UNFAO': '#2ecc71',
    'USAID': '#9b59b6',
    'WB': '#34495e',
    'ADB': '#16a085',
    'JICA': '#f1c40f',
    'SDC': '#e67e22',
    'UKAID': '#e74c3c',
    # Add more mappings as needed
}

@register.filter(name='color_for_organization')
def color_for_organization(organization_name):
    # Return the color for the organization or a default color if not found
    return ORG_COLORS.get(organization_name, '#7f8c8d')
