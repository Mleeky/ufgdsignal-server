from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from .forms import AnuncianteForm,  UserForm
from django.views.generic.edit import CreateView
from .models import AnuncianteProfile



class UsuarioCreate(CreateView):
    form_class = UserForm
    template_name = 'user_form.html'
    sucess_url = 'thanks.html'
    