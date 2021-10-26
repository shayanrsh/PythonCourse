from hw1 import Portfolio, Stock, MutualFund

portfolio = Portfolio()
portfolio.addCash(300)
s = Stock(20, "SXP")
portfolio.buyStock(5, s)
mf1 = MutualFund("DOGE")
mf2 = MutualFund("XRP")

portfolio.buyMutualFund(4.4, mf1)
portfolio.buyMutualFund(7, mf2)
portfolio.print()

portfolio.sellMutualFund("DOGE", 1)
portfolio.sellStock("SXP", 4)
portfolio.print()

portfolio.withdrawCash(31)
portfolio.print()

portfolio.history()
portfolio.withdrawCash(200)

