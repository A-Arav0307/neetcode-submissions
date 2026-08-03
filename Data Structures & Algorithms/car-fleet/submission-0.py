class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        new_list = sorted(position_speed, key=lambda x: x[0], reverse=True) 
        #[(7, 1), (4, 2), (1, 2), (0, 1)]
        [3, 3, 4.5, 10]
        time = [0] * len(position)
        for i in range(len(new_list)-1, -1, -1):
            time[i] = (target - new_list[i][0]) / new_list[i][1]

        for i in range(len(time)-1, 0, -1): 
            if time[i] <= time[i-1]:
                time.pop()


        return len(time) 