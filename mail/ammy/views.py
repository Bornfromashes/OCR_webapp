from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from .models import student_info
from django.shortcuts import render
from PIL import Image
import tesserocr




# Create your views here.
def index(request):
    im= input('Enter image here')
    image=Image.open(im)
    t= tesserocr.image_to_text(image)
    print t
