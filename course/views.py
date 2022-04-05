from django.shortcuts import render
from datetime import datetime

# Create your views here.
def learn_django(request):
    # cname = 'Django'
    # duration = '4 months'
    # seats = 10
    # django_details = {'nm':cname, 'du': duration, 'st':seats}
    # return render(request, 'course/courseone.html', context=django_details)
   d = datetime.now()
   return render(request, 'course/courseone.html', {'dt': d})