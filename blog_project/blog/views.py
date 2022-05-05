from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect


# Create your views here.
def about(request):
    return render(request, 'about.html', {})


def home(request):
    return render(request, 'about.html', {})

def redirect_ml(request):
    response= HttpResponse(status=302)
    response['location']='redirection_fct'
    return response

def redirection_fct(request):
    return render(request,'redirection.html', {})



def redirect_m2(request):
    return HttpResponseRedirect ('redirection_url')

def redirect_perm(request):
    return HttpResponsePermanentRedirect('redirection_url')

def redirect_m3(request):
    return redirect('blog : redir_fct',permanant=False)