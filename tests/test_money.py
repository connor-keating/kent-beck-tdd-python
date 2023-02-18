#!/usr/bin/env/ python3
"""Unit tests for money module."""

from tdd.money import Dollar


def test_multiplication():
    """Testing Dollar multiplication function."""
    five: Dollar = Dollar(amount=5)
    five.times(factor=2)
    assert five.amount == 10
    five.times(3)
    assert five.amount == 15
