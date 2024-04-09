
from django.views.generic import ListView, DetailView
from .models import Category, Menu, Payment
from django.shortcuts import render, get_object_or_404

class CategoryLV(ListView):
    model = Category
    template_name = "cafe/category_list.html"
    context_object_name = 'categories'

class CategoryDV(DetailView):
    model = Category
    template_name = "cafe/category_detail.html"
    context_object_name = "category"