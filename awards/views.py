from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Review
from .forms import ProfileForm, ProjectForm, RateForm


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    # current_user = request.user
    # try:
    #     if not request.user.is_authenticated:
    #         return redirect('accounts/login')
    #      current_user = request.user
    #      profile = Profile.objects.get(user=current_user)

    # except 


    return render(request, 'index.html',)