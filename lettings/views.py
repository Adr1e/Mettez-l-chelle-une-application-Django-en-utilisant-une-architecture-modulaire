"""Views for the lettings application."""

from django.shortcuts import render
from .models import Letting


def index(request):
    """Display the list of all lettings.

    Args:
        request: HTTP request object.

    Returns:
        Rendered HTML page with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """Display details of a specific letting.

    Args:
        request: HTTP request object.
        letting_id: Primary key of the letting to display.

    Returns:
        Rendered HTML page with letting details.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
