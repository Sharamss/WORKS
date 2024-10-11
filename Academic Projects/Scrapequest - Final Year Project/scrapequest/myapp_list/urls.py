from django.contrib import admin
from django.urls import path
from . views import *

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('search/', custom_search, name= 'search_bar'),
    
    path('home/', dashboard_view, name= 'homepage'),
    path('list/',display_data, name='project_list'),
    path('search/keywords/',list_projects_by_keyword, name='search_by_keyword'),
    path('save_project/', save_project, name='save_project'),
    path('saved_projects/', view_saved_projects, name='view_saved_project'),
    
    path('signup/', signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name= 'login.html'), name='login'),
    path('logout/', logout_view, name='logout'),


]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 