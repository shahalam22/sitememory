
# SiteMemory

SiteMemory is an AI-powered visual memory system that helps an autonomous agent remember environments across multiple visits, track objects and their locations, and understand how the environment changes over time.

The project aims to distinguish genuine environmental changes from differences caused by viewpoint, lighting, occlusion, and uncertainty.

> **Status:** Initial setup and research discovery.
> The research method and system architecture are not yet finalized.

## Project goals

- Investigate how visual systems can maintain memory across visits.
- Study persistent object identity and spatial consistency.
- Explore reliable interpretation of environmental changes.
- Evaluate alternative methods using reproducible experiments.
- Deliver an interactive demonstration supported by a maintainable
  software engineering workflow.

## Current status

Repository and development tooling are being established.
Research questions, datasets, methods, and evaluation protocols
will be selected through documented investigation.

## Development setup

Requirements: Git, Python 3.11, and uv.

```bash
git clone https://github.com/YOUR-USERNAME/sitememory.git
cd sitememory
uv sync --all-groups
```

## Quality checks

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src
uv run pytest
```

## Documentation

- `AGENTS.md` — repository instructions for coding agents.
- `docs/decisions/` — significant architecture decisions.
- `docs/` — project and research documentation.

## Research integrity

Research hypotheses are not results. Performance claims will be
supported by documented experiments, baselines, and evaluation.

## License

The project's license has not yet been selected.