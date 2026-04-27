class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        current_fleet_time = 0.0
        
        for p, s in cars:
            time_to_reach = (target - p) / s
            
            if time_to_reach > current_fleet_time:
                fleets += 1
                current_fleet_time = time_to_reach
                
        return fleets