"""
Purpose: Parse a command from input to list of command name + arguments.
Author: Roei Samuel
Time: 01.07.25
"""

COMMAND_NAME = 0
LAST_COMMAND = -1
EVENT_DESIGNATOR_SIGN = "!"
EVENT_DESIGNATOR_TYPE_LOCATION = 1
EVENT_DESIGNATOR_NUMBER = 2
EVENT_DESIGNATOR_LAST_COMMAND = "!"
EVENT_DESIGNATOR_FROM_END = "-"

def get_event_designator_command(command):
    """
    Return the wanted command location in commands_history for an event designator.
    :param command: Command input from user.
    :return: The location in commands_history list of the wanted command.
    """
    wanted_command = None
    if command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION] == EVENT_DESIGNATOR_LAST_COMMAND:
        wanted_command = LAST_COMMAND
    elif command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION:].isdigit():
        wanted_command = int(command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION:]) - 1
    elif (command[COMMAND_NAME][EVENT_DESIGNATOR_TYPE_LOCATION] == EVENT_DESIGNATOR_FROM_END and
          command[COMMAND_NAME][EVENT_DESIGNATOR_NUMBER:].isdigit()):
        wanted_command = -int(command[COMMAND_NAME][EVENT_DESIGNATOR_NUMBER:])
    return wanted_command

def parse_event_designator(wanted_command, commands_history, command):
    """
    Convert event designator to the wanted command.
    :param wanted_command: Location of wanted command in commands history list.
    :param commands_history: The commands history list.
    :param command: The input command from user.
    :return: The wanted command in a list of the command name + arguments.
    """
    try:
        for i in range(len(commands_history[wanted_command].split())):
            command.insert(i + 1, commands_history[wanted_command].split()[i])
        del command[0]
        print(" ".join(command))
    except (IndexError, TypeError):
        pass
    return command


def convert_command(command, commands_history):
    """
    Convert input from user to command and arguments.
    :param command: The input from the user.
    :param commands_history: History of all commands so far.
    :return: The command seperated to command name and arguments.
    """
    command = command.split()
    if command[COMMAND_NAME].startswith(EVENT_DESIGNATOR_SIGN):
        wanted_command = get_event_designator_command(command)
        command = parse_event_designator(wanted_command, commands_history, command)
    return command