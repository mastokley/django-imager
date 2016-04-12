from django.test import TestCase
from .models import ImagerProfile
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist

# Create your tests here.
class ImagerProfileModel(TestCase):

    def test_profile_created_for_user(self):
        """
        Instantiating a new user object instantiates and links
        a new user record object
        """
        new_user_bob = User.objects.create_user(username='bob')
        self.assertEquals(new_user_bob, new_user_bob.profile.user)

    def test_dunder_str(self):
        """Is my profile object displaying appropriately in the shell?"""
        new_user_bob = User.objects.create_user(username='bob')
        profile = new_user_bob.profile
        self.assertEquals(profile.__str__(), 'bob')

    def test_profile_deletes_on_user_delete(self):
        """
        When I delete a user record, is the profile also deleted?
        """
        new_user_bob = User.objects.create_user(username='bob')
        new_user_bob.save()
        profile_id = new_user_bob.profile.id
        new_user_bob.delete()

        # NOTE: I have not written any delete receiver
        # profile records are apparently being deleted automagically
        with self.assertRaises(ObjectDoesNotExist):
            ImagerProfile.objects.get(id=profile_id)

    def test_active_method(self):
        """
        Does the .active method on ImagerProfile return all active
        users?
        """
        new_user_bob = User.objects.create_user(username='bob')
        new_user_sally = User.objects.create_user(username='sally')

