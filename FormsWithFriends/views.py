from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import RegistrationForm
from django.contrib.messages import success, error, warning

def landing(request):
    return render_to_response("landing_page.html",
                              locals(),
                              context_instance=RequestContext(request))

def login(request):
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            success(request, 'You have logged in Successfully!')
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('user/login.html', context_instance=RequestContext(request))

# Create your views here.

def register(request):

    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        success(request, 'Profile has been added to our site')
        return HttpResponseRedirect('/')

    return render_to_response("user/register.html",
                              locals(),
                              context_instance=RequestContext(request))


def aboutus(request):
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request))


@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    warning(request, 'You are now Logged Out!')
    return HttpResponseRedirect('/')