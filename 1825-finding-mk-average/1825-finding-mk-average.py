from collections import deque
from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.n = m - 2 * k
        self.q = deque()
        self.left = SortedList()
        self.mid = SortedList()
        self.right = SortedList()
        self.mid_sum = 0

    def _add(self, x):
        if self.left and x <= self.left[-1]:
            self.left.add(x)
        elif self.right and x >= self.right[0]:
            self.right.add(x)
        else:
            self.mid.add(x)
            self.mid_sum += x
        self._rebalance()

    def _remove(self, x):
        if self.left and x <= self.left[-1]:
            self.left.remove(x)
        elif self.right and x >= self.right[0]:
            self.right.remove(x)
        else:
            self.mid.remove(x)
            self.mid_sum -= x
        self._rebalance()

    def _rebalance(self):
        while len(self.left) > self.k:
            x = self.left.pop()
            self.mid.add(x)
            self.mid_sum += x
        while len(self.left) < self.k and self.mid:
            x = self.mid.pop(0)
            self.mid_sum -= x
            self.left.add(x)

        while len(self.right) > self.k:
            x = self.right.pop(0)
            self.mid.add(x)
            self.mid_sum += x
        while len(self.right) < self.k and self.mid:
            x = self.mid.pop()
            self.mid_sum -= x
            self.right.add(x)

        while self.mid and self.left and self.mid[0] < self.left[-1]:
            a = self.left.pop()
            b = self.mid.pop(0)
            self.left.add(b)
            self.mid.add(a)
            self.mid_sum += a - b

        while self.mid and self.right and self.mid[-1] > self.right[0]:
            a = self.right.pop(0)
            b = self.mid.pop()
            self.right.add(b)
            self.mid.add(a)
            self.mid_sum += a - b

    def addElement(self, num: int) -> None:
        self.q.append(num)
        self._add(num)
        if len(self.q) > self.m:
            old = self.q.popleft()
            self._remove(old)

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        return self.mid_sum // self.n