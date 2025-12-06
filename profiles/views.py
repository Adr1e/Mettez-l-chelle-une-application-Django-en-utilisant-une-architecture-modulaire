"""Views for the profiles application."""

from django.shortcuts import render
from .models import Profile


def index(request):
    """Display the list of all profiles.

    Args:
        request: HTTP request object.

    Returns:
        Rendered HTML page with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """Display details of a specific profile.

    Args:
        request: HTTP request object.
        username: Username of the profile to display.

    Returns:
        Rendered HTML page with profile details.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
