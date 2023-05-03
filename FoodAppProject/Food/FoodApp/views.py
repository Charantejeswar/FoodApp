from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from .serializers import *
from .models import *
from rest_framework import request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from FoodApp import *
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User


# Create your views here.

def Home(request):
    return render(request, 'templates/HomePage.html')
@api_view(["POST"])
def Signup(request):
    form=Userform()
    if request.method == "POST":
        if form.is_valid():
            first_name=request.data("first_name")
            last_name=request.data("last_name")
            username=request.data("username")
            password1=request.data("password1")
            user=User.objects.create_user(first_name,last_name,username,password1,)

    return