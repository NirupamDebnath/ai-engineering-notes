# Serve Docs Locally

Status: Ready

Use MkDocs to preview the documentation site on your machine.

## Start The Server

From the repository root:

```bash
source .venv/bin/activate
mkdocs serve --config-file ai-docs/mkdocs.yml
```

Open the URL printed by MkDocs. By default it is:

```text
http://127.0.0.1:8000/
```

## Alternative Without Activating The Virtualenv

From the repository root:

```bash
.venv/bin/mkdocs serve --config-file ai-docs/mkdocs.yml
```

## Use A Different Port

If port `8000` is already in use:

```bash
.venv/bin/mkdocs serve --config-file ai-docs/mkdocs.yml -a 127.0.0.1:8001
```

Then open:

```text
http://127.0.0.1:8001/
```

## Stop The Server

Press `Ctrl+C` in the terminal where MkDocs is running.

## Verify A Production Build

Before committing larger documentation changes, run:

```bash
.venv/bin/mkdocs build --config-file ai-docs/mkdocs.yml --strict
```
