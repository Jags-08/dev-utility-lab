class SnapshotCompactor:
    def compact(self, snapshots): return [snapshots[-1]] if snapshots else []
