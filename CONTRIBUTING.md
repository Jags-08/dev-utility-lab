# Contributing to dev-utility-lab

First off, thank you for considering contributing to `dev-utility-lab`! It's people like you that make open-source a great community.

## Code of Conduct
By participating in this project, you are expected to uphold standard open-source professional conduct. Please be welcoming and respectful to all members.

## How to Contribute

### 1. Fork & Clone
- Fork the repository on GitHub.
- Clone your fork locally.
- Create a new branch for your feature or bug fix: `git checkout -b feature/my-awesome-feature`

### 2. Development Setup
We use `pytest` for testing. Set up your environment:
```bash
pip install -r requirements-dev.txt
pip install -e .
```

### 3. Making Changes
- Keep your commits small and focused.
- Write clean, readable code.
- Add tests for any new functionality in the `tests/` directory.

### 4. Running Tests
Ensure all tests pass before submitting a Pull Request:
```bash
pytest tests/
```

### 5. Submit a Pull Request
- Push your changes to your fork.
- Open a Pull Request against the `main` branch.
- Provide a clear description of the changes and link to any relevant issues.

Thank you for your contributions!
