from django.http.response import HttpResponse
from django.shortcuts import render
from .models import room_reservation

from . import forms

def mrrs(request):
    return HttpResponse('会議室予約システム')
    