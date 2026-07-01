class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position, speed))
        new_list = sorted(position_speed, key=lambda x: x[0], reverse=True) 
        #[(4, 1), (2, 3), (0, 2)]
        
        [6, 2.66, 5]
        time = [0] * len(position)
        for i in range(len(new_list)-1, -1, -1):
            time[i] = (target - new_list[i][0]) / new_list[i][1]

        for i in range(len(time)-1, 0, -1): 
            for j in range(i-1, -1, -1):
                if time[i] <= time[j]:
                    time.pop()
                    break


        return len(time) 