# Notebook Index

Status: In progress

Use this page to track Jupyter notebooks and their learning value.

## Notebook Summary Template

| Field | Notes |
| --- | --- |
| Purpose | What question or concept does the notebook explore? |
| Inputs | Datasets, APIs, files, or generated data used. |
| Key steps | Main workflow or experiment stages. |
| Results | Metrics, observations, or outputs. |
| Lessons | What was learned. |
| Follow-up | What to improve, repeat, or study next. |

## Notebooks

| Notebook | Status | Topic | Summary |
| --- | --- | --- | --- |
| `notebooks/solutions/002-linear-regression-baseline.ipynb` | Done | Linear regression | Baseline experiment using scikit-learn's diabetes dataset, including data inspection, metrics, coefficients, residuals, and a single-feature comparison. |
| `notebooks/exercises/003-logistic-regression-classification.ipynb` | Planned | Logistic regression | Guided classification exercise using scikit-learn's breast-cancer dataset, with questions on stratified splits, baselines, probabilities, confusion matrices, and thresholds. |

## Storage Location

Keep unsolved exercises in `notebooks/exercises/` and completed solutions in `notebooks/solutions/`. Keep their summaries and learning notes in this documentation section.

Install notebook dependencies from the repository root before starting JupyterLab:

```bash
pip install -r requirements.txt
```

## Suggested Naming

Use names that sort naturally and describe the topic:

```text
001-train-test-split.ipynb
002-linear-regression-baseline.ipynb
003-logistic-regression-classification.ipynb
```
