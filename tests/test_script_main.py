from unittest import TestCase

from bin.get_testids import main

class TestCmd(TestCase):
    def test_basic(self):
        main(None)