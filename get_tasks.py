import csv
import re


class GetTask:
    def __init__(self):
        """ Initializes a new GetTask object

        Creates a data varible which is created from opening 
        the provided CSV file in read only mode.
        Sets up the DictReader to pull data out of CSV.
        Creates a Rows varible which pulls all rows from CSV into a list
        """
        self.data = open('work_log.csv', 'r')
        self.task_reader = csv.DictReader(self.data, delimiter=',')
        self.rows = list(self.task_reader)

    def available_dates(self):
        """ Gets all dates that have been added to the work log

        Adds all Dates to the output list variable if 
        that date is not already in the list.
        Returns the list object with all the dates to choose from.
        """
        output = []

        for row in self.rows[:]:
            if row['Date'] not in output:
                output.append(row['Date'])
            else:
                continue

        return output

    def by_date(self, date):
        """ Gets all work logs that have been added on a given date

        Adds all work logs are added to the output list variable.
        Returns the list object with all the work log rows.
        """
        output = []

        for row in self.rows[:]:
            check_date = row['Date']
            if check_date == date:
                output.append(row)

        return output

    def av_times(self):
        """ Gets all time spent that have been added to the work log

        Adds all times to the output list variable 
        if that time is not already in the list.
        Returns the list object with all the times to choose from.
        """
        output = []

        for row in self.rows[:]:
            if row['Time Spent'] not in output:
                output.append(row['Time Spent'])
            else:
                continue

        return output

    def by_time_spent(self, time_spent):
        """ Gets all work logs that have been added with a given time spent

        Adds all work logs are added to the output list variable.
        Returns the list object with all the work log rows.
        """
        time_spent = str(time_spent)
        output = []

        for row in self.rows[:]:
            check_time = row['Time Spent']
            if check_time == time_spent:
                output.append(row)

        return output

    def exact_match(self, string):
        """ Gets all work logs that have been added that match a search query

        Adds all work logs that match search query to the output list variable.
        Returns the list object with all the work log rows.
        """
        output = []

        for row in self.rows[:]:
            if string in row['Task Name']:
                output.append(row)
            if string in row['Task Notes']:
                output.append(row)

        return output

    def pattern_match(self, pattern):
        """ Gets all work logs that have been added that match a regex pattern

        Adds all work logs that match regex pattern to the output list variable.
        Returns the list object with all the work log rows.
        """
        output = []

        for row in self.rows[:]:
            task_search = re.search(r'\b' + pattern + r'\b', row['Task Name'], re.I | re.VERBOSE)
            notes_search = re.search(r'\b' + pattern + r'\b', row['Task Notes'], re.I | re.VERBOSE)
            if task_search or notes_search:
                output.append(row)

        return output
