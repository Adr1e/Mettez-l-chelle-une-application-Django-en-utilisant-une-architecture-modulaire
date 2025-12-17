"""Views for the lettings application."""

import logging
from django.shortcuts import render
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """Display the list of all lettings.

    Args:
        request: HTTP request object.

    Returns:
        Rendered HTML page with the list of lettings.
    """
    lettings_list = Letting.objects.all()
    logger.info(f"Lettings index accessed - {len(lettings_list)} lettings found")
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
    try:
        letting = Letting.objects.get(id=letting_id)
        logger.info(f"Letting detail accessed - ID: {letting_id}, Title: {letting.title}")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Letting.DoesNotExist:
        logger.error(f"Letting not found - ID: {letting_id}")
        raise
