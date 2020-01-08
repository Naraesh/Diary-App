from django import forms
from .models import entry

class EntryForm(forms.ModelForm):
    class Meta:
        model=entry
        fields=['text']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['text'].widget.attrs.update({'class':'form-control','placeholder':'What\'s on your mind?'})
