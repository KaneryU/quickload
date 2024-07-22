import pytest
import os
import pathlib
from quickfiles import quickload, quicksave, QuickType


def test_quickload_file_not_found():
    with pytest.raises(FileNotFoundError):
        quickload("nonexistentfile.txt", QuickType.TEXT)


def test_quickload_text_file():

    test_file = pathlib.Path("tmp/testfile.txt")
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    test_file.write_text("")
    
    with open(test_file, "w") as f:
        test_data = "string thread string race condition"
        f.write(test_data)

    test_file.write_text(test_data)


    result = quickload(str(test_file), QuickType.TEXT)

    assert result == test_data


def test_quickload_binary_file():

    test_file = pathlib.Path("tmp/testfile.txt")
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    test_file.write_text("")
    
    with open(test_file, "wb") as f:
        test_data = b"binary binary 2 2"
        f.write(test_data)
    
    test_file.write_bytes(test_data)

    result = quickload(str(test_file), QuickType.BYTES)

    assert result == test_data


def test_quicksave_file_not_found():
    with pytest.raises(FileNotFoundError):
        quicksave("nonexistentfile.txt", "data", QuickType.TEXT)

def test_quicksave_text_file():
    test_file = pathlib.Path("tmp/testfile.txt")
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    test_file.write_text("")

    test_data = "string thread string"
    quicksave(str(test_file), test_data, QuickType.TEXT)
    
    assert test_file.read_text() == test_data
    
def test_quicksave_binary_file():
    test_file = pathlib.Path("tmp/testfile.txt")
    os.makedirs(os.path.dirname(test_file), exist_ok=True)
    test_file.write_text("")

    test_data = b"binary binary 2 2"
    quicksave(str(test_file), test_data, QuickType.BYTES)
    
    assert test_file.read_bytes() == test_data