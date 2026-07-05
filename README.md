# ai-engineering-notes

Personal AI engineering learning workspace for notes, setup guides, Jupyter notebooks, and project documentation.

## Assistant workflow

- Start with `AGENTS.md` for repository-specific assistant instructions.
- Use `ai-docs/docs/progress/learning-progress.md` as the durable learning status file.
- Update the progress file whenever new topics, notebooks, projects, or priorities are added.

Initial Repo Setup Commands:
```
python3 -m venv .venv
source .venv/bin/activate
pip install mkdocs mkdocs-material
mkdocs new ai-docs
cd ai-docs
pip install jupyterlab
```

## Serve docs locally

From the repository root:

```bash
source .venv/bin/activate
mkdocs serve --config-file ai-docs/mkdocs.yml
```

Then open the local URL shown by MkDocs, usually `http://127.0.0.1:8000/`.
