# Learning Progress

This is the quick-orientation file for the AI engineering learning journey. Update it whenever new learning work, notebooks, projects, or priorities are added.

## Current Status

- Overall status: In progress
- Primary workspace: MkDocs documentation in `ai-docs/`
- Current focus: CS229 machine learning foundations through Lecture 3, with notes and practice in progress
- Last updated: 2026-09-21

## Learning Goals

- Build strong foundations in machine learning and AI engineering.
- Document setup steps, tools, and reproducible workflows.
- Create and summarize Jupyter notebooks for hands-on learning.
- Build practical AI engineering projects with clear implementation notes.
- Track open questions, decisions, and next actions in one place.

## Topic Map

| Area | Status | Location | Notes |
| --- | --- | --- | --- |
| Repository setup | Done | `README.md`, `Makefile`, `requirements.txt`, `ai-docs/docs/setup/` | A Makefile now creates `.venv` and installs all documentation and notebook dependencies from the root requirements file. |
| Local docs preview | Done | `README.md`, `ai-docs/docs/setup/serve-docs-locally.md` | MkDocs serve commands documented. |
| Mermaid diagrams | Done | `ai-docs/docs/setup/mermaid-diagrams.md` | Mermaid usage documented and available for architecture/workflow diagrams. |
| Git and SSH setup | Done | `ai-docs/docs/setup/git-ssh-authentication.md` | GitHub SSH guide added. |
| OpenClaw setup | In progress | `ai-docs/docs/setup/opencalaw-installation-in-vm.md` | Mind-map checklist added for install, security, SSH tunnel, agent rules, and cost optimization. |
| ML basics | In progress | `ai-docs/docs/ml/basics.md` | Foundations section started. |
| Linear regression | Done | `ai-docs/docs/ml/linear-regression.md` | Added CS229 Lecture 2 notes, math derivation, gradient descent, normal equation, probabilistic interpretation, locally weighted regression, and practical Python implementation. |
| CS229 Lecture 3 | Watched | _Notes pending_ | Lecture watched; capture the concepts and add practice work next. |
| AI system design | Planned | `ai-docs/docs/system-design/ai-systems.md` | Placeholder created for architecture notes. |
| Jupyter notebooks | In progress | `notebooks/exercises/`, `notebooks/solutions/`, `ai-docs/docs/notebooks/index.md` | Exercises and completed solutions are separated; the first guided linear regression notebook is ready to complete. |
| Projects | Planned | `ai-docs/docs/projects/index.md` | Project index created; add one page per project or experiment. |

## Active Work

- Continue CS229 machine learning foundations notes.
- Organize the repository so future learning notes, notebooks, and projects have predictable locations.
- Keep this progress file updated as the main assistant handoff document.

## Recently Completed

- Created an assistant guide in `AGENTS.md`.
- Added a persistent learning progress tracker.
- Added starter documentation sections for ML basics, AI system design, notebooks, and projects.
- Expanded the OpenClaw installation page using the `mindmaps/Openclaw.minder` mind map.
- Added Mermaid diagram setup documentation and agent guidance for diagram usage.
- Added local MkDocs serving instructions.
- Added CS229 Lecture 2 linear regression documentation with math and practical Python implementation.
- Enabled MathJax rendering for equation-heavy notes.
- Expanded the linear regression gradient descent section with a partial derivative breakdown.
- Added a numeric house-price example showing how training examples fit into the gradient formula.
- Reworked the linear regression code section around common NumPy and scikit-learn implementations.
- Documented a by-hand batch gradient descent implementation that maps Python code to the update rule.
- Created separate `notebooks/exercises/` and `notebooks/solutions/` folders, with a guided linear regression exercise in Exercises.
- Added Makefile commands for full environment setup, local docs preview, docs builds, and JupyterLab.
- Consolidated documentation and machine-learning dependencies in the root `requirements.txt`.
- Watched CS229 Lecture 3; notes and exercises are still to be captured.

## Next Actions

- Verify exact OpenClaw configuration keys for heartbeat, caching, and token limits.
- Add OpenClaw prerequisites, environment details, and validation steps after the setup is tested.
- Complete `notebooks/exercises/002-linear-regression-baseline.ipynb` step by step, then save the finished version in `notebooks/solutions/`.
- Add a short model evaluation note covering train/test splits, leakage, MAE, RMSE, and R-squared.
- Capture CS229 Lecture 3 notes, then continue with the next lecture or a related classification exercise.

## Open Questions

- Which dataset should be used for a hands-on linear regression notebook?
- Should notebooks be stored directly in the repo, exported into docs, or both?
- Will this documentation be published publicly, or kept as a private learning workspace?

## Notebook Log

| Notebook | Status | Summary | Follow-up |
| --- | --- | --- | --- |
| `exercises/002-linear-regression-baseline.ipynb` | In progress | Guided linear regression baseline on the diabetes dataset. | Complete the exercise, then save the solved version in `solutions/` and document results. |

## Project Log

| Project | Status | Summary | Follow-up |
| --- | --- | --- | --- |
| _None yet_ | Planned | Add project entries here as projects are created. | Choose first project. |
