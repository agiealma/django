from django.shortcuts import render
from djangoforms.forms import StudentForm

def index(request):
    student=StudentForm()
    return render(request, 'index.html', {'form':student})