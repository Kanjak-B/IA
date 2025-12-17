# models.py

class ForeignKey:
    def __init__(self, column, ref_table):
        self.column = column
        self.ref_table = ref_table


class Table:
    def __init__(self, name, columns, foreign_keys=None):
        self.name = name
        self.columns = columns
        self.foreign_keys = foreign_keys or []
