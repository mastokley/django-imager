from django.test import TestCase
from .models import ImagerProfile
from django.contrib.auth.models import User


# Create your tests here.
class ImagerProfileModel(TestCase):

    def test_profile_created_for_user(self):
        """
        Instantiating a new user object instantiates and links
        a new user record object
        """
        new_user = User.objects.create_user(username='bob')
        self.assertEquals(new_user, new_user.profile.user)

    def test_dunder_str(self):
        new_user = User.objects.create_user(username='bob')
        profile = new_user.profile
        self.assertEquals(p)
