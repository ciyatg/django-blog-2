from django import forms
from .models import WasHere # Because we want to create a form for the WasHere model.

class NameForm(forms.ModelForm):

    class Meta:
        model = WasHere #Django will use WasHere model for the form.
        fields = ('Name',)


