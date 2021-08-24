import pandas as pd
from src import logging

if __name__ == "__main__":
    logging.info('Hello World')
    df = pd.DataFrame()
    df['test'] = [1, 2, 3]
    df.to_csv('test.csv')
