import enum
import os


class QuickType(enum.IntEnum):
    TEXT = 1
    BYTES = 2


def quickload(file: str, type: QuickType) -> str | bytes:
    """Return the contents of a file

    Args:
        file (str): The file to read
        type (QuickloadType): What type to return
        errorTolerance (ErrorTolerance): Amount of error tolerance. Defaults to None

    Returns:
        str | bytes: The contents of the file. Will return "fileNotFound" if the file is not found and errorTolerance is set to FILE_NOT_FOUND
    """

    if not os.path.exists(file):
        raise FileNotFoundError(f"File {file} not found.")

    with open(file, "r" if type == QuickType.TEXT else "rb") as f:
        return f.read()

def quicksave(file: str, data: str | bytes, type: QuickType) -> None:
    """Save data to a file

    Args:
        file (str): The file to write to
        data (str | bytes): The data to write
        type (QuickloadType): What type to write
    """

    with open(file, "w" if type == QuickType.TEXT else "wb") as f:
        f.write(data)
