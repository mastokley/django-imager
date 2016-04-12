from django.db.models.signals import post_save
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
    pass
