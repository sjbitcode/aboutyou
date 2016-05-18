from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from .models import Profile
from .forms import ProfileForm

# Create your views here.
def success(request):
    return HttpResponse('success!!!')

def custom_login(request):
    if request.user.is_authenticated():
        return redirect('all')
    else:
        return login(request)

def custom_logout(request):
    logout(request)
    return redirect('custom_login')

def index(request):
    print request.META.get('REMOTE_ADDR', None)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            #import pdb; pdb.set_trace();
            profile_info = form.save(commit=False)
            profile_info.user = request.user
            profile_info.save()
            form.save_m2m()
            return redirect('success')
        else:
            print form.errors
    else:
        form = ProfileForm()

    return render(request, 'profiles/fillout.html', {'form':form})

@login_required
def profile_update(request, slug):
    existing = get_object_or_404(Profile, slug=slug)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=existing)

        if form.is_valid():
            profile_info = form.save(commit=False)
            profile_info.save()
            form.save_m2m()
            return redirect('all')
        else:
            print form.errors
    else:
        form = ProfileForm(instance=existing)

    return render(request, 'profiles/update_profile.html', {'form':form})

class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'location', 'spotlight', 'image', 'tags']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('all')


class ProfileView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

class ProfileList(ListView):
    model = Profile
    context_object_name = 'profiles'
    template_name = 'profiles/all.html'

