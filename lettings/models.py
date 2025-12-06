"""Models for the lettings application."""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """Model representing a physical address for a letting.

    Attributes:
        number: Street number.
        street: Street name.
        city: City name.
        state: State code (2 characters).
        zip_code: Postal code.
        country_iso_code: ISO country code (3 characters).
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    class Meta:
        """Meta options for Address model."""

        verbose_name_plural = "Addresses"

    def __str__(self):
        """Return string representation of the address."""
        return f'{self.number} {self.street}'


class Letting(models.Model):
    """Model representing a letting (rental property).

    Attributes:
        title: Name of the letting.
        address: Associated address (one-to-one relationship).
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of the letting."""
        return self.title
