from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView, DeleteView

from rent.models import User
from rent.forms import UserUpdateForm


class UserListView(ListView):
    model = User
    template_name = 'auth/users/user_list.html'
    context_object_name = 'users'


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'auth/users/user_update.html'
    success_message = 'The user has been updated successful'
    success_url = '/users/'


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_message = 'The user has been deleted'
    template_name = 'auth/users/user_delete.html'
    success_url = '/users/'
