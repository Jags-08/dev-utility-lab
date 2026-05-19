# Autonomous Workload Redistribution Planner
import math
import random

class RedistributionPlanner:
    def __init__(self, region_map):
        self.region_map = region_map
        self.saturation_threshold = 0.85

    def check_and_rebalance(self, current_loads):
        rebalanced = False
        rebalance_plan = {}
        for region, load in current_loads.items():
            if load > self.saturation_threshold:
                overflow = load - self.saturation_threshold
                rebalance_plan[region] = -overflow
                rebalanced = True
        return rebalanced, rebalance_plan
