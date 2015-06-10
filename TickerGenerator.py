#  TickerGenerator.py
#
#  Created by Derek Omuro on 6/9/15.
#  Copyright (c) 2015 domuro. All rights reserved.
#
#  A class to generate ProcessedTicker objects based on provided parameters.

import math
from datetime import date
import ProcessedTicker

class TickerGenerator:
    def __init__(self):
        # options are be listed for +/- 30% of base strike price.
        self.strike_range = 0.3

        # strike prices are incremented based on roundup price.
        self.increment_rules_keys = [20, 60, 140, 290, 100000]
        self.increment_rules = {20: 0.5, 60: 1.0, 140: 2.5, 290: 5.0, 100000: 10}

    # returns a list of third fridays of the month.
    def generate_dates(self, number_of_months):
        today = date.today()
        fridays = []

        for i in range(number_of_months):
            first = date(today.year, today.month+i, 1)
            weekday = first.weekday()
            friday = date(today.year, today.month+i, 1+(4-weekday)%7+14);
            fridays.append(friday)

        return fridays

    # returns a symbol
    def generate_symbol(self, ticker, current_price, option_type, strike_price, expiration_date):
        return ticker + expiration_date.strftime('%y%m%d') + option_type[0] + '%08d' % (strike_price*1000)

    # returns a list of generated ProcessedTickers.
    def generate_tickers(self, ticker, current_price):
        # option types
        option_types = ['CAL', 'PUT']

        # round up to nearest 10
        roundup = (current_price + 9.999) // 10 * 10

        # determine increment based on roundup
        for key in self.increment_rules_keys:
            if roundup <= key:
                break
        increment = self.increment_rules[key];

        # lowest strike price
        strike_price = current_price * (1-self.strike_range) // increment * increment

        # list of five third fridays of the month
        expiration_dates = self.generate_dates(5)

        # Create ProcessedTickers.
        processed_tickers = [];
        for exp_date in expiration_dates:
            for option_type in option_types:
                c_strike_price = strike_price
                while c_strike_price < current_price * (1+self.strike_range):
                    symbol = self.generate_symbol(ticker, current_price, option_type, c_strike_price, exp_date)
                    processed_tickers.append(ProcessedTicker.ProcessedTicker(ticker, current_price, option_type, symbol, c_strike_price, exp_date, roundup))
                    c_strike_price += increment;

        return processed_tickers
