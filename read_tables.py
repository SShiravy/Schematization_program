import pandas as pd


class ReadTables:
    def __init__(self,tables_dir):
        self.tables_dir = tables_dir
        self.companies = None
        self.companies_distance = None
        self.subtasks = None
        self.required_resource = None

    def read_tables(self):
        self.companies = pd.read_excel(self.tables_dir+'/'+'table_1.xlsx')
        self.companies_distance = pd.read_excel(self.tables_dir + '/' + 'table_2.xlsx')
        self.subtasks = pd.read_excel(self.tables_dir + '/' + 'table_3.xlsx')
        self.required_resource = pd.read_excel(self.tables_dir + '/' + 'table_4.xlsx')

        return self.companies, self.companies_distance, self.subtasks, self.required_resource,

