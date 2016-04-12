from django.test import TestCase
from .models import ImagerProfile
from django.contrib.auth.models import User

# Create your tests here.
class ImagerProfileModel(TestCase):

    def test_profile_created_for_user(self):
        new_user = User.objects.create_user(username='bob')
        self.assertEquals(new_user.profile, new_user.profile.user)
