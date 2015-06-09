#  ivysaur.py
#
#  Created by Derek Omuro on 6/9/15.
#  Copyright (c) 2015 domuro. All rights reserved.
#
#  The main script run to process an input file of Ticker and Price data.

import sys
import csv
import TickerGenerator

if len(sys.argv) != 3:
    print "Please specify input and output files.\n\t linux: 'python ivysaur.py input.csv output.csv' \n\t windows: 'ivysaur.py input.csv output.csv'"
    sys.exit()

tg = TickerGenerator.TickerGenerator()

with open(sys.argv[1], 'rb') as in_file:
    with open(sys.argv[2], 'wb') as out_file:
        # write header of output csv
        writer = csv.writer(out_file)
        writer.writerow(['Ticker','Current Price','Option Type','Symbol','Strike Price','Expiration Date','Roundup'])

        # read input csv row by row
        reader = csv.reader(in_file)
        reading_ticker_data = False;
        for row in reader:
            if reading_ticker_data:
                # for each input {ticker, price} generate output.
                ticker = row[0]
                try:
                    price = float(row[1])
                except ValueError:
                    continue

                options = tg.generate_tickers(ticker, price)
                for option in options:
                    writer.writerow(option.to_list());
            else:
                if row[0] == "Ticker":
                    reading_ticker_data = True

print "Finished processing '" + sys.argv[1] + "'. Wrote to file '" + sys.argv[2] + "'"
