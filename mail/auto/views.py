from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import student_info, history
from django.shortcuts import get_object_or_404, render
from .forms import info


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def info(request):
    if request.method == "POST":
        the_form=info(request.POST or None)
        context={
            "form": the_form
        }
        if form.is_valid():
            form.save()
    return render_to_response(request, 'info.html')
