from django.shortcuts import render


# Create your views here.
def learn_django(request):

    return render(request, 'course/courseone.html', {'p1':56.24321, 'p2':56.00000,'p3':56.37200 })