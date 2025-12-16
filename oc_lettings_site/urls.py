"""URL configuration for the oc_lettings_site project."""

from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    """Trigger a test error for 500 page."""
    raise Exception("Test 500 error")


urlpatterns = [
    path('', views.index, name='index'),
    path('test-500/', trigger_error),
    path('lettings/', include('lettings.urls')),
    path('profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'oc_lettings_site.views.custom_404'
handler500 = 'oc_lettings_site.views.custom_500'