from django.shortcuts import render
from .models import Profile


def index(request):
    """Affiche la liste de tous les profils."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Affiche les détails d'un profil spécifique."""
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)