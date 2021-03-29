"""
Author: Geoff Lucas

Date begin: 25 Mar 21

"""

import argparse
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument("dataset", help="path and filename to dataset to analyze")
    parser.add_argument("algorithm", help="ML algorithm you want to run on the data")
    parser.add_argument("-cv", "--cross-validation", type=int, help="number of folds for cross-validation")

    args = parser.parse_args()

    df = pd.read_csv(args.dataset)
    print(df.head())

