from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *


class schoollist(ListView):
    model=school
    context_object_name='schools'