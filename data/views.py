from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView
from data.models import *

# Create your views here.
class ScrappList(ListView):
	model = Web
	template_name = 'index.html'

class ScrappDetail(DetailView):
	model = Web
	template_name = 'detail.html'