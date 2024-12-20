from django import forms
from .models import Character, Lieu

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
    

# Formulaire pour ajouter un personnage
class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['id_character', 'nom', 'etat', 'niveau', 'type', 'team', 'photo', 'lieu']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'style': 'width: 340px',}),
        }

# Formulaire pour ajouter un lieu
class LieuForm(forms.ModelForm):
    class Meta:
        model = Lieu
        fields = ['id_lieu', 'nom', 'description', 'type_lieu', 'disponibilite', 'niveau_acces', 'capacite_max', 'photo']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'class': 'form-control',}),
        }