import random


class Portfolio(object):
    def __init__(self):
        self.cash = 0.00
        self.stock = {}
        self.mutual_funds = {}
        self.history_rec = '\nYour portfolio is initialized successfully. \n'

    def addCash(self, cash_add):
        self.cash += cash_add
        self.history_rec += '%.2f added to your account successfully. \n' % cash_add

    def buyStock(self, share_price, stock):

        total_price = stock.price * share_price

        if total_price <= self.cash:
            self.cash -= total_price

            if stock.symbol in self.stock.keys():
                total_amount = share_price + self.stock[stock.symbol]
                self.stock[stock.symbol] = total_amount

            else:
                self.stock[stock.symbol] = [share_price]

            self.history_rec += str(int(share_price)) + ' shares of ' + str(stock.symbol) + ' has been successfully ' \
                                                                                            'purchased for $' + str(
                share_price) + '\n'

        else:
            print(' You do NOT have enough utility. \n')

    def buyMutualFund(self, user_share_value, mutual_fund):

        price_to_buy = user_share_value * random.uniform(1, 20)

        if price_to_buy <= self.cash:

            self.cash -= price_to_buy

            if mutual_fund.symbol in self.mutual_funds.keys():

                user_mutual_fund = self.mutual_funds[mutual_fund.symbol][0]
                self.mutual_funds[mutual_fund.symbol] = [user_mutual_fund + float(user_share_value)]

            else:
                self.mutual_funds[mutual_fund.symbol] = [float(user_share_value)]
            self.history_rec += str(float(user_share_value)) + ' shares of ' + str(mutual_fund.symbol) \
                                    + ' has been successfully purchased for $' + str(price_to_buy) + '.\n'

        else:
            print('You do NOT have enough utility. \n')

    def print(self):
        print('Cash: ' + str(self.cash))
        print('Stock: ' + str(self.stock))
        print('Mutual Fund: ' + str(self.mutual_funds))

    def sellMutualFund(self, symbol, user_share_value):

        if self.mutual_funds[symbol][0] != 0 and symbol in self.mutual_funds.keys():

            user_mutual_value = self.mutual_funds[symbol][0]

            if user_mutual_value < user_share_value:

                print(' You do not have utility to sell! \n')

            else:
                user_mutual_value = user_mutual_value - user_share_value
                sell_price = random.uniform(1, 20)

                self.addCash(sell_price * user_share_value)
                self.mutual_funds[symbol] = [user_mutual_value, 1]

            self.history_rec += str(float(user_share_value)) + ' shares of ' + str(symbol) + ' has been successfully ' \
                                                                                             'sold for $' + str(
                sell_price * user_share_value) + '.\n'

        else:
            print('User does NOT have Mutual Funds \n')

    def sellStock(self, symbol, share_price):

        sell_value = random.uniform(1, 20)

        if self.stock[symbol][0] != 0 and symbol in self.stock.keys():

            user_share_value = self.stock[symbol][0]

            if share_price > user_share_value:

                print(' You do not have utility to sell! \n')

            else:

                user_share_value = user_share_value - share_price

                self.stock[symbol] = [user_share_value]
                self.addCash(share_price * sell_value)

                self.history_rec += str(int(share_price)) + ' shares of ' + str(symbol) + ' has been sold for $' + str(
                    sell_value * share_price) + '\n'

        else:

            print(' Warning!!: Please come back with your own portfolio! \n')

    def withdrawCash(self, cash_withdraw):

        if cash_withdraw > self.cash:
            print(' Not enough money in your account! \n')

        else:
            self.cash -= cash_withdraw
            self.history_rec += '%.2f was withdrawn from your account successfully.' % cash_withdraw

    def history(self):
        print(self.history_rec)


class Stock(object):
    price = 0
    symbol = None

    def __init__(self, p, s):
        self.price = p
        self.symbol = s


class MutualFund(object):
    tickerSymbol = None

    def __init__(self, s):
        self.symbol = s
