class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        mapped = dict()
        for arr in paths:
            a, b = arr
            mapped[a] = b
        print(mapped)
        for key, value in mapped.items():
            if value not in mapped:
                return value
    
