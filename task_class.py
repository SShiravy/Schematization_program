import pandas as pd


class Task:
    def __int__(self, name):
        self.name = name
        self.batch = int
        self.task_resources = pd.DataFrame
        self.subtasks_list = []
        self.total_elapsed_time = None
        self.total_cost = None
        self.total_reliability = None

    def subtask_resource(self, subtask_number):
        return self.task_resources.loc[self.name][subtask_number]

    def all_needed_resources(self):
        all_resources = []
        for st in range(len(self.subtasks_list)):
            all_resources.append(self.subtask_resource(st))

        return all_resources

    def give_subtask_name(self, subtask_number):
        return self.name + '_' + subtask_number
