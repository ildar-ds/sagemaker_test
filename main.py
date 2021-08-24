import pandas as pd

if __name__ == "__main__":
    df = pd.DataFrame()
    df['test'] = [1, 2, 3]
    df.to_csv('test.csv')
