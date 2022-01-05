from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rent.models import User
from rent.form.auth_form import UserUpdateForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'auth/users/user_list.html'
    context_object_name = 'users'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'auth/users/user_update.html'
    success_message = 'The user has been updated successful'
    success_url = '/users/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_message = 'The user has been deleted'
    template_name = 'auth/users/user_delete.html'
    success_url = '/users/'
