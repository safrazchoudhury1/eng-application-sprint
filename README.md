# Engineering Application Sprint (Fall 2025)

This repository captures my preparation for university engineering applications. It showcases daily practice in algorithms, contest mathematics, and a small engineering project demonstrating Python proficiency, testing discipline, and tooling.

## Structure
- `coding/` – solved programming problems with notes
- `math/` – contest-style solutions written in Markdown
- `project/` – an engineering demo with multiple logging approaches
- `tests/` – unit tests exercising the project code
- `LOG.md` – daily log with links and progress

## Running Checks
From the repository root run:

```bash
ruff check .
black --check .
mypy .
pytest -q
```

## What this demonstrates
- Clean Python with static typing and linting
- Test-driven fixes and high coverage
- Ability to explain mathematical reasoning clearly
