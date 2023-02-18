#!/usr/bin/env/ python3
"""Unit tests for money module."""

from tdd import money


def test_multiplication():
    """Testing Dollar multiplication function."""
    dollar = money.Dollar(amount=5)
    dollar.times(factor=2)
    assert dollar.amount == 10
    dollar.times(3)
    assert dollar.amount == 15
