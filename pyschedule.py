import os
import datetime


def get_date_string():
    """Returns the current date as a string."""
    today = datetime.datetime.today()
    return today.strftime('%Y-%m-%d')


def get_day_of_week():
    """Returns the current day of the week as a string."""
    today = datetime.datetime.today()
    return today.strftime('%A')


def get_day_number():
    """Returns the current day of the month as a number."""
    today = datetime.datetime.today()
    return int(today.strftime('%d'))


def _execute_command(command):
    """Executes a command in the shell."""
    os.system(command)


def _gen_command(command, date_string):
    """Generates a command with the date string."""
    return date_string + ' ' + command + '\n'


def _log_command(command, date_string):
    """Create a file that notates that a command has been executed."""
    with open('log.txt', 'ab') as f:
        f.write(_gen_command(command, date_string))


def _check_if_run(command, date_string):
    """Checks if a command has been run already."""
    with open('log.txt', 'rb') as f:
        for line in f:
            if _gen_command(command, date_string) in line:
                return True
    return False


def run_daily(command):
    """Runs a command once a day."""
    date_string = get_date_string()
    if not _check_if_run(command, date_string):
        _execute_command(command)
        _log_command(command, date_string)


def run_weekly(command, day_of_week):
    """Runs a command once a week."""
    if get_day_of_week() == day_of_week:
        date_string = get_date_string()
        if not _check_if_run(command, date_string):
            _execute_command(command)
            _log_command(command, date_string)


def run_monthly(command, day_number):
    """Runs a command once a month."""
    if get_day_number() == day_number:
        date_string = get_date_string()
        if not _check_if_run(command, date_string):
            _execute_command(command)
            _log_command(command, date_string)


if __name__ == '__main__':
    print('get_date_string:', get_date_string())
    print('get_day_of_week:', get_day_of_week())
    print('get_day_number:', get_day_number())
