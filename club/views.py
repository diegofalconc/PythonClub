from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def resourceDetail(request, id):
    resource = get_object_or_404(Resource, pk=id)
    return render(request, 'club/resourcedetail.html', {'resource' : resource})