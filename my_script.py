import pandas as pd
import numpy as np
import random
from sys import argv
from ppt import PPT_Creator as PPT
OUTPUT_DIR = './log/'


def main(n, *args):
    n = n or 1
    filename = OUTPUT_DIR + 'frame_{0}.csv'
    ppt = PPT()
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
        ppt.add_frame(frame)
        print(f'Added frame {n} to PPT_Creator')
    pres = ppt.create()
    pres_path = OUTPUT_DIR + 'presentation.pptx'
    pres.save(pres_path)
    print(f'Exported to {pres_path}') 


if __name__ == "__main__":
    try:
        n = input('how many data frames would you like to print?\n')
        n = int(n)
        print(f'Docker is running in interactive mode')
    except EOFError:
        print(f'Docker is NOT running in interactive mode')
        n = random.choice(range(1,11))
    print(f'The application will create {n} dataframe(s)')
    main(n, argv)