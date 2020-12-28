"""
Defines the Django models for this app ('api').

For more information see:
https://docs.djangoproject.com/en/2.2/topics/db/models/
"""
import os
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import rest_framework.authtoken.models
from ui_framework.models import OverwriteStorage


class BaseModel(models.Model):
    """Base Model for the models of this app."""

    class Meta:
        """Define attributes of the Meta class."""

        abstract = True
        """Make this an abstract class in order to be used as an enhanced base model"""

    creation_timestamp = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name="Creation time"
    )
    """Creation timestamp, autogenerated upon creation"""

    update_timestamp = models.DateTimeField(
        auto_now=True, editable=False, verbose_name="Last Updated"
    )
    """Update timestamp, autogenerated upon creation and autoupdated on every update"""

class Token(rest_framework.authtoken.models.Token):
    """Custome Token model with ForeignKey relation to User model. Based on the DRF Token model."""

    key = models.CharField(_("Key"), max_length=40, db_index=True, unique=True, blank=True)
    """ Key attribute (the token string). It is no longer primary key, but still indexed and unique"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='auth_tokens',
        on_delete=models.CASCADE, verbose_name=_("User")
    )
    """ Relation to User model, it is a ForeignKey, so each user can have more than one token"""

    def __str__(self):
        """Define the string representation for objects of this class.

        Returns
        -------
        self.key: string
            The string representaiton, it is currently just the Token.key attribute
        """
        return self.key


class GlobalPermissions(models.Model):
    """Database-less model for custom Permissions."""

    class Meta:
        """The Meta class of this class."""

        managed = False
        """boolean: Define wether or not the model will be managed by the ORM (saved in the DB)"""

        permissions = (
            ('command.execute_command', 'Execute Commands'),
            ('command.run_script', 'Run and Requeue scripts in ScriptQueues'),
        )
        """((string, string)): Tuple defining permissions in the format ((<name>, <description>))"""

class ConfigFile(BaseModel):
    """ConfigFile Model, that includes actual configuration files, creation date and user."""
    
    def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = ['.json', '.sh']
        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file extension.')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='config_files',
        on_delete=models.CASCADE, verbose_name= "User"
    )

    file_name = models.CharField(max_length=30, blank=True)
    """The custom name for the configuration"""

    config_file = models.FileField(
        upload_to="configs/",
        default="configs/default.json",
        validators=[validate_file_extension],
    )
    """Order of the View within the Workspace."""

    # def __str__(self):
    #     """Redefine how objects of this class are transformed to string."""
    #     if self.view_name and self.view_name != "":
    #         return "{}: {} - {}".format(
    #             self.view_name, self.workspace.name, self.view.name
    #         )
    #     else:
    #         return "{} - {}".format(self.workspace.name, self.view.name)
