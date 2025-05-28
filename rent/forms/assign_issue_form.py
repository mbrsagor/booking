from django import forms

from issue.models import TransferIssue, AssignIssue
from user.models import User


class AssignIssueForm(forms.ModelForm):
    """
    Name: Transfer Issue Worker.
    Source: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
    """

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AssignIssueForm, self).__init__(*args, **kwargs)
        self.fields['crew'].queryset = User.objects.filter(role=6)
        self.fields['crew'].label_from_instance = lambda obj: obj.fullname  # Display Full name
        self.fields['issue'].queryset = TransferIssue.objects.filter(contractor=self.request.user.id, status=1)
        # Empty label name set here
        self.fields['crew'].empty_label = 'Select Worker/Crew'
        self.fields['issue'].empty_label = 'Select Task'
        self.fields['team'].empty_label = 'Select Team'

    class Meta:
        model = AssignIssue
        read_only_fields = ('contractor',)
        fields = (
            'title', 'issue', 'crew', 'team', 'date', 'hour', 'description',
            'minute', 'budget', 'attachment', 'attachment2', 'attachment3'
        )
        widgets = {
            'crew': forms.Select(attrs={'class': 'form-control', 'id': 'crew'}),
            'team': forms.Select(attrs={'class': 'form-control', 'id': 'team'}),
            'issue': forms.Select(attrs={'class': 'form-control', 'id': 'issue'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'id': 'date', 'type': 'date'}),
            'hour': forms.NumberInput(attrs={'class': 'form-control', 'id': 'hour', 'placeholder': 'H'}),
            'minute': forms.NumberInput(attrs={'class': 'form-control', 'id': 'minute', 'placeholder': 'M'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'id': 'budget', 'placeholder': 'Enter budget'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter task short description',
                       'rows': 5}),
            # Attachments
            'attachment': forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'attachment'}),
            'attachment2': forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'attachment2'}),
            'attachment3': forms.FileInput(attrs={'class': 'custom-file-input', 'id': 'attachment3'}),
        }


class AssignIssuePayStatus(forms.ModelForm):
    """
    Name: Assign issue payment status form.
    Desc: When issue will complete worker after that the contactor will payment status update using the form.
    :param
    :is_paid
    """
    class Meta:
        model = AssignIssue
        fields = ('is_paid',)
        widgets = {
            'is_paid': forms.CheckboxInput(attrs={'class': 'js-switch', 'id': 'is_paid', 'onchange': 'this.form.submit()'}),
        }


class AssignIssueUpdateForm(forms.ModelForm):
    """
    Name: Assign Issue update
    Desc: When issue
    """

    class Meta:
        model = AssignIssue
        fields = ('status',)
        widgets = {
            'status': forms.CheckboxInput(attrs={'class': 'js-switch', 'id': 'status'}),
        }
