"""Tests for the profiles application."""

import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


@pytest.fixture
def user():
    """Create a test user."""
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpassword",
        first_name="Test",
        last_name="User"
    )


@pytest.fixture
def profile(user):
    """Create a test profile."""
    return Profile.objects.create(
        user=user,
        favorite_city="Test City"
    )


@pytest.mark.django_db
class TestProfileModel:
    """Tests for the Profile model."""

    def test_profile_str(self, profile):
        """Test string representation of Profile."""
        assert str(profile) == "testuser"


@pytest.mark.django_db
class TestProfilesViews:
    """Tests for the profiles views."""

    def test_profiles_index(self, client, profile):
        """Test profiles index view."""
        response = client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert b"Profiles" in response.content

    def test_profile_detail(self, client, profile):
        """Test profile detail view."""
        response = client.get(reverse('profiles:profile', args=[profile.user.username]))
        assert response.status_code == 200
        assert b"testuser" in response.content


@pytest.mark.django_db
class TestProfilesUrls:
    """Tests for the profiles URLs."""

    def test_profiles_index_url(self):
        """Test profiles index URL."""
        url = reverse('profiles:index')
        assert url == '/profiles/'

    def test_profile_detail_url(self):
        """Test profile detail URL."""
        url = reverse('profiles:profile', args=['testuser'])
        assert url == '/profiles/testuser/'
