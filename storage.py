import json, pathlib

DB_PATH = pathlib.Path("data/db.json")

def load_db():
    if not DB_PATH.exists():
        return {"doctors": [], "patients": [], "appointments": []}
    return json.loads(DB_PATH.read_text())

def save_db(db):
    DB_PATH.write_text(json.dumps(db, indent=2))
