# ai-compliance-ui
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
deactivate

Simple Flask app to dynamically load JavaScript snippets. Use the form to add
a script URL and optional attributes such as `data-backend`, `data-stream`,
and `defer`. Added scripts appear in the page head and can be removed from the
list.

## Running

```bash
python app.py
```

