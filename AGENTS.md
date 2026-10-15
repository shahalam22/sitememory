
# SiteMemory — Agent Instructions

## Project status
SiteMemory is in its initial setup and discovery phase.
The research architecture and algorithms are not yet decided.

## General rules
- Read the README and relevant documentation before making changes.
- Inspect existing code and tests before proposing modifications.
- Do not invent research results, benchmark results, or test results.
- Do not commit secrets, credentials, datasets, or model weights.
- Do not introduce major dependencies without explaining why.
- Do not make unrelated changes.
- Prefer small, reviewable changes over large rewrites.
- Ask for clarification when a decision materially affects
  research direction or system architecture.

## Engineering requirements
- Use the existing Python package under src/sitememory/.
- Use uv for Python dependency management.
- Keep dependencies and uv.lock synchronized.
- Add or update tests when changing behavior.
- Use type annotations for new functions.
- Follow the configured Ruff and mypy rules.
- Keep research experiments reproducible.
- Record significant architecture decisions in docs/decisions/.

## Verification
Before reporting a task as complete:
- Run the relevant tests.
- Run Ruff lint and formatting checks.
- Run mypy on the source package.
- Report which commands actually ran and their results.
- Identify any checks that could not be run.

## Research integrity
- Separate established facts, hypotheses, and assumptions.
- Do not claim novelty before reviewing prior work.
- Do not choose a research method merely because it is easy to implement.
- Compare alternatives against explicit criteria.
- Keep evaluation protocols and results traceable to code and configuration.

## Safety
- Do not expose secrets in code, logs, commits, or outputs.
- Do not run destructive commands without explicit authorization.
- Do not deploy, publish, or incur paid compute costs without approval.