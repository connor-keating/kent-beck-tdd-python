#!/usr/bin/env/ python3
"""Unit tests for money module."""

from tdd.money import Dollar


def test_multiplication():
    """Testing Dollar multiplication function."""
    dollar = Dollar(amount=5)
    dollar.times(factor=2)
    assert dollar.amount == 10
