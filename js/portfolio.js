const Money = require('./money');

class Portfolio {
    constructor() {
        this.moneys = [];
    }

    convert(money, currency) {
        let eurToUsd = 1.2;
        if(money.currency === currency) {
            return money.amount;
        }
        return money.amount * eurToUsd;
    }

    add(...moneys) {
        this.moneys = this.moneys.concat(moneys);
    }

    evaluate(currency) {
        let total = this.moneys.reduce((sum, money) => {
            return sum + this.convert(money, currency);
        }, 0);
        return new Money(total, currency);
    }
}

module.exports = Portfolio