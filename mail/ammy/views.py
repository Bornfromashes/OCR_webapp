from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import student_info
from django.shortcuts import render
from PIL import Image
import tesserocr
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect




# Create your views here.
def index(request):
    return render(request, 'index.html')
def form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    return render(request, 'form.html', {'form': form})
