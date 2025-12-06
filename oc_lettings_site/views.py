"""Views for the main oc_lettings_site application."""

from django.shortcuts import render


def index(request):
    """Display the home page of the website.

    Args:
        request: HTTP request object.

    Returns:
        Rendered HTML home page.
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """Display custom 404 error page.

    Args:
        request: HTTP request object.
        exception: Exception that triggered the 404.

    Returns:
        Rendered 404 error page with status code 404.
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """Display custom 500 error page.

    Args:
        request: HTTP request object.

    Returns:
        Rendered 500 error page with status code 500.
    """
    return render(request, '500.html', status=500)
