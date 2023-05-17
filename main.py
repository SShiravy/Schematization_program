# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from read_tables import ReadTables
from enterprise_class import Enterprise
from task_class import Task
from resourse_class import Resource

if __name__ == '__main__':
    tables_obj = ReadTables('Tables')
    companies_table, companies_distance_table, subtasks_table, required_resource_table\
        = tables_obj.read_tables()
    # print(companies_table,companies_distance_table,subtasks_table,required_resource_table)

    # TODO: remove index column in tables and replace with second column
    # TODO: create Enterprises and initialize them
    # TODO: create Tasks and Initialize them
