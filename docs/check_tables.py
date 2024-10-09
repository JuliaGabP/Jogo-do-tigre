# docs/check_tables.py
from docs import app, db

with app.app_context():
    print(db.engine.table_names())
