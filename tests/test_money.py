#!/usr/bin/env/ python3
"""Unit tests for money module."""

from tdd.money import Dollar


def test_multiplication():
    """Testing Dollar multiplication function."""
    five: Dollar = Dollar(amount=5)
    product: Dollar = five.times(factor=2)
    assert product.amount == 10
    product: Dollar = five.times(factor=3)
    assert product.amount == 15
