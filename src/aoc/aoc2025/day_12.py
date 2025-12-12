from typing import Any
from ..utils.day import Day
from ..utils import aoc
import re

class Day12(Day):

    def day(self, _input: str) -> Any:
        for line in aoc.yield_line(_input):

            if "x" not in line:
                continue

            m = re.match(r"^\s*(\d+)x(\d+):\s*(.*)$", line)
            self.ans1 += (((int(m.group(1)) // 3) * (int(m.group(2)) // 3)) >= sum([int(x) for x in m.group(3).strip().split()]))

        return (self.ans1, self.ans2)

