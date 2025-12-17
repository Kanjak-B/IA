# main.py

from models import Table, ForeignKey
from sql_to_nosql import sql_to_nosql
from nosql_to_sql import nosql_to_sql

# -------------------------
# Exemple SQL
# -------------------------
users = Table(
    name="users",
    columns=["id", "name", "email"]
)

orders = Table(
    name="orders",
    columns=["id", "user_id", "total"],
    foreign_keys=[ForeignKey("user_id", "users")]
)

tables = [users, orders]

# -------------------------
# SQL → NoSQL
# -------------------------
nosql = sql_to_nosql(tables)

print("=== NoSQL Schema ===")
for k, v in nosql.items():
    print(k, "=>", v)

# -------------------------
# NoSQL → SQL
# -------------------------
sql = nosql_to_sql(nosql)

print("\n=== SQL Generated ===")
for stmt in sql:
    print(stmt)
