#  ProcessedTicker.py
#
#  Created by Derek Omuro on 6/9/15.
#  Copyright (c) 2015 domuro. All rights reserved.
#
#  A class representing processed ticker data.

class ProcessedTicker:
    def __init__(self, ticker, current_price, option_type, symbol, strike_price, expiration_date, roundup):
        self.ticker = ticker
        self.current_price = current_price
        self.option_type = option_type
        self.symbol = symbol
        self.strike_price = strike_price
        self.expiration_date = expiration_date
        self.roundup = roundup

    def to_list(self):
        return [self.ticker, self.current_price, self.option_type, self.symbol, self.strike_price, self.expiration_date, self.roundup]
