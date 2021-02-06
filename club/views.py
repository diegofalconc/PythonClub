from django.shortcuts import render
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list = Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list': resource_list})

def meeting(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meeting.html', {'meeting' : meeting})