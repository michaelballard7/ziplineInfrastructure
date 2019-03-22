import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from run_zipline import run_strategy


def main():
    print ("Algo is running")
    perf = run_strategy('buy_and_hold') # insert strategy file name here
    perf.to_csv("bnh_performance.csv") # insert name of output here


if __name__ == '__main__':
    main()
