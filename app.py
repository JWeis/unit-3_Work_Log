import os

from create_tasks import Task
from get_tasks import GetTask

# Sets up local variables to use in app
my_log = Task()
emp_log = GetTask()
by_date = emp_log.by_date
by_time = emp_log.by_time_spent
by_exact = emp_log.exact_match
by_pattern = emp_log.pattern_match


def clear():
    # Utility function to clear screen on Linux, MacOS, and Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def end_app():
    # Utility function to ask user to run app again or quit
    choice = input("Run app again or quit? 1: Run Again, 2: Quit  ")
    if choice == '1':
        app()
    else:
        clear()
        quit()


def add_task():
    # Utility function to add a new task to the work_log.csv via Task class
    task_name = input("Task Name:  ")
    task_notes = input("Task Notes: ")
    time_spent = input("Time Spent in Minutes:  ")
    my_log.new_task(task_name.lower(), task_notes.lower(), time_spent)
    clear()
    print("Your new task for has been created!")


def output(task_getter):
    # Utility function to format the output of work logs to terminal
    for log in task_getter:
        log_output = "\nDate: {} \n Task Name: {} \n Task Notes: {} " \
                     "\n Time Spend: {} \n\n".format(log['Date'],
                                                     log['Task Name'],
                                                     log['Task Notes'],
                                                     log['Time Spent'])
        print(log_output)


def app():
    # app logic and user input interface for terminal
    while True:
        clear()
        start = input("Please select what you would like to do: "
                      "1: Add to Work Log, 2: Review Work Log  ")

        if start == '1':
            clear()
            add_task()
            while True:
                again = input("Add another task? 1: Yes, 2: No ")
                if again == '1':
                    clear()
                    add_task()
                else:
                    end_app()

        if start == '2':
            clear()
            first_action = input("Would you like to search your logs by: "
                                 "1: Date, 2: Time Spent, 3: Exact Search, "
                                 "4: Pattern Match  ")

            if first_action == '1':
                print("Here are the available dates of logs to choose from:\n")
                available_dates = emp_log.available_dates()
                for date in available_dates:
                    print(date)

                while True:
                    choice = input("\nWhich date would your like to search by? "
                                   "Please use exact formatting as shown:  ")
                    if choice in available_dates:
                        logs_by_date = by_date(choice)
                        print("\nShowing all logs for {} date".format(choice))
                        output(logs_by_date)
                        end_app()
                    else:
                        print("\nPlease select a date provided. "
                              "Please ensure the format MM/DD/YYYY is used.")

            if first_action == '2':
                clear()
                print("Here are the available times in minutes of logs to choose from:\n")
                available_times = emp_log.av_times()

                for time in available_times:
                    print(time, 'Minutes')

                while True:
                    chosen_time = input("\nWhich time duration you would like to search by:  ")
                    if chosen_time in available_times:
                        logs_by_time = by_time(chosen_time)
                        output(logs_by_time)
                        end_app()
                    else:
                        print("\nPlease select a time provided. "
                              "Please ensure that only numbers are used. i.e '60'.")

            if first_action == '3':
                clear()

                while True:
                    search_query = input("Please enter exact query you would like to search:  ")
                    exact_search = by_exact(search_query.lower())
                    if exact_search:
                        output(exact_search)
                        again = input("\nWould you like to try another Exact Search Query? "
                                      "1: Yes, 2: No ")
                        if again == '1':
                            clear()
                            continue
                        else:
                            end_app()
                    else:
                        print("\nNo logs found for that the query {}".format(search_query))
                        again = input("\nWould you like to try another Exact Search Query? "
                                      "1: Yes, 2: No ")
                        if again == '1':
                            clear()
                            continue
                        else:
                            end_app()

            if first_action == '4':
                clear()

                while True:
                    pattern_query = input("Enter the pattern query you would like to search:  ")
                    pattern_search = by_pattern(pattern_query)
                    if pattern_search:
                        output(pattern_search)
                        again = input("\nWould you like to try another Pattern Search Query? "
                                      "1: Yes, 2: No ")
                        if again == '1':
                            clear()
                            continue
                        else:
                            end_app()
                    else:
                        print("No logs found for that the query {}".format(pattern_query))
                        again = input("\nWould you like to try another Pattern Search Query? "
                                      "1: Yes, 2: No ")
                        if again == '1':
                            clear()
                            continue
                        else:
                            end_app()

            else:
                pass
        else:
            print("Please choose either 1 or 2...")

if __name__ == '__main__':
    app()
