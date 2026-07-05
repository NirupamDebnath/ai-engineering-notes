# AI Engineering Notes Agent Guide

This repository is a personal AI engineering learning workspace. The assistant should help organize notes, notebooks, experiments, and project writeups while preserving the learner's voice and progress history.

## First File To Read

Before scanning the whole repository, read:

- `ai-docs/docs/progress/learning-progress.md`

Use that file as the quick state document for current topics, completed work, active questions, and next actions. Update it whenever meaningful learning progress, new notebooks, new projects, or changed priorities are added.

## Repository Shape

- `ai-docs/`: MkDocs documentation site.
- `ai-docs/docs/`: Markdown source files.
- `ai-docs/docs/setup/`: Environment, tooling, and installation notes.
- `ai-docs/docs/ml/`: Machine learning foundations.
- `ai-docs/docs/system-design/`: AI system design and architecture notes.
- `ai-docs/docs/notebooks/`: Notebook index and summaries.
- `ai-docs/docs/projects/`: Project notes, experiments, and implementation logs.
- `mindmaps/`: Source mind-map files, such as `.minder` planning documents.

## Assistant Responsibilities

- Keep documentation organized into clear topic folders.
- Store `.minder` files in `mindmaps/` and reference them from the related documentation page.
- Prefer small, well-named Markdown files over one large catch-all note.
- Add or update navigation in `ai-docs/mkdocs.yml` when new public docs pages are created.
- Keep `learning-progress.md` current so future sessions do not need to re-read the entire repo.
- When reviewing notebooks, summarize purpose, key learnings, dependencies, results, and follow-up tasks.
- When adding study notes, include concise examples, practical commands, and links to related local pages when useful.
- Feel free to use Mermaid diagrams when they make workflows, architectures, data flow, model pipelines, or decision trees easier to understand.
- Do not rewrite personal notes aggressively unless asked. Improve structure, clarity, typos, and consistency while preserving intent.

## Documentation Style

- Use descriptive headings and short sections.
- Prefer practical examples and reproducible steps.
- Use fenced code blocks with language tags.
- Use Mermaid fenced blocks with `mermaid` for diagrams. Keep diagrams readable and split large diagrams into smaller ones when needed.
- Capture open questions explicitly.
- Mark work status clearly: `Planned`, `In progress`, `Paused`, `Done`.

## Suggested Workflow

1. Read `ai-docs/docs/progress/learning-progress.md`.
2. Inspect only the files relevant to the user's current request.
3. Make focused updates.
4. Update `learning-progress.md` with any durable progress or next step.
5. If docs navigation changed, verify `ai-docs/mkdocs.yml`.
