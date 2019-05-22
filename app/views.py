from django.shortcuts import render
from django.views.generic import ListView
from .models import db

class view(ListView):
    model = db
    template_name = 'db_list.html'
    context_object_name = 'n'