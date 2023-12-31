from django.shortcuts import render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from django.urls import reverse

@requires_csrf_token
def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account was created succesfully.")
            new_user = authenticate(username=form.cleaned_data['email'], 
                                    password=form.cleaned_data['password1']                        
            )
            login(request, new_user)
            return HttpResponseRedirect(reverse("store:index"))
        
    else:
        form = UserRegisterForm()
        
    
    
    context = {
        'form': form,
    }
    return render(request, "userauths/sign-up.html", context)