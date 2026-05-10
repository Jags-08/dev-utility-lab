import os
import sys

from flask import Flask, Response, jsonify, render_template

# Adjust path if running from dashboard dir
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dev_utils
from benchmarks.benchmark_core import run_benchmarks

app = Flask(__name__)

@app.route("/")
def index() -> str:
    system_info = {
        "python_version": sys.version.split(" ")[0],
        "package_version": dev_utils.__version__,
        "loaded_modules": len(sys.modules)
    }
    return render_template("index.html", sys_info=system_info)

@app.route("/benchmarks")
def benchmarks() -> str:
    results = run_benchmarks()
    return render_template("benchmarks.html", results=results)

@app.route("/examples")
def examples() -> str:
    return render_template("examples.html")

@app.route("/health")
@app.route("/api/health")
def health() -> Response:
    return jsonify({"status": "ok", "version": dev_utils.__version__})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
