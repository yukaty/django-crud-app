from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from .models import Product

class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    paginate_by = 10

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = "__all__"
    success_url = "/crud/"

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = "__all__"
    success_url = "/crud/"

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = "/crud/"

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

class LoginView(LoginView):
     form_class = AuthenticationForm
     template_name = 'login.html'
