"""Tests for the lettings application."""

import pytest
from django.urls import reverse
from .models import Address, Letting


@pytest.fixture
def address():
    """Create a test address."""
    return Address.objects.create(
        number=123,
        street="Test Street",
        city="Test City",
        state="TS",
        zip_code=12345,
        country_iso_code="USA"
    )


@pytest.fixture
def letting(address):
    """Create a test letting."""
    return Letting.objects.create(
        title="Test Letting",
        address=address
    )


@pytest.mark.django_db
class TestAddressModel:
    """Tests for the Address model."""

    def test_address_str(self, address):
        """Test string representation of Address."""
        assert str(address) == "123 Test Street"


@pytest.mark.django_db
class TestLettingModel:
    """Tests for the Letting model."""

    def test_letting_str(self, letting):
        """Test string representation of Letting."""
        assert str(letting) == "Test Letting"


@pytest.mark.django_db
class TestLettingsViews:
    """Tests for the lettings views."""

    def test_lettings_index(self, client, letting):
        """Test lettings index view."""
        response = client.get(reverse('lettings:index'))
        assert response.status_code == 200
        assert b"Lettings" in response.content

    def test_letting_detail(self, client, letting):
        """Test letting detail view."""
        response = client.get(reverse('lettings:letting', args=[letting.id]))
        assert response.status_code == 200
        assert b"Test Letting" in response.content


@pytest.mark.django_db
class TestLettingsUrls:
    """Tests for the lettings URLs."""

    def test_lettings_index_url(self):
        """Test lettings index URL."""
        url = reverse('lettings:index')
        assert url == '/lettings/'

    def test_letting_detail_url(self):
        """Test letting detail URL."""
        url = reverse('lettings:letting', args=[1])
        assert url == '/lettings/1/'
