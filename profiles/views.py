"""Views for the profiles application."""

import logging
from django.shortcuts import render
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of all profiles.

    Args:
        request: HTTP request object.

    Returns:
        Rendered HTML page with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    logger.info(f"Profiles index accessed - {len(profiles_list)} profiles found")
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
    try:
        profile = Profile.objects.get(user__username=username)
        logger.info(f"Profile detail accessed - Username: {username}")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Profile.DoesNotExist:
        logger.error(f"Profile not found - Username: {username}")
        raise
