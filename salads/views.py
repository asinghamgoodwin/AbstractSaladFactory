from django.shortcuts import render
from django.http import HttpResponse

def index(request):
#    return HttpResponse('Hello from Alicia!')
    return render(request, 'test.html')


#def db(request):
#
#    greeting = Greeting()
#    greeting.save()
#
#    greetings = Greeting.objects.all()
#
#    return render(request, 'db.html', {'greetings': greetings})

