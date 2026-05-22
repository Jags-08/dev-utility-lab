# coding=utf-8
import subprocess
import time

def run_cmd(cmd, suppress_err=False):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0 and not suppress_err:
        print(f"Warning/Error: {result.stderr.strip()}")
    return result.stdout.strip()

repos_to_star = [
    "kubernetes/kubernetes",
    "prometheus/prometheus",
    "open-telemetry/opentelemetry-go",
    "istio/istio",
    "envoyproxy/envoy",
    "cncf/toc",
    "grafana/grafana",
    "hashicorp/terraform",
    "apache/kafka",
    "etcd-io/envoy",
    "moby/moby",
    "cilium/cilium",
    "argoproj/argo-cd",
    "fluxcd/flux2",
    "containous/moby",
    "containerd/containerd",
    "opencontainers/runc",
    "goharbor/harbor",
    "traefik/traefik",
    "crossplane/crossplane"
]

print("Starting Ecosystem Visibility Engine (Starring Repos)...")
for repo in repos_to_star:
    run_cmd(f'gh api -X PUT "user/starred/{repo}"', suppress_err=True)
    time.sleep(1)

print("Day 13 Part 4 Complete")
