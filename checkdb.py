from database import engine
from sqlalchemy import text

with engine.connect() as conn:
    # print("\n📌 TABLES IN DATABASE:")
    # tables = conn.execute(
    #     text("SELECT name FROM sqlite_master WHERE type='table'")
    # ).fetchall()

    # for t in tables:
    #     print(" -", t[0])

    # print("\n📌 SUPPLIERS TABLE STRUCTURE:")
    # columns = conn.execute(
    #     text("PRAGMA table_info(suppliers)")
    # ).fetchall()

    # for col in columns:
    #     print(f" - {col[1]} ({col[2]})")



    # tables = conn.execute(
    #     text("SELECT * FROM sales_items ")
    # ).fetchall()

    # for t in tables:
    #     print(" -", t[0],t[1], t[2],t[3], t[4],t[5])

    # tables = conn.execute(
    #     text("SELECT * FROM sales_invoice ")
    # ).fetchall()

    # for t in tables:
    #     print(" -", t[0],t[1], t[2],t[3], t[4],t[5])


    # print("\n📌 SUPPLIERS TABLE STRUCTURE:")
    columns = conn.execute(
       text("PRAGMA table_info(sales_items)")
    ).fetchall()

    for col in columns:
      print(f" - {col[1]} ({col[2]})")