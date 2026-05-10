import sys

from flask import Blueprint, render_template

import dev_utils
from benchmarks.benchmark_core import run_benchmarks
from dashboard.services.dispatcher import TOOL_REGISTRY

pages_bp = Blueprint('pages', __name__)

@pages_bp.route("/")
def index() -> str:
    system_info = {
        "python_version": sys.version.split(" ")[0],
        "package_version": dev_utils.__version__,
        "loaded_modules": len(sys.modules),
        "total_tools": len(TOOL_REGISTRY)
    }
    return render_template("index.html", sys_info=system_info)

@pages_bp.route("/benchmarks")
def benchmarks() -> str:
    results = run_benchmarks()
    return render_template("benchmarks.html", results=results)

@pages_bp.route("/examples")
def examples() -> str:
    return render_template("examples.html")

@pages_bp.route("/playground")
def playground() -> str:
    return render_template("playground.html", tools=TOOL_REGISTRY.keys())

@pages_bp.route("/docs")
def docs() -> str:
    return render_template("docs.html")
