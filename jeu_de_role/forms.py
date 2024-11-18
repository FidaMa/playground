from django import forms
from .models import Character

# Formulaire pour changer le lieu du personnage
class MoveForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['lieu']

# Formulaire pour changer l'état du personnage
class ChangeTypeForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['type']

 