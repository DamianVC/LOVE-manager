"""
Defines the Django models for this app.

For more information see:
https://docs.djangoproject.com/en/2.2/topics/db/models/
"""
from django.db import models


class BaseModel(models.Model):
    """Base Model for the models of this app."""

    class Meta:
        """Define attributes of the Meta class."""

        abstract = True
        """Make this an abstract class in order to be used as an enhanced base model"""

    creation_timestamp = models.DateTimeField(
        auto_now_add=True, editable=False,
        verbose_name='Creation time'
    )
    """Creation timestamp, autogenerated upon creation"""

    update_timestamp = models.DateTimeField(
        auto_now=True, editable=False,
        verbose_name='Last Updated'
    )
    """Update timestamp, autogenerated upon creation and autoupdated on every update"""


class Workspace(BaseModel):
    """Workspace Model."""

    name = models.CharField(max_length=20)
    """The name of the Workspace. e.g 'My Workspace'"""

    def __str__(self):
        """Redefine how objects of this class are transformed to string."""
        return self.name
