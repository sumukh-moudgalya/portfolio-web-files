from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from basicapp.models import Project
app_name='basicapp'


class Baseview(TemplateView):
    template_name='html/home_page.html'
class ContactsView(TemplateView):
    template_name="html/contacts.html"

class AndroidAppDevlopmentView(TemplateView):
    template_name='html/app_dev.html'

class ResumeView(TemplateView):
    template_name='html/resume.html'

class ProjectListView(ListView):
    context_object_name='project_list'
    model=Project
    def get_queryset(self):
        return Project.objects.all().order_by('rank')
# Create your views here.
