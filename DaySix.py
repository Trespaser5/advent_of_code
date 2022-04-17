import enum


class FishEventIndex(enum.Enum):
    BREED = 0
    RESET_TIME = 6
    NEW_FISH_TIMER = 7


class LanternFish(object):

    _internal_timer = 0

    def __init__(self, initial_value):

        self._internal_timer = initial_value

    def get_timer(self):

        return self._internal_timer

    def age(self):

        new_timer_value = self._internal_timer - 1

        return [LanternFish(new_timer_value), self._check_for_event(new_timer_value)]

    def _check_for_event(self, time_value):

        fe = FishEventIndex

        try:
            return {fe.BREED.value: self.breed(self.__class__)}[time_value]
        except KeyError:
            return None

    @staticmethod
    def breed(fish_class):
        # create a new fish object
        return fish_class(FishEventIndex.NEW_FISH_TIMER)

