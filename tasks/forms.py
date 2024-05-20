from django import forms
from .models import Task    
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important', 'resena']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Write a title'}),
            'resena': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Write a resena'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Write a description'}),  
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }