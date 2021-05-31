from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project, Review
from .serializer import ProjectSerializer

class ProjectCreateView(CreateView):
    model = Project
    template_name = 'projcts/new_project.html'
    fields = '__all__'


class ReviewCreateView(CreateView):
    model = Review
    fields = '__all__'
    template_name = 'projcts/newreview.html'

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

def project_search(request):
    keyword = request.GET.get('searchword')
    results = Project.search_project(keyword)
    message = f"{keyword}".capitalize()
    return render(request, 'projcts/search.html', {"message": message, "results": results})

class ProjectsList(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializers = ProjectSerializer(projects, many=True)
        return Response(serializers.data)


