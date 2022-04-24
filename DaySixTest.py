import unittest
from DaySix import LanternFish, Shoal, ShoalProcessing
import threading


class LanternFishTest(unittest.TestCase):

    def test_aging(self):

        lantern_fish = LanternFish(3)

        for i in range(0,2):
            lantern_fish = lantern_fish.age()

        self.assertEqual(lantern_fish.get_timer(), 1)

    def test_lay_egg(self):

        fish = LanternFish(3).lay_egg()

        self.assertEqual(fish.has_egg(), True)


class ShoalTest(unittest.TestCase):

    def test_create(self):

        shoal = Shoal([], create=[3,7])

        self.assertEqual(shoal.get_fish()[1].get_timer(), 7)

    def test_hatch(self):

        shoal = Shoal([LanternFish(3, egg=True)])

        shoal = shoal.hatch()

        self.assertEqual(len(shoal.get_fish()), 2)

    def test_pass_days(self):

        shoal = Shoal([LanternFish(3)])

        self.assertEqual(len(shoal.pass_days(5).get_fish()), 2)

    def test_day_6_task_1(self):

        shoal = Shoal([], create=[3,4,3,1,2])

        shoal1 = shoal.pass_days(18)
        shoal2 = shoal.pass_days(80)

        self.assertEqual(len(shoal1.get_fish()), 26)
        self.assertEqual(len(shoal2.get_fish()), 5934)

    def test_day_6_task_1_sp(self):

        init_shoal = [3,4,3,1,2]

        sp1 = ShoalProcessing()
        sp1.process_big(init_shoal, 18)

        self.assertEqual(sp1.shoal_size(), 26)

        sp2 = ShoalProcessing()
        sp2.process_big(init_shoal, 80)

        self.assertEqual(sp2.shoal_size(), 5934)

    def test_task_1(self):

        with open("d6t1.txt") as f:
            existing_shoal = [int(character) for character in f.read() if character.isdigit()]

        sp1 = ShoalProcessing()
        sp1.process_big(existing_shoal, 80)

        self.assertEqual(sp1.shoal_size(), 374927)
    """
    def test_task_2(self):

        with open("d6t1.txt") as f:
            existing_shoal = [int(character) for character in f.read() if character.isdigit()]

        sp1 = ShoalProcessing()
        sp1.process_big(existing_shoal, LanternFish, threading.Thread, 256)

        self.assertEqual(sp1.shoal_size(), 374927)
        """


"""
    def test_task_2(self):

        with open("d6t1.txt") as f:
            existing_shoal = [int(character) for character in f.read() if character.isdigit()]

        self.assertEqual(len(Shoal([], create=existing_shoal).pass_days(256).get_fish()), 374927)
    """





