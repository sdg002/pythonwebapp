[[_TOC_]]

Read [](file:///c%3A/Users/saurabhd/MyTrials/Python/pythonwebapp/requirements.txt)

Here are the steps to migrate this project from pip to **uv**:

---

# 1. Install uv

```powershell
pip install uv
# or via the official installer:
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

# 2. Initialize a uv project (creates `pyproject.toml`)

```powershell
cd C:\Users\saurabhd\MyTrials\Python\pythonwebapp
uv init --no-workspace
```

This creates `pyproject.toml`. If one already exists, skip this step.

---

# 3. Import dependencies from requirements.txt

```powershell
uv add $(Get-Content requirements.txt | Where-Object { $_ -notmatch '^\s*#' -and $_ -ne '' } | ForEach-Object { $_.Trim() })
```

Or add them manually one by one:

```powershell
uv add flask==3.0.3 dash==3.0.1 pandas plotly==6.0.1 Flask-Caching==2.3.1 dash-bootstrap-components==2.0.0 arrr
```

uv will:

- Create a virtual environment in .venv
- Generate a `uv.lock` lockfile (replaces requirements.txt for reproducibility)

---

# 4. Verify the environment

```powershell
uv run python -c "import flask, dash; print('OK')"
```

---

# 5. Replace common pip workflows

| Old (pip)                         | New (uv)                                            |
| --------------------------------- | --------------------------------------------------- |
| `pip install -r requirements.txt` | `uv sync`                                           |
| `pip install <pkg>`               | `uv add <pkg>`                                      |
| `pip uninstall <pkg>`             | `uv remove <pkg>`                                   |
| `python app.py`                   | `uv run python app.py`                              |
| `pip freeze > requirements.txt`   | `uv export -o requirements.txt` (for compatibility) |

---

# 6. Update .gitignore

Add .venv if not already present, and commit `pyproject.toml` and `uv.lock` instead of requirements.txt.

---

**Note:** You can keep requirements.txt alongside for CI/CD compatibility using `uv export -o requirements.txt --no-hashes`.

---

# What was the outcome ?

1. Created a file `.python-version`
1. Create a file `pyproject.toml`
1. Added dependencies. This produced a `uv.lock` file
1. Adding pytest `uv add --dev pytest`

## Configure logging of pytests

This has to be added manuall

```
[tool.pytest.ini_options]
log_cli = true
log_cli_level = "INFO"
```

## How to run the pytests ?

`uv run pytest` ensures pytest runs inside the uv-managed .venv, using the exact interpreter and packages resolved by uv. Without it, `pytest` would resolve to whatever is on the agent's `PATH`, which may be a different version or missing your project's dependencies entirely.

That said, you **can** use `uv run pytest tests/` to scope it to the tests directory — that's perfectly fine. The key part is the `uv run` prefix, not the directory argument.

In CI, the safer habit is always `uv run <command>` rather than activating the venv manually and relying on `PATH`.

## How to deploy to Azure Web App when using uv ?

Read [](file:///c%3A/Users/saurabhd/MyTrials/Python/pythonwebapp/.azuredevops/deploy.ps1#1-1), lines 1 to 60

Azure App Service's Oryx build system doesn't natively support uv, so the approach is: **generate a locked requirements.txt from uv.lock using `uv export`, then let Oryx use that** — instead of copying the manually-maintained root requirements.txt.

Changes needed in deploy.ps1:

1. Install uv on the deploy agent
2. Replace the `Copy-Item requirements.txt` block with `uv export --no-dev`

Replacing 8 lines with 11 lines in [](file:///c%3A/Users/saurabhd/MyTrials/Python/pythonwebapp/.azuredevops/deploy.ps1)

```

```

**What changed and why:**

| Before                                             | After                                                 |
| -------------------------------------------------- | ----------------------------------------------------- |
| Copied root requirements.txt (manually maintained) | Runs `uv export --no-dev` to generate it from uv.lock |
| No guarantee versions were locked                  | Versions are pinned exactly as resolved by uv         |
| Dev dependencies could accidentally slip in        | `--no-dev` excludes pytest and other dev tools        |

`--no-hashes` is used because Azure's Oryx pip install doesn't support hash-pinned requirements. Oryx still reads the generated requirements.txt from the src folder and installs it as before.

---

# Why do we need the file .python-version ?

Response from copilot below:

Good question. With uv, `requires-python = ">=3.12"` in pyproject.toml sets a **minimum version constraint** — it tells uv "any Python 3.12 or higher is acceptable", but it doesn't pin an exact version.

.python-version tells uv **exactly which version to use** when creating the venv (e.g., `3.12.9` vs `3.13.1`).

**In practice with uv:**

- If you have `requires-python = ">=3.12"` and no .python-version, uv picks whatever Python it finds that satisfies the constraint — which could vary between machines and CI agents.
- If you add `.python-version = 3.12`, uv will always use Python 3.12.x specifically.

**For this project, you likely don't need it** because:

- Your `requires-python = ">=3.12"` already constrains the version
- Your CI explicitly installs Python 3.12 via `UsePythonVersion@0`
- uv will use that installed Python automatically in CI

.python-version adds value mainly when developers have multiple Python versions installed locally (via pyenv/asdf) and you want to enforce exact version consistency across the team.

---
