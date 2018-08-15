from django.shortcuts import render

# Create your views here.
def increase_timelion(request):
    start = request.GET['start']
    end = request.GET['end']

