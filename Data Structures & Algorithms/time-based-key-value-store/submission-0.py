class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if self.dict[key] == "":
            return ""
        else:
            values = self.dict[key]
            l = 0
            r = len(values) - 1 
            while l<=r: 
                middle = (l+r)//2
                if values[middle][0] == timestamp: 
                    return values[middle][1]
                elif values[middle][0] < timestamp : 
                    l = middle + 1
                else: 
                    r = middle - 1
            if r >= 0: 
                return values[r][1]
            else:
                return ""