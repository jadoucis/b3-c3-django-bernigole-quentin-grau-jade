from django.shortcuts import render
from .models import School


# Create your views here.
def index(request):
    schools = School.objects.all()
    return render(request, 'templates/school_list.html', {'schools': schools})
