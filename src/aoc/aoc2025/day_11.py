from functools import lru_cache
from typing import Any
from ..utils.day import Day
from ..utils import aoc

racks = {}

@lru_cache(maxsize=10000)
def search_path_size(string: str, part1: bool, fft: bool = False, dac: bool = False) -> int:

    if string == "out":
        return part1 or (fft and dac)

    fft = not part1 and (fft or string == "fft")
    dac = not part1 and (dac or string == "dac")

    return sum([search_path_size(next, part1, fft, dac) for next in racks[string]])

class Day11(Day):

    def day(self, _input: str) -> Any:
        global racks
        for line in aoc.yield_line(_input):
            key, values = line.split(":", 1)
            racks[key.strip()] = values.strip().split()

        return (search_path_size("you", True), search_path_size("svr", False))
