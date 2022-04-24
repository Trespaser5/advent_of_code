import enum, threading


class FishEventIndex(enum.Enum):
    BREED = 0
    RESET_TIME = 6
    NEW_FISH_TIMER = 8


class LanternFish(object):

    _internal_timer = 0
    _egg = False
    _just_hatched = False

    def __init__(self, initial_value, egg=False, just_hatched=False):

        self._egg = egg
        self._internal_timer = initial_value
        self._just_hatched = just_hatched

    def __repr__(self):
        return str(self._internal_timer)

    def get_timer(self):

        return self._internal_timer

    def has_egg(self):
        return self._egg

    def age(self):

        if self._just_hatched:
            # reset just hatched state but do not age
            return self.__class__(self._internal_timer, self._egg)

        else:

            new_time = self._internal_timer -1

            return self.__class__(new_time, self._egg)._check_for_event(new_time)

    def _check_for_event(self, time_value):

        fe = FishEventIndex

        try:
            return {fe.BREED.value: self.lay_egg()}[time_value]
        except KeyError:
            return self

    def lay_egg(self):
        # create a new fish object
        return self.__class__(self._internal_timer, egg=True)


class Shoal(object):

    _fish = []
    _fish_class = None

    def __init__(self, fish, create=None, fish_class=LanternFish):

        self._fish = fish
        self._fish_class = fish_class

        if create is not None:
            for start_time in create:
                self._fish.append(fish_class(start_time))

    def get_fish(self):
        return self._fish

    def get_size(self):
        return len(self._fish)

    def hatch(self):

        shoal = self._fish

        for i, fish in enumerate(shoal):
            if fish.has_egg():
                shoal[i] = self._fish_class(FishEventIndex.RESET_TIME.value, just_hatched=True)
                shoal.append(self._fish_class(FishEventIndex.NEW_FISH_TIMER.value, just_hatched=True))

        return Shoal(shoal)

    def pass_days(self, days):

        new_shoal = self

        for day in range(0, days+1):
            if day > 0:
                new_shoal = new_shoal.hatch()
                new_shoal = Shoal(fish=[fish.age() for fish in new_shoal.get_fish()])

        return new_shoal

    def pass_one_day(self):

        new_shoal = self

        new_shoal = new_shoal.hatch()
        new_shoal = Shoal(fish=[fish.age() for fish in new_shoal.get_fish()])

        return new_shoal


class ShoalProcessing:

    _shoals = {}
    _threads = {}
    _temp_shoals = []

    def __init__(self, shoals=None, threads=None):

        if shoals is None:
            self._shoals = {}
        else:
            self._shoals = shoals

        if threads is None:
            self._threads = {}
        else:
            self._threads = threads

    def process_big(self, init_shoal, days_to_run):

        #enter try to handle empty array
        try:
            ci = [*self._shoals.keys()][-1:][0] + 1
        except IndexError:
            ci = 0

        if isinstance(init_shoal, list):
            self._shoals[ci]=(Shoal([], create=init_shoal))
        elif isinstance(init_shoal, Shoal):
            self._shoals[ci] = (init_shoal)
        else:
            raise ValueError("Shoal must of type list or Shoal")

        current_day = 0
        for day in range(0, days_to_run):

            self._shoals[ci] = self._shoals[ci].pass_one_day()
            print("day {}".format(day))

            if self._shoals[ci].get_size() > 600:
                current_day = day
                break

        days_left = days_to_run - current_day

        for chunk in [self._shoals[ci].get_fish()[i:i+200] for i in range(0, self._shoals[ci].get_size(), 200)]:

            try:
                ti = [*self._shoals.keys()][-1:][0] + 1
            except IndexError:
                ti = 0

            self._threads[ti] = \
                threading.Thread(target=self.process_big, args=([Shoal(chunk), days_left]))
            self._threads[ti].start()
            self._threads[ti].join()

    @staticmethod
    def return_shoal(shoals):

        return [fish for shoal in shoals.values() for fish in shoal.get_fish()]

    def shoal_size(self):

        size = 0

        for shoal in self._shoals.values():
            size += len(shoal.get_fish())

        return size












