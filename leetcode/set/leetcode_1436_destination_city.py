#leetcode_1436:-https://leetcode.com/problems/destination-city

from typing import List,Set, Dict


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source_cities: Set[str] = set()
        dest_cities: Set[str] = set()

        for source, dest in paths:
            source_cities.add(source)
            dest_cities.add(dest)

        return (dest_cities - source_cities).pop()

def destcity1(self, paths: List[List[str]]) -> str:
    # create a set of all sources cities
    sources = set(path[0] for path in paths)

    # Check each destination - if it's not a source, it's the final destination
    for _, destination in paths:
        if destination not in sources:
            return destination
