from django.test import TestCase
from .models import ImagerProfile
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist


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

    def test_active_method_setup(self):
        """
        Does the .active method on ImagerProfile return all active
        users?
        """
        new_user_sally = User.objects.create_user(username='sally')
        new_user_sally.is_active = False
        new_user_sally.save()  # to commit update of attrib.
        self.assertEquals(new_user_sally.is_active, False)

    def test_active_method_including(self):
        """
        Does the .active method on ImagerProfile return all active
        users?
        """
        new_user_bob = User.objects.create_user(username='bob')
        active_user_profiles = ImagerProfile.active.all()
        self.assertIn(new_user_bob.profile, active_user_profiles)

    def test_object_get_query(self):
        """
        Does the .active method on ImagerProfile return all active
        users?
        """
        new_user_susan = User.objects.create_user(username='susan')
        new_user_susan.is_active = False
        new_user_susan.save()  # to commit update of attrib.
        all_users = User.objects.all()
        self.assertIn(new_user_susan, all_users)

    def test_query_filter_excluding(self):
        """
        Does the .active method on ImagerProfile return all active
        users?
        """
        new_user_salamander = User.objects.create_user(username='salamander')
        new_user_salamander.is_active = False
        new_user_salamander.save()  # to commit update of attrib.
        all_profiles = ImagerProfile.objects.all()
        filtered_user_set = all_profiles.filter(user__is_active=True)
        self.assertNotIn(new_user_salamander, filtered_user_set)

    def test_active_excluding(self):
        """
        Does the .active method on ImagerProfile return all active
        users?
        """
        new_user_susan = User.objects.create_user(username='susan')
        new_user_susan.is_active = False
        new_user_susan.save()  # to commit update of attrib.
        active_user_profiles = ImagerProfile.active.all()
        self.assertNotIn(new_user_susan.profile, active_user_profiles)
