class TopologyAwareScheduler:
    def align_workload(self, task, region_affinity):
        return f"Executing {task} explicitly in {region_affinity}"
