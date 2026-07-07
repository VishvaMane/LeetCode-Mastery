from collections import defaultdict
from sortedcontainers import SortedList
from typing import List

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = defaultdict(SortedList)      # movie -> sorted (price, shop)
        self.price = {}                               # (shop, movie) -> price
        self.rented = SortedList()                    # sorted (price, shop, movie)

        for shop, movie, p in entries:
            self.available[movie].add((p, shop))
            self.price[(shop, movie)] = p

    def search(self, movie: int) -> List[int]:
        return [shop for p, shop in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.available[movie].remove((p, shop))
        self.rented.add((p, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        p = self.price[(shop, movie)]
        self.rented.remove((p, shop, movie))
        self.available[movie].add((p, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for p, shop, movie in self.rented[:5]]