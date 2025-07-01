"""
Purpose: Implement files related pyshell commands.
Author: Roei Samuel
Time: 01.07.25
"""
from pathlib import Path
from typing import List

HISTORY_LOCATION = -1


def touch(arguments: List[str]) -> None:
    """
    Create new file.
    Usage: touch [filename]...
    """
    if len(arguments) <= 1:
        print("touch: missing file operand")
    else:
        for file in arguments[:HISTORY_LOCATION]:
            try:
                Path.touch(file)
            except NotADirectoryError:
                print(f"touch: cannot touch '{file}': No such file or directory")
