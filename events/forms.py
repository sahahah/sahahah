from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Feedback

from .models import Events, UserEvent, partcipateEvents

class UserEventForm(ModelForm):
    class Meta:
        model = UserEvent
        fields = '__all__'
        exclude = ['user']

class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']

class AddeventForm(ModelForm):
    class Meta:
        model = Events
        fields = '__all__' 

from django import forms
from .models import User, Events



# class RegeventForm(forms.ModelForm):
#     # Define fields from the User model
#     name = forms.CharField(max_length=200)
#     phone = forms.CharField(max_length=200)
#     email = forms.CharField(max_length=200)
#     # Define fields from the Events model
#     team_size = forms.CharField(max_length=200)

#     class Meta:
#         model = User  # Just specify any model here, as we are not directly saving this form
#         fields = ['name', 'phone', 'email', 'team_size']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment', 'rating']


class partcipateForm(ModelForm):
    class Meta:
        model = partcipateEvents
        fields = '__all__' 