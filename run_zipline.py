import os
from toolz import merge
from zipline import run_algorithm
from zipline.utils.calendars import register_calendar, get_calendar
from strategy import BaseStrategy
from buy_and_hold import BuyAndHold
from os import environ


def run_strategy(strategy_name):
    """ Run strategies here """

    # instantiate a strategy as a mod, change my strategy here:
    mod = None

    if strategy_name == "buy_and_hold":
        mod = BuyAndHold()

    # Here I set the trading calendar for a given exchange
    register_calendar("YAHOO",get_calendar("NYSE"), force=True)

    return run_algorithm(
        initialize=getattr(mod, 'initialize', None),
        handle_data=getattr(mod, 'handle_data',None),
        before_trading_start=getattr(mod,'before_trading_start',None),
        analyze=getattr(mod,'analyze',None),
        bundle='quantopian-quandl',
        environ=environ,
        # allows the default capital base to be overidden by the strategy class
        **merge({'capital_base':1e7},mod._test_args())
    )



def measure_strategy():
    pass
