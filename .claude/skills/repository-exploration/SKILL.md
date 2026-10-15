---
name: repository-exploration
description: Explore the SiteMemory repository and plan a task before implementation. Use when starting a new task, investigating unfamiliar code, or deciding what to change.
---

# Repository Exploration and Planning

## Objective

Understand the current state of SiteMemory and produce a grounded,
reviewable plan without prematurely committing to an implementation.

## Procedure

1. Inspect `AGENTS.md`, `README.md`, `pyproject.toml`, and the relevant
   source files. Inspect other files as needed; do not assume the repository
   matches an expected structure.
2. Check `git status` and recent commits. Never overwrite unrelated changes.
3. Restate the task and identify its expected outcome.
4. Separate:
   - facts verified from the repository or sources;
   - assumptions that still need confirmation;
   - unresolved decisions.
5. Identify the smallest useful scope of work.
6. List relevant files that may need changes and explain why.
7. Identify tests, validation commands, risks, and dependencies.
8. For research decisions, compare plausible alternatives and their
   trade-offs. Do not invent novelty claims or fabricate citations.
9. For unclear or high-impact decisions, ask the user instead of guessing.

## Output

Provide:

- Understanding of the task
- Findings from the existing repository
- Assumptions and unresolved questions
- Proposed implementation or investigation plan
- Files likely to change
- Validation plan
- Risks and decisions requiring user approval

## Constraints

- Do not edit files during exploration unless the user explicitly asks.
- Do not install dependencies, start compute jobs, or make external changes.
  Ask first if they are needed.
- Prefer a small, reversible next step over a large speculative implementation.