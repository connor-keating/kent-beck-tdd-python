#!/usr/bin/env/ python3
"""Unit tests for money module."""

from tdd import money


def test_multiplication():
    dollar = money.Dollar(amount=5)
    dollar.times(factor=2)
    assert dollar.amount == 10
