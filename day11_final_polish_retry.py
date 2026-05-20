# coding=utf-8
import os
import subprocess
import time

def run_cmd(cmd, suppress_err=False):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0 and not suppress_err:
        print(f"Warning/Error: {result.stderr.strip()}")
    return result.stdout.strip()

def create_file(path, content):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")
    print(f"Created/Updated {path}")

run_cmd("git config --global user.name")
run_cmd("git checkout main && git pull origin main", True)

# PR 1: Ecosystem Readability & LTS Polish (RETRY)
branch1 = "docs/ecosystem-polish-v2"
run_cmd(f"git checkout -B {branch1}")

create_file("docs/SUPPORT_LIFECYCLE_MATRICES.md", '''# LTS Support Lifecycle
| Version | Status | Active Support | Security Support |
|---------|--------|----------------|------------------|
| v3.x    | 🟢 LTS  | Dec 2026       | Dec 2027         |
| v2.x    | 🟡 Maint| -              | Jan 2027         |
| v1.x    | 🔴 EOL  | -              | -                |

*Federation stability is guaranteed across all v3.x minor releases.*
''')

create_file("docs/CONTRIBUTING_QUICKSTART_V2.md", '''# Contributor Navigation
- **Architecture**: See `README.md`
- **Telemetry Ingress**: `src/warehouse/`
- **Orchestration**: `dev_utils/federation/`
- **Reliability Validation**: `dev_utils/reliability/`
''')

run_cmd('git add . && git commit -m "docs: formalize LTS support lifecycle and contributor matrices"')
run_cmd(f"git push -f origin {branch1}")
run_cmd(f'gh pr create --title "Docs: Ecosystem Readability & LTS Support Matrices" --body "Polishes contributor discovery paths and publishes the formal LTS lifecycle for v3.x."')
time.sleep(2)
run_cmd(f"gh pr merge {branch1} --squash --delete-branch")

# PR 2: Governance & Roadmap Cleanup (RETRY)
run_cmd("git checkout main && git pull origin main", True)
branch2 = "chore/governance-cleanup-v2"
run_cmd(f"git checkout -B {branch2}")

create_file("ROADMAP_GA.md", '''# Ecosystem Roadmap
## Completed (v3.0.0 GA)
- Distributed telemetry federation
- Predictive routing & QoS bounds
- Replay governance & automation
- Autonomic balancing heuristics

## Horizon (v4.x)
- Ergonomic improvements for platform engineers
- Seamless edge-node dependency management
- Standardized cross-region tracing standards
''')

run_cmd('git add ROADMAP_GA.md && git commit -m "chore: prune roadmap to reflect v3.0.0 GA completion and v4 horizon metrics"')
run_cmd(f"git push -f origin {branch2}")
run_cmd(f'gh pr create --title "Chore: Roadmap & Governance Cleanup" --body "Trims legacy roadmap items into the completed GA tier and focuses the horizon purely on ergonomics and stability."')
time.sleep(2)
run_cmd(f"gh pr merge {branch2} --squash --delete-branch")

print("Retry Complete")
