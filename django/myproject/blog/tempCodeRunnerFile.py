from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from django.template import loader
from django.http import Http404, JsonResponse
import os
from django.conf import settings

print(settings.BASE_DIR)