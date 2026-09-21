# ai-engineering-notes

Personal AI engineering learning workspace for notes, setup guides, Jupyter notebooks, and project documentation.

## Initial Setup

Requirements: Python 3 and GNU Make.

From the repository root, create the virtual environment and install MkDocs, JupyterLab, and the machine-learning libraries:

```bash
make setup
```

This installs `mkdocs`, `mkdocs-material`, `jupyterlab`, `numpy`, `pandas`, `matplotlib`, and `scikit-learn` into `.venv/`.

To see every available command:

```bash
make help
```

## Notebooks

Keep unsolved exercises in `notebooks/exercises/` and your completed solutions in `notebooks/solutions/`. Start JupyterLab with:

```bash
make notebook
```

The first guided exercise is `notebooks/exercises/002-linear-regression-baseline.ipynb`.

## Serve docs locally

From the repository root:

```bash
make serve-docs
```

Then open the local URL shown by MkDocs, usually `http://127.0.0.1:8000/`.

To generate the static site without starting a server:

```bash
make build-docs
```

## Assistant Workflow

- Start with `AGENTS.md` for repository-specific assistant instructions.
- Use `ai-docs/docs/progress/learning-progress.md` as the durable learning status file.
- Update the progress file whenever new topics, notebooks, projects, or priorities are added.
