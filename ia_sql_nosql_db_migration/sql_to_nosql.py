# sql_to_nosql.py

from models import Table, ForeignKey

def decide_relation():
    """
    Règle simple :
    - relation forte → embed
    """
    return "embed"


def sql_to_nosql(tables):
    nosql_schema = {}

    for table in tables:
        if not table.foreign_keys:
            nosql_schema[table.name] = {
                "_id": "ObjectId",
                **{col: "value" for col in table.columns if col != "id"}
            }

    for table in tables:
        for fk in table.foreign_keys:
            decision = decide_relation()

            if decision == "embed":
                parent = fk.ref_table
                if parent in nosql_schema:
                    nosql_schema[parent].setdefault(table.name, [])
                    nosql_schema[parent][table.name].append(
                        {col: "value" for col in table.columns if col != fk.column}
                    )

    return nosql_schema
