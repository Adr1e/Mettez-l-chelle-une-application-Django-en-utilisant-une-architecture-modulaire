"""Tests for the main oc_lettings_site application."""

import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestIndexView:
    """Tests for the index view."""

    def test_index_view(self, client):
        """Test home page view."""
        response = client.get(reverse('index'))
        assert response.status_code == 200
        assert b"Welcome to OC Lettings" in response.content


@pytest.mark.django_db
class TestIndexUrl:
    """Tests for the index URL."""

    def test_index_url(self):
        """Test index URL."""
        url = reverse('index')
        assert url == '/'
