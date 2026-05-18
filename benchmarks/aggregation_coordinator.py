import statistics

def aggregate_benchmark_runs(runs):
    if not runs: return {}
    latencies = [run['latency'] for run in runs]
    return {
        "p50": statistics.median(latencies),
        "p99": statistics.quantiles(latencies, n=100)[98],
        "samples": len(latencies)
    }
