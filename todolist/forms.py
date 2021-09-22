from django import forms
from django.forms import ModelForm, TextInput
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form
        widgets = {
            'title': TextInput(attrs={
                'class': "rounded-l-lg p-4 border-t mr-0 border-b border-l text-gray-800 border-gray-200 bg-white",
                'placeholder': 'New task'
                })
        }