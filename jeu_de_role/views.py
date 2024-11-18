from django.shortcuts import render, get_object_or_404,redirect
from .forms import MoveForm, ChangeTypeForm
from .models import Lieu, Character

def home(request):
    return render(request, 'jeu_de_role/base.html')

def character_list(request):
    characters = Character.objects.all()
    return render(request, 'jeu_de_role/character_list.html', {'characters': characters})

def character_detail(request, id_character):
    # Récupérer le personnage à partir de la base de données
    character = get_object_or_404(Character, id_character=id_character)
    # Initialiser les formulaires
    move_form = MoveForm(request.POST or None)
    type_form = ChangeTypeForm(request.POST or None) # Ne pas lier le formulaire à l'instance pour éviter les changements prématurés
    message = ""

    if request.method == "POST":
        if 'move' in request.POST and move_form.is_valid():
            # Récupérer le lieu actuel du personnage
            ancien_lieu = get_object_or_404(Lieu, id_lieu=character.lieu.id_lieu)

            # Récupérer le nouveau lieu à partir du formulaire
            nouveau_lieu = move_form.cleaned_data['lieu']
            
            # Compter le nombre de personnages dans le nouveau lieu (sans inclure le personnage actuel)
            nb_personnages_nouveau_lieu = Character.objects.filter(lieu=nouveau_lieu).exclude(id_character=character.id_character).count()

            # Vérifier le niveau d'accès du personnage pour le nouveau lieu
            if character.niveau < nouveau_lieu.niveau_acces:
                message = "Niveau d'accès insuffisant pour entrer dans ce lieu."
            # Vérifier la capacité maximale du nouveau lieu
            elif nb_personnages_nouveau_lieu >= nouveau_lieu.capacite_max:
                # Lister les personnages déjà présents dans ce lieu
                personnages_dans_le_lieu = Character.objects.filter(lieu=nouveau_lieu).exclude(id_character=character.id_character)
                noms_personnages = ", ".join([p.nom for p in personnages_dans_le_lieu])  # Supposons que chaque personnage ait un champ 'nom'
                message = f"Le lieu est plein. Vous ne pouvez pas y accéder. Il est occupé par : {noms_personnages}."
            else:
                # Si toutes les vérifications passent, déplacer le personnage
                ancien_lieu.disponibilite = (
                    "libre" if Character.objects.filter(lieu=ancien_lieu).count() - 1 < ancien_lieu.capacite_max 
                    else "occupé"
                )
                ancien_lieu.save()

                # Mettre à jour le personnage avec le nouveau lieu
                character.lieu = nouveau_lieu
                character.save()

                # Mettre à jour la disponibilité du nouveau lieu
                nb_personnages_nouveau_lieu = Character.objects.filter(lieu=nouveau_lieu).count()
                nouveau_lieu.disponibilite = (
                    "libre" if nb_personnages_nouveau_lieu < nouveau_lieu.capacite_max 
                    else "occupé"
                )
                nouveau_lieu.save()

                return redirect('character_detail', id_character=id_character)
        elif 'change_type' in request.POST and type_form.is_valid():
            nouveau_type = type_form.cleaned_data['type']
            character.type = nouveau_type
            character.save()
            return redirect('character_detail', id_character=id_character)

    # Recharger le formulaire avec l'instance actuelle après toutes les validations
    move_form = MoveForm(instance=character)
    type_form = ChangeTypeForm(instance=character)

    return render(request, 'jeu_de_role/character_detail.html', {
        'character': character,
        'move_form': move_form,
        'type_form': type_form,
        'message': message
    })

def lieu_list(request):
    lieux = Lieu.objects.all()
    return render(request, 'jeu_de_role/lieu_list.html', {'lieux': lieux})

def lieu_detail(request, pk):
    lieu = get_object_or_404(Lieu, pk=pk)
    return render(request, 'jeu_de_role/lieu_detail.html', {'lieu': lieu})

def explore(request):
    characters = Character.objects.all()
    lieux = Lieu.objects.all()
    return render(request, 'jeu_de_role/explore.html', {
        'characters': characters,
        'lieux': lieux
    })
