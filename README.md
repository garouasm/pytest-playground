# pytest-playground

The test-automation spine of my journey into **security-informed safety for autonomous and safety-critical systems**.

This repository grows with every module of my learning plan. It starts small — a tiny calculator with tests — and stays green from day one.

## What's here

- `calculator.py` — a tiny example module.
- `test_calculator.py` — `pytest` tests that verify it.
- Continuous Integration (CI): every push runs the tests automatically on GitHub.

## Run the tests locally

```powershell
# 1. Create and activate a virtual environment
py -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install the tools
pip install -r requirements.txt

# 3. Run the tests
pytest -v
```

## Status

![CI](https://github.com/garouasm/pytest-playground/actions/workflows/ci.yml/badge.svg)

