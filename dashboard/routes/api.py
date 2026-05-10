from flask import Blueprint, Response, jsonify, request

import dev_utils
from dashboard.services.dispatcher import TOOL_REGISTRY, dispatch_tool

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route("/health")
def health() -> Response:
    return jsonify({"status": "ok", "version": dev_utils.__version__})

@api_bp.route("/run-tool", methods=["POST"])
def run_tool() -> Response:
    data = request.get_json()
    if not data or "tool_id" not in data or "payload" not in data:
        err_msg = "Invalid request format. Provide tool_id and payload."
        return jsonify({"success": False, "error": err_msg}), 400
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@api_bp.route("/tools")
def list_tools() -> Response:
    tools_info = []
    for tool_id, spec in TOOL_REGISTRY.items():
        tools_info.append({
            "id": tool_id,
            "arguments": spec["args"] # type: ignore
        })
    return jsonify({"tools": tools_info})
