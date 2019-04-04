from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import (
    UserForm, 
    UserProfileForm, 
    UserUpdateForm,
)

from django.views.generic import (
    CreateView,
)
# Create your views here.

class UserCreationView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('post_list')
    template_name = 'user/user_creation.html'

    def form_valid(self, form):
        user = form.save()
        return user


def UserProfileView(request,*args,**kwargs):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance = request.user.userprofile)
        
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            return redirect('user_profile',pk= request.user.id)
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = UserProfileForm(instance = request.user.userprofile)
    context = {
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request,'profile/profile.html',context)