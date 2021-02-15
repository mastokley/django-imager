from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from .models import ImagerProfile

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def ensure_user_profile(sender, **kwargs):
    """Create user profile after new user has been created."""
    user_created = kwargs.get('created', False)
    if user_created:
        user = kwargs['instance']
        try:
            user_profile = ImagerProfile(user=user)
            user_profile.save()
        except (KeyError, ValueError):
            msg = "Unable to create new profile for user {}."
            logger.error(msg.format(user))


@receiver(post_delete, sender=User)
def delete_user_profile(sender, **kwargs):
    """Delete user profile after user has been deleted."""
    # NOTE: sender provides no kwargs that confirm deletion
    deleted_user = kwargs['instance']
    try:
        profile_to_delete = deleted_user.profile
        profile_to_delete.delete()
    # If already deleted, id == None and cannot be re-deleted
    except (AssertionError):
        pass
