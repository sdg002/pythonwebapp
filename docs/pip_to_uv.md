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
