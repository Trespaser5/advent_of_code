import unittest
from DaySix import LanternFish, Shoal


class LanternFishTest(unittest.TestCase):

    def test_aging(self):

        lantern_fish = LanternFish(3)

        for i in range(0,2):
            lantern_fish = lantern_fish.age()

        self.assertEqual(lantern_fish.get_timer(), 1)

    def test_ay_egg(self):

        fish = LanternFish(3).lay_egg()

        self.assertEqual(fish.has_egg(), True)


class ShoalTest(unittest.TestCase):

    def test_create(self):

        shoal = Shoal([], create=[3,7])

        self.assertEqual(shoal.get_fish()[1].get_timer(), 7)








