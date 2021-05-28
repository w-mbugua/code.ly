from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView

from .models import Project

class ProjectListView(ListView):
    model = Project
    template_name = 'projcts/projects_list.html'

class ProjectDetailView(DetailView):
    pass


class ProjectEditView(UpdateView):
    pass

class ProjectDeleteView(DeleteView):
    pass