from collections import Counter
from itertools import combinations

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        d = defaultdict(int)
        for b,u in boxTypes:
            d[u] += b

        u = Counter(d)
        print(d)
        units = list(u.elements())
        print(units)

        max_units = 0
        n_boxes = list()

        for i in range(truckSize, 1, -1):
            combs = list(set(combinations(units, i)))
            for comb in combs:
                n_units = sum(comb)
                print(i, comb, n_units)
                if n_units > max_units:
                    max_units = n_units

        return max_units
