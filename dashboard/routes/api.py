import functools
import json
import time
from typing import Any, Dict

import psutil  # type: ignore
from flask import Blueprint, Response, jsonify, request

import dev_utils
from dashboard.services.dispatcher import TOOL_REGISTRY, dispatch_tool

api_bp = Blueprint("api", __name__, url_prefix="/api")
START_TIME = time.time()

# Simple telemetry wrapper structure
telemetry_stats = {"total_requests": 0, "successful_executions": 0, "failed_executions": 0}


@api_bp.before_request
def track_requests() -> None:
    if request.path.startswith("/api/run-tool"):
        telemetry_stats["total_requests"] += 1


@api_bp.route("/health")
def health() -> Response:
    return jsonify({"status": "ok", "version": dev_utils.__version__})


@api_bp.route("/system-info")
def system_info() -> Response:
    """Production telemetry for hardware and OS status."""
    uptime_sec = time.time() - START_TIME
    try:
        mem = psutil.virtual_memory()
        cpu = psutil.cpu_percent(interval=0.1)
        system_stats = {
            "uptime_seconds": round(uptime_sec, 2),
            "cpu_usage_percent": cpu,
            "memory_usage_percent": mem.percent,
            "memory_available_mb": round(mem.available / (1024 * 1024), 2),
        }
    except Exception:
        system_stats = {
            "uptime_seconds": round(uptime_sec, 2),
            "cpu_usage_percent": 0.0,
            "memory_usage_percent": 0.0,
            "memory_available_mb": 0.0,
        }
    return jsonify(system_stats)


@api_bp.route("/metrics")
def metrics() -> Response:
    return jsonify(telemetry_stats)


@functools.lru_cache(maxsize=128)
def cached_dispatch(tool_id: str, payload_frozen: str) -> Dict[str, Any]:
    payload = json.loads(payload_frozen)
    return dispatch_tool(tool_id, payload)


@api_bp.route("/run-tool", methods=["POST"])
def run_tool() -> tuple[Response, int]:
    if request.content_length and request.content_length > 1024 * 1024:
        return jsonify({"success": False, "error": "Payload too large. Max 1MB."}), 413

    data = request.get_json()
    if not data or "tool_id" not in data or "payload" not in data:
        err_msg = "Invalid request format. Provide tool_id and payload."
        telemetry_stats["failed_executions"] += 1
        return jsonify({"success": False, "error": err_msg}), 400

    tool_id = data["tool_id"]
    payload_frozen = json.dumps(data["payload"], sort_keys=True)

    if "random/" not in tool_id:
        result = cached_dispatch(tool_id, payload_frozen)
    else:
        result = dispatch_tool(tool_id, data["payload"])

    if result.get("success"):
        telemetry_stats["successful_executions"] += 1
        return jsonify(result), 200
    else:
        telemetry_stats["failed_executions"] += 1
        return jsonify(result), 400


@api_bp.route("/tools")
def list_tools() -> Response:
    tools_info = []
    for tool_id, spec in TOOL_REGISTRY.items():
        tools_info.append(
            {
                "id": tool_id,
                "arguments": spec.get("args", {}),
            }
        )
    return jsonify({"tools": tools_info})
