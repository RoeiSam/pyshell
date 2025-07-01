"""
Purpose: Implementation of shell
Author: Roei Samuel
Date: 01.07.25
"""
from pyshell_commands import ls, cd, pwd, echo, logname, man, history
from parse_command import convert_command
from files_commands import touch, cat, cp

COMMAND_NAME = 0
FIRST_ARGUMENT = 1


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
