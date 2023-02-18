#!/usr/bin/env/ python3
"""Money module."""


class Dollar:
    """Class containing the properties & behavior of a US dollar."""

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def times(self, factor: int) -> "Dollar":
        """Multiply the dollar amount by the given factor."""
        return Dollar(self.amount * factor)
