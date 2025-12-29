from sqlalchemy import text
from database import engine

with engine.connect() as conn:
    conn.execute(text("""
        ALTER TABLE sales_items
        ADD COLUMN MRP float
    """))
    print("✅ Column MRP added successfully")