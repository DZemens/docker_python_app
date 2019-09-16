import pandas as pd
import numpy as np
import random
from sys import argv

OUTPUT_DIR = './log/'

def main(n, *args):
    n = n or 1
    filename = OUTPUT_DIR + 'frame_{0}.csv'
    for i in range(n):
        data = np.array(np.random.randint(0,100,(3,4)))
        columns = ['A','B','C','D']
        index = ['Row 1', 'Row 2', 'Row 3']
        frame = pd.DataFrame(data, index=index, columns=columns, dtype=int)
        out = filename.format(i+1)
        try:
            frame.to_csv(out)
            print(f'frame exported as {out}')
        except OSError as e:
            print(f'OSError writing to {out}, this file will not be produced!')


if __name__ == "__main__":
    try:
        n = input('how many data frames would you like to print?\n')
        n = int(n)
        print(f'Docker is running in interactive mode')
    except EOFError:
        n = random.choice(range(10))
    print(f'The application will create {n} dataframe(s)')
    main(n, argv)