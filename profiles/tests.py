from django.test import TestCase
from .models import UserProfile


class UserProfileTestCase(TestCase):
    # Lets test the UserProfile model
    # Here we are creating two new users
    def setUp(self):
        UserProfile.objects.create(
            full_name="Ben Smith",
            default_phone_number="07833928174",
            default_street_address1="12 Oxford Street",
            default_street_address2="Somewhere Faraway",
            default_town_or_city="Inarandom Town",
            default_postcode="B32 1TG",
        )
        UserProfile.objects.create(
            full_name="Andy Cole",
            default_phone_number="07983726184",
            default_street_address1="16 New Street",
            default_street_address2="Somewhere Else",
            default_town_or_city="New City",
            default_postcode="B16 2RF",
        )

    # This test is going to check the phone numbers
    def test_user_phone_number(self):
        user1 = UserProfile.objects.get(full_name="Ben Smith")
        user2 = UserProfile.objects.get(full_name="Andy Cole")
        self.assertEqual(user1.default_phone_number, "07833928174")
        self.assertEqual(user2.default_phone_number, "07983726184")

    # This test is going to check the phone numbers
    def test_user_street_address1(self):
        user1 = UserProfile.objects.get(full_name="Ben Smith")
        user2 = UserProfile.objects.get(full_name="Andy Cole")
        self.assertEqual(user1.default_street_address1, "12 Oxford Street")
        self.assertEqual(user2.default_street_address1, "16 New Street")


# These tests won't pass because I have no user ID
