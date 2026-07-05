# Mermaid Diagrams

Status: Ready

This MkDocs site is configured to render Mermaid diagrams inside Markdown files.

## Configuration

Mermaid support is enabled in `ai-docs/mkdocs.yml` through `pymdownx.superfences`:

```yaml
markdown_extensions:
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
```

## Basic Usage

Use a fenced code block with `mermaid` as the language:

````markdown
```mermaid
flowchart TD
  A[Define goal] --> B[Collect data]
  B --> C[Build baseline]
  C --> D[Evaluate]
  D --> E{Good enough?}
  E -- Yes --> F[Document result]
  E -- No --> B
```
````

Rendered example:

```mermaid
flowchart TD
  A[Define goal] --> B[Collect data]
  B --> C[Build baseline]
  C --> D[Evaluate]
  D --> E{Good enough?}
  E -- Yes --> F[Document result]
  E -- No --> B
```

## Useful Diagram Types

### Flowchart

Use for workflows, learning paths, experiments, and decision trees.

```mermaid
flowchart LR
  Notes[Study notes] --> Notebook[Jupyter notebook]
  Notebook --> Results[Results]
  Results --> Docs[Project documentation]
  Docs --> Progress[Learning progress]
```

### Sequence Diagram

Use for agent workflows, API calls, and multi-system interactions.

```mermaid
sequenceDiagram
  participant User
  participant Agent
  participant Repo
  User->>Agent: Ask for a learning update
  Agent->>Repo: Read learning-progress.md
  Repo-->>Agent: Current status
  Agent-->>User: Summarize progress and next actions
```

### State Diagram

Use for lifecycle notes such as project status or model deployment status.

```mermaid
stateDiagram-v2
  [*] --> Planned
  Planned --> InProgress
  InProgress --> Paused
  InProgress --> Done
  Paused --> InProgress
  Done --> [*]
```

## Verification

Build the docs with strict mode:

```bash
.venv/bin/mkdocs build --config-file ai-docs/mkdocs.yml --strict
```

Run the local docs server when previewing diagrams:

```bash
.venv/bin/mkdocs serve --config-file ai-docs/mkdocs.yml
```

Then open the local URL shown by MkDocs.

## Diagram Guidelines

- Use diagrams when they clarify structure, flow, or relationships.
- Keep node labels short.
- Prefer multiple small diagrams over one crowded diagram.
- Use Mermaid source as the editable truth instead of screenshots.
- Add a short sentence before or after the diagram explaining what it shows.
