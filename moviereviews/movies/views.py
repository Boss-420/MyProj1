from django.shortcuts import render
from .models import Email , Movie

# Create your views here.


def home(request):
    email_id = request.GET.get('email')
    searchTerm=request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies= Movie.objects.all()
    if email_id:
        email= Email.objects.create(emailId = email_id)
        email.save()
        return render(request,'email.html',{'email':email_id})
    return render(request, 'home.html',{'movies':movies})

def email(request):
    return render(request, 'email.html')

    