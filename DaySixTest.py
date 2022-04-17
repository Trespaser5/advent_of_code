import unittest
from DaySix import LanternFish


class LanternFishTest(unittest.TestCase):

    def test_aging(self):

        lantern_fish = LanternFish(3)

        for i in range(0,2):
            lantern_fish = lantern_fish.age()[0]

        self.assertEqual(lantern_fish.get_timer(), 1)

    def test_breeding(self):

        lantern_fish = LanternFish(3)

        shoal = [lantern_fish]







