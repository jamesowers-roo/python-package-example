"""Tests for the example module"""
import pytest

from python_package_name.example_module import get_sequence


def test_get_sequence():
    for ii in range(10):
        assert len(get_sequence(ii)) == ii

    with pytest.raises(ValueError):
        get_sequence(-1)

    with pytest.raises(ValueError):
        get_sequence(1.1)
