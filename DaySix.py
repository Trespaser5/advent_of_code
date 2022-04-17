import enum


class FishEventIndex(enum.Enum):
    BREED = 0
    RESET_TIME = 6
    NEW_FISH_TIMER = 7


class LanternFish(object):

    _internal_timer = 0
    _egg = False

    def __init__(self, initial_value, egg=False):

        self._egg = egg

        self._internal_timer = initial_value

    def get_timer(self):

        return self._internal_timer

    def has_egg(self):
        return self._egg

    def age(self):

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

    def __init__(self, fish, create=None, fish_class=LanternFish):

        self._fish = fish

        if create is not None:
            for start_time in create:
                self._fish.append(fish_class(start_time))

    def get_fish(self):
        return self._fish





