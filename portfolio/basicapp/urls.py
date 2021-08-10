from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from basicapp import views
from django.conf import settings
from django.conf.urls.static import static
app_name='basicapp'

urlpatterns=[
url(r'^$',views.Baseview.as_view(),name='home_view'),
url(r'app-development/',views.AndroidAppDevlopmentView.as_view(),name='app_view'),
url(r'resume/',views.ResumeView.as_view(),name="resume_view"),
url(r"project-list/",views.ProjectListView.as_view(),name="project_list_view"),
url(r"contact-info/",views.ContactsView.as_view(),name="contact_info_view"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
