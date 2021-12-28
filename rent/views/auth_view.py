from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import resolve_url
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from rent.forms import UserLoginForm, UserSignUpForm


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


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class SingUpView(CreateView):
    form_class = UserSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'auth/login/signup.html'
