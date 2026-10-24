# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

Uses a plain venv + pip (no uv/poetry). The package is installed in editable mode with dev extras:

```sh
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

## Commands

- Run all tests: `.venv/bin/pytest`
- Run one test: `.venv/bin/pytest tests/test_core.py::test_minimize_scalar_quadratic`
- Lint: `.venv/bin/ruff check .` (auto-fix: `--fix`)
- Format: `.venv/bin/ruff format .`

## Layout

- `src/` layout: the package lives in `src/optimisation/`, tests in `tests/`. Tests import the installed package, so the editable install above is required.
- All config (build, pytest, ruff) is in `pyproject.toml`. Target Python is 3.12+; ruff enforces rules E, F, I, UP, B.
