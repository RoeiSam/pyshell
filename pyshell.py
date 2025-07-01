"""
Purpose: Implementation of shell
Author: Roei Samuel
Date: 01.07.25
"""
from pyshell_commands import ls, cd, pwd, echo, logname, man, history
from typing import List

COMMAND_NAME = 0
FIRST_ARGUMENT = 1
LAST_COMMAND = -1
EVENT_DESIGNATOR_SIGN = "!"
EVENT_DESIGNATOR_TYPE_LOCATION = 1
EVENT_DESIGNATOR_NUMBER = 2
EVENT_DESIGNATOR_LAST_COMMAND = "!"
EVENT_DESIGNATOR_FROM_END = "-"


def convert_command(command: str, commands_history: List[str]) -> str:
    """
    Convert input from user to command and arguments.
    :param command: The input from the user.
    :param commands_history: History of all commands so far.
    :return: The command seperated to command name and arguments.
    """
    command = command.split()
    if command[COMMAND_NAME].startswith(EVENT_DESIGNATOR_SIGN):
        if command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION] == EVENT_DESIGNATOR_LAST_COMMAND:
            wanted_command = LAST_COMMAND
        elif command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION:].isdigit():
            wanted_command = int(command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION:]) - 1
        elif (command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION] == EVENT_DESIGNATOR_FROM_END and
              command[COMMAND_NAME][EVENT_DESIGNATOR_NUMBER:].isdigit()):
            wanted_command = -int(command[COMMAND_NAME][EVENT_DESIGNATOR_NUMBER:])
        try:
            for i in range(len(commands_history[wanted_command].split())):
                command.insert(i + 1, commands_history[wanted_command].split()[i])
            del command[0]
            print(" ".join(command))
        except (IndexError, UnboundLocalError):
            pass
    return command


def pyshell() -> None:
    """
    The pyshell! Get a command from user and execute.
    :return: None
    """
    commands_history = []
    print("Welcome to the Python Shell!")
    while True:
        command = input(f"{logname([])}:{pwd([])} -> ")
        if command:
            command = convert_command(command, commands_history)
            commands_history.append(" ".join(command))
            command.append(commands_history)
            try:
                return_string = eval(f"{command[COMMAND_NAME]}({command[FIRST_ARGUMENT:]})")
                if return_string:
                    print(return_string)
            except (NameError, SyntaxError):
                print("No such command")

def main() -> None:
    pyshell()

if __name__ == "__main__":
    main()
