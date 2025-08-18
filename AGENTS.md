# Repo Guidelines

## Setup
- Install dependencies: `pip install -r requirements.txt` if available; otherwise `pip install -U black ruff mypy pytest`.

## Checks
Run these before committing code:
- `ruff check .`
- `black --check .`
- `mypy .`
- `pytest -q`

## Notes
- Keep commits focused and well described.
- Prefer small, pure functions with type hints.
