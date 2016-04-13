from __future__ import unicode_literals

from django.conf import settings

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
    ('af', 'Africa'),
    ('an', 'Antarctica'),
    ('as', 'Asia'),
    ('au', 'Australia'),
    ('eu', 'Europe'),
    ('no', 'North America'),
    ('so', 'South America'),
)


class ImagerProfileManager(models.Manager):
    def get_queryset(self):
        """Return set of all active users."""
        profiles = super(ImagerProfileManager, self).get_queryset()
        return profiles.filter(user__is_active=True)


@python_2_unicode_compatible
class ImagerProfile(models.Model):
    """Profile that stands in front of django's User model."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                null=False)
    camera = models.CharField(max_length=20, default='')
    photography_type = models.CharField(max_length=2,
                                        choices=PHOTOGRAPHY_TYPES,
                                        default='amateur')
    region = models.CharField(max_length=2, choices=REGIONS)

    def __str__(self):
        return self.user.username

    # order is important
    objects = models.Manager()  # return all user profiles
    active = ImagerProfileManager()  # return active user profiles

    @property  # can be used with attribute syntax (doesn't want to be called)
    def is_active(self):
        """Indicate whether the user is active (allowed to log in)"""
        return self.user.is_active

    # friends = models.ManyToManyField(settings.AUTH_USER_MODEL,
    #                                  symmetrical=False,
    #                                  related_name='friend_of')


