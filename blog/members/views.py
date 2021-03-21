from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from myblog.models import Profile
from .forms import ProfilePageForm

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name ='registration/register.html'
    success_url = reverse_lazy('login')


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name ='registration/edit-profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user



class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    #success_url = reverse_lazy('home')
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password-success')


def password_success(request):
    return render(request, 'registration/password-success.html', {})



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user-profile.html'

    def get_context_data(self,*args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit-profile-page.html'
    success_url = reverse_lazy('home')
    fields = ['bio','profile_pic', 'instagram_url', 'twitter_url', 'facebook_url', 'website_url']

class CreateProfilePageView(generic.CreateView):
    model = Profile
    template_name = 'registration/create-profile-page.html'
    form_class = ProfilePageForm

    def form_valid(self,form):
        form.instance.user = self.request.user
        print(form.instance.user)
        return super().form_valid(form)
