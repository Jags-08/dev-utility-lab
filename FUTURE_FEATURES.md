# Future Features: dev-utility-lab

While the core of `dev-utility-lab` is stable, the following features are targeted for future development. These are designed to be modular enhancements rather than monolithic additions.

## 1. CLI Enhancements
*   **Interactive Mode**: Add a REPL (Read-Eval-Print Loop) mode to `dev-utils` for chaining commands without returning to the shell.
*   **Config Profiles**: Allow users to save frequently used parameter sets (e.g., standard password length and complexity) via a `~/.dev-utils.yaml` file.
*   **Tab Completion**: Implement shell completions for Bash, Zsh, and PowerShell for utility names and arguments.

## 2. Dashboard Improvements
*   **Authentication**: Introduce lightweight API key management for the dashboard to restrict access in exposed environments.
*   **Persistent Automation**: Allow saving workflows created in the dashboard to a local SQLite database for later retrieval.
*   **Export Enhancements**: Enable exporting benchmark and telemetry data to Prometheus or Grafana formats.

## 3. Core Utilities Expansion
*   **Data Serialization**: Add utilities for fast conversion between JSON, YAML, and TOML.
*   **Cryptographic Helpers**: Provide simple, secure hashing and verifying wrappers (e.g., Argon2) that wrap standard libraries safely.
*   **Network Ops**: Provide basic port-scanning or ping utilities for environment sanity checks.

## 4. Extensibility
*   **Plugin Protocol Finalization**: Complete the implementation of `plugins/plugin_loader.py` to allow the community to dynamically load custom Python scripts as first-class utilities in the dashboard/CLI.
