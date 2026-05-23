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
