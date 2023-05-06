import functools
import operator

from money import Money

class Portfolio:
    def __init__(self):
        self.moneys = []

    def __convert(self, aMoney, aCurrency):
        exchangeRates = {'EUR->USD': 1.2, 'USD->KRW': 1100}

        if aMoney.currency == aCurrency:
            return aMoney.amount
        
        key = aMoney.currency + '->' + aCurrency
        return aMoney.amount * exchangeRates[key]

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, bank, currency):
        total = 0.0
        failures = []
        for m in self.moneys:
            try:
                total += bank.convert(m, currency).amount
            except Exception as ex:
                failures.append(ex)

        if not failures:
            return Money(total, currency)

        failureMessage = failureMessage = ",".join(f.args[0] for f in failures)
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")