from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

from django.utils.encoding import python_2_unicode_compatible

PHOTOGRAPHY_TYPES = (
    ('ad', 'advertising'),
    ('am', 'amateur'),
    ('bl', 'black and white'),
    ('co', 'color'),
    ('co', 'commercial'),
    ('cr', 'crime scene'),
    ('ed', 'editorial'),
    ('fa', 'fashion'),
    ('fo', 'food'),
    ('la', 'landscape'),
    ('ph', 'photojournalism'),
    ('po', 'portrait and wedding'),
    ('st', 'still life'),
    ('wi', 'wildlife'),
)

REGIONS = (
    ('Af', 'Africa'),
    ('An', 'Antarctica'),
    ('As', 'Asia'),
    ('Au', 'Australia'),
    ('Eu', 'Europe'),
    ('No', 'North America'),
    ('So', 'South America'),
)


class ImagerProfileManager(models.Manager):
    def get_queryset(self):
        """Return set of all active users."""
        profiles = super(ImagerProfileManager, self).get_queryset()
        return profiles.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Profile that stands in front of django's User model."""
    user = models.OneToOneField(User, related_name='profile', null=False)
    camera = models.CharField(max_length=20, default='')
    photography_type = models.CharField(max_length=2,
                                        choices=PHOTOGRAPHY_TYPES,
                                        default='amateur')
    region = models.CharField(max_length=2, choices=REGIONS)

    def __str__(self):
        return self.user.username

    objects = models.Manager()  # return all users
    active = ImagerProfileManager()  # return only active users

    def is_active(self):
        """
        a property which returns a boolean value indicating whether the user
        associated with the given profile is active (allowed to log in)
        """
        return self.user.is_active



