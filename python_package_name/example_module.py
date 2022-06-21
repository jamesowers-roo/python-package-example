"""This is an example module: a group of related functions for use in scripts etc."""
import numpy as np


def get_sequence(sequence_length: int = 10) -> np.ndarray:
    """Returns a sequence of numbers.

    Args:
        sequence_length: the desired length of the sequence of numbers

    Returns:
        array: the array containing the sequence of numbers
    """
    if not isinstance(sequence_length, int):
        raise ValueError("sequence_length must be an int")
    if sequence_length < 0:
        raise ValueError("sequence_length must be non-negative")
    array = np.arange(sequence_length)
    return array
