# nosql_to_sql.py

def nosql_to_sql(nosql_schema):
    sql_tables = []

    for collection, fields in nosql_schema.items():
        columns = []

        for key, value in fields.items():
            if isinstance(value, list):
                # relation détectée
                table_name = key
                sql_tables.append(
                    f"CREATE TABLE {table_name} (id INT, {collection}_id INT);"
                )
            else:
                columns.append(f"{key} TEXT")

        sql_tables.append(
            f"CREATE TABLE {collection} ({', '.join(columns)});"
        )

    return sql_tables
