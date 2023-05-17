import pandas as pd


class Enterprise:
    def __int__(self, name):
        self.name = name
        self.resources_list = []
        self.position_matrix = pd.DataFrame
        self.tasks_list = []

    def distance_from(self, other_enterprise):
        return self.position_matrix.loc[self.name][other_enterprise]

    def perform_task(self,task):
        """
        perform given task using proper manufacturing resource
        :return: Cost, elapsed_time , Reliability
        """
        pass

    def __perform_all_tasks(self):
        """
        we will use this method if all subtasks in tasks_list have same pre task name
        :return: total of cost, elapsed_time and reliability
        """
        total_cost, total_elapsed_time, total_reliability = 0,0,0
        for task in self.tasks_list:
            cost, elapsed_time , reliability = self.perform_task(task)
            total_cost += cost
            total_elapsed_time += elapsed_time
            total_reliability += reliability

    def start(self):
        """
        perform tasks with proper method
        :return: dictionary of subtasks and their total of cost, elapsed_time and reliability
        """
        # TODO: define conditions to specify which method should be used
        pass

