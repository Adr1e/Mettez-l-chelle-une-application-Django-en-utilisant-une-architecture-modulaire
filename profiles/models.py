"""Models for the profiles application."""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model representing a user profile.

    Attributes:
        user: Associated Django user (one-to-one relationship).
        favorite_city: User's favorite city (optional).
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """Return string representation of the profile."""
        return self.user.username
