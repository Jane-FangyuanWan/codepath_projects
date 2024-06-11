class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sta_cities, end_cities = set(), set()
        
        for sta_city, end_city in paths:
            sta_cities.add(sta_city)
            end_cities.add(end_city)

        for end_city in end_cities:
            if end_city not in sta_cities:
                return end_city