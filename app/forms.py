from django import forms
from .models import DiaryEntry

class DiaryEntryForm(forms.ModelForm):
    class Meta:
        model=DiaryEntry
        fields=['content']
        widgets={
            'content': forms.Textarea(attrs={'class':'textarea','placeholder':"What is on your mind?"}),
        }