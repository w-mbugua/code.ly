from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

from .models import Project

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projcts/new_project.html'
    fields = '__all__'

class ProjectListView(ListView):
    model = Project
    template_name = 'projcts/projects_list.html'

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'projcts/project_details.html'


class ProjectEditView(UpdateView):
    model = Project
    fields = ('title', 'description',)
    template_name = 'projcts/project_edit.html'

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'projcts/project_delete.html'
    success_url = reverse_lazy('project_list')