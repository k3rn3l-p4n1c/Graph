"""
A simple Test which need to be replaced with more appropriate tests
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

"""



from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 5+5 always equals 10.
        """
        self.assertEqual(5+5, 10)
