"""Views for the main oc_lettings_site application."""

import logging
from django.shortcuts import render

logger = logging.getLogger(__name__)


def index(request):
    """Display the home page of the website.

    Args:
        request: HTTP request object.

    Returns:
        Rendered HTML home page.
    """
    logger.info("Home page accessed")
    return render(request, 'index.html')


def custom_404(request, exception):
    """Display custom 404 error page.

    Args:
        request: HTTP request object.
        exception: Exception that triggered the 404.

    Returns:
        Rendered 404 error page with status code 404.
    """
    logger.warning(f"404 error - Page not found: {request.path}")
    return render(request, '404.html', status=404)


def custom_500(request):
    """Display custom 500 error page.

    Args:
        request: HTTP request object.

    Returns:
        Rendered 500 error page with status code 500.
    """
    logger.error("500 error - Internal server error")
    return render(request, '500.html', status=500)
