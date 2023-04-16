import unittest

class Money:
    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency

    def __eq__(self, other: object) -> bool:
        return self.amount == other.amount and self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

import functools
import operator

class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, currency):
        total = functools.reduce(operator.add, 
                                 map(lambda m: m.amount, self.moneys), 
                                 0)
        return Money(total, currency)

class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        fiver = Money(5, "USD")
        tenner = Money(10, "USD")
        self.assertEqual(tenner, fiver.times(2))

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision,
                        originalMoney.divide(4))

if __name__ == '__main__':
    unittest.main()