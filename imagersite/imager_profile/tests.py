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

        # profile records are apparently being deleted automagically
        with self.assertRaises(ObjectDoesNotExist):
            ImagerProfile.objects.get(id=profile_id)

    def test_active_method_setup(self):
        """
        Can I manually assign .is_active to False?
        """
        new_user_sally = User.objects.create_user(username='sally')
        new_user_sally.is_active = False
        new_user_sally.save()  # to commit update of attrib.
        self.assertEquals(new_user_sally.is_active, False)

    def test_active_method_including(self):
        """
        Does the .active method on ImagerProfile include all active
        users?
        """
        new_user_bob = User.objects.create_user(username='bob')
        active_user_profiles = ImagerProfile.active.all()
        self.assertIn(new_user_bob.profile, active_user_profiles)

    def test_object_get_query(self):
        """
        Does the .objects.all() method on ImagerProfile return all users?
        """
        new_user_susan = User.objects.create_user(username='susan')
        new_user_susan.is_active = False
        new_user_susan.save()  # to commit update of attrib.
        all_users = User.objects.all()
        self.assertIn(new_user_susan, all_users)

    def test_query_filter_excluding(self):
        """
        Does the .objects.all() method on ImagerProfile return all active
        users and filter in a predictable way?
        """
        new_user_salamander = User.objects.create_user(username='salamander')
        new_user_salamander.is_active = False
        new_user_salamander.save()  # to commit update of attrib.
        all_profiles = ImagerProfile.objects.all()
        filtered_profile_set = all_profiles.filter(user__is_active=True)
        self.assertNotIn(new_user_salamander.profile, filtered_profile_set)

    def test_objects_all_returns_intact(self):
        """
        When I get susanna back, will she still be set to .is_active == False?
        """
        new_user_susanna = User.objects.create_user(username='susanna')
        new_user_susanna.is_active = False
        new_user_susanna.save()  # to commit update of attrib.
        self.assertEquals(new_user_susanna.is_active, False)
        user_profiles = ImagerProfile.objects.all()
        self.assertEquals(user_profiles[0].user.is_active, False)

    def test_active_excluding(self):
        """
        Does the .active method on ImagerProfile exclude inactive
        users?
        """
        new_user_susanna = User.objects.create_user(username='susanna')
        new_user_susanna.is_active = False
        new_user_susanna.save()  # to commit update of attrib.
        active_user_profiles = ImagerProfile.active.all()
        self.assertNotIn(new_user_susanna.profile, active_user_profiles)

    def test_is_active_method(self):
        """
        Does the profile.is_active method return the user.is_active method?
        """
        new_user_samuel = User.objects.create_user(username='samuel')
        new_user_samuel.save()
        self.assertEqual(new_user_samuel.is_active,
                         new_user_samuel.profile.is_active)
