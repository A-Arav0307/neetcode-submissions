class TimeMap:

    def __init__(self):
        self.storage = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value, timestamp]) 
    
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.storage:
            return ""
        values = self.storage[key]

        l = 0
        r = len(values) - 1

        result = ""

        while l <= r:
            mid = (l + r) // 2
            value, time = values[mid]
            if time <= timestamp:
                result = value
                l = mid + 1
            else:
                r = mid - 1

        return result