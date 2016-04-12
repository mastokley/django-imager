from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

PHOTOGRAPHY_TYPES = (
    ('co', 'color'),
    ('bl', 'black and white'),
    ('la', 'landscape'),
    ('st', 'still life'),
    ('co', 'commercial'),
    ('ad', 'advertising'),
    ('fo', 'food'),
    ('ph', 'photojournalism'),
    ('po', 'portrait and wedding'),
    ('wi', 'wildlife'),
    ('am', 'amateur'),
    ('cr', 'crime scene'),
    ('fa', 'fashion'),
    ('ed', 'editorial')
)

REGIONS = (
    ('Af', 'Africa'),
    ('Eu', 'Europe'),
    ('As', 'Asia'),
    ('No', 'North America'),
    ('So', 'South America'),
    ('An', 'Antarctica'),
    ('Au', 'Australia'),
)


class ImagerProfileManager(models.Manager):
    def get_active_users(self):
        """Return set of all active users."""
        profiles = super(ImagerProfileManager, self).get_queryset()
        return profiles.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Profile that stands in front of django's User model."""

    camera = models.CharField(max_length=20)
    photography_type = models.CharField(max_length=2,
                                        choices=PHOTOGRAPHY_TYPES,
                                        default='amateur')
    region = models.CharField(max_length=2, choices=REGIONS)
    user = models.OneToOneField(User, related_name='profile', null=False)

    def __str__(self):
        return self.user.username

    objects = models.Manager()  # return all users
    active = ImagerProfileManager()  # return only active users

    def is_active(self):
        """
        a property which returns a boolean value indicating whether the user
        associated with the given profile is active (allowed to log in)
        """
        pass



