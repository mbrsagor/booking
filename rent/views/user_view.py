from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from rent.models import User
from rent.forms.auth_form import UserUpdateForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'auth/users/user_list.html'
    context_object_name = 'users'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect(reverse_lazy('my_booking_history'))
        return super(UserListView, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CustomerListView(ListView):
    model = User
    template_name = 'customers/customers.html'
    context_object_name = 'customers'

    def get_queryset(self):
        return User.objects.filter(role=0)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect(reverse_lazy('my_booking_history'))
        return super(CustomerListView, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'auth/users/user_update.html'
    success_message = 'The user has been updated successful'
    success_url = '/users/'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect(reverse_lazy('my_booking_history'))
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    success_message = 'The user has been deleted'
    template_name = 'auth/users/user_delete.html'
    success_url = '/users/'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect(reverse_lazy('my_booking_history'))
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)
