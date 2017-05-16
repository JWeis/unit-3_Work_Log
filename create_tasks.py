import csv
import datetime


class Task:
    def __init__(self):
        """ Initializes a new Task object
        
        Sets fieldnames and set up the DictWriter. writeheader() 
        commented out to not write new header row
        for each new object. 
        """
        self.fieldnames = ['Date', 'Task Name', 'Task Notes', 'Time Spent']
        with open('work_log.csv', 'a') as csvfile:
            self.task_writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            #self.task_writer.writeheader()

    def new_task(self, task_name, task_notes, time_spent):
        """ Creates a new tasks item for Task object

        Writes a new row in the CSV with fieldnames that were initiated
        """
        created_date = datetime.datetime.now().strftime('%m/%d/%Y')
        with open('work_log.csv', 'a') as csvfile:
            self.task_writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            self.task_writer.writerow({
                'Date': created_date,
                'Task Name': task_name,
                'Task Notes': task_notes,
                'Time Spent': time_spent})
