from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import resolve_url
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rent.forms import UserLoginForm, UserSignUpForm, ProfileUpdateForm
from rent.models import Profile, User


class SignInView(LoginView):
    authentication_form = UserLoginForm
    form_class = UserLoginForm
    redirect_authenticated_user = False
    template_name = 'auth/login/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('/dashboard/')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())
        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(SignInView, self).form_valid(form)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class SingUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'auth/login/signup.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'auth/profile/profile_update.html'
    success_message = "Profile has been successfully updated!"
    model = Profile
    form_class = ProfileUpdateForm

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(username=self.request.user.id)

    def get_success_url(self):
        return reverse('profile_update', kwargs={
            'pk': self.object.pk,
        })


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileView(ListView):
    model = Profile
    template_name = 'auth/profile/profile.html'
    context_object_name = 'profile_ctx'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Profile.objects.get(username=self.request.user)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PasswordChange(SuccessMessageMixin, PasswordChangeView):
    model = User
    form_class = PasswordChangeForm
    template_name = "auth/users/change_password.html"
    success_message = "Password Changed Successfully."
    success_url = reverse_lazy("change_password")
