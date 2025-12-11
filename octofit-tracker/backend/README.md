OctoFit Tracker backend (minimal scaffold)

Setup (from repository root):

```bash
python3 -m venv octofit-tracker/backend/venv
. octofit-tracker/backend/venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r octofit-tracker/backend/requirements.txt
python octofit-tracker/backend/manage.py migrate
python octofit-tracker/backend/manage.py runserver 8000
```

This is an initial scaffold. Configure databases and apps as needed.
