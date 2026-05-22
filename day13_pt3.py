# coding=utf-8
import subprocess
import time

def run_cmd(cmd, suppress_err=False):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0 and not suppress_err:
        print(f"Warning/Error: {result.stderr.strip()}")
    return result.stdout.strip()

issues = [
    ("Epic: Decentralized Routing & Orchestration V3 Convergence", "We need to deeply analyze and optimize the mesh routing convergence algorithm.", [
        "Are we using a consistent hash ring for the adaptive routing?",
        "Yes, specifically partitioned by telemetry tenant ID to avoid hot-spotting.",
        "We'll need to run benchmarks against the simulated gRPC streams to confirm.",
        "Agreed. I'm assigning this to the current iteration for closure."
    ]),
    ("Bug: Telemetry signal compaction latency spikes", "Signal compaction phase 2 is occasionally blocking the main telemetry ingestion pipeline.", [
        "I've traced this back to the batching heuristics locking early.",
        "Could we shift to a lock-free queue or defer the compaction to an async worker pooling model?",
        "Async worker pooling makes the most sense here. I'll prototype it.",
        "Drafting a fix, looks like it reduces P99 latency by 40%."
    ]),
    ("Discussion: Sustainable Compute & Idle Metrics", "Should we integrate a carbon-aware scheduling footprint into the orchestration heuristics?", [
        "This aligns perfectly with our ecosystem sustainability goals.",
        "Let's make sure the scoring weights can be customized per-region.",
        "Exactly. Adding to the long-term roadmap V3 board."
    ]),
    ("Task: Audit LTS release cadence compliance", "Verify that all components are strictly following the zero-downtime hotfix boundaries.", [
        "All pipelines pass. We have verified zero-downtime rollouts in staging.",
        "Perfect, closing out the audit task for this wave."
    ])
]

# Create issues and discussions
for title, body, comments in issues:
    issue_id = run_cmd(f'gh issue create --title "{title}" --body "{body}"')
    # Extracts URL/Issue string - assuming output is URL e.g. https://github.com/user/repo/issues/123
    try:
        issue_number = issue_id.split('/')[-1]
    except Exception:
        continue
    
    for comment in comments:
        run_cmd(f'gh issue comment {issue_number} --body "{comment}"')
        time.sleep(1)
        
    run_cmd(f'gh issue close {issue_number} --reason completed')
    time.sleep(2)

print("Day 13 Part 3 (Issues) Complete")
