import os

import pandas
import shutil

from WarbleContext import settings


class PreProcessor:
    def execute(self):
        raise NotImplementedError


class HH101PreProcessor(PreProcessor):
    def __init__(self, raw_fp=None, processed_fp=None, v=None):
        self.raw_fp = os.path.join(settings.RAW_OUTPUT_PATH, 'hh101', 'hh101', 'rawdata.txt') if raw_fp is None else raw_fp
        self.processed_fp = os.path.join(settings.PROCESSED_OUTPUT_PATH, 'hh101.pre.dat') if processed_fp is None else processed_fp
        self.v = dict() if v is None else v

    def execute(self):
        print('Copying raw to processed ...')
        shutil.copy2(self.raw_fp, self.processed_fp)

        print('Adding column names ...')
        with open(self.processed_fp, 'r') as file:
            content = file.read()
        with open(self.processed_fp, 'w') as file:
            file.write(' '.join(['date', 'time', 'thing', 'data']) + '\n')
            file.write(content)

        print('Filtering ...')
        df = pandas.read_csv(self.processed_fp, sep=' ')
        if 'c_inc' in self.v:
            df = df[self.v['c_inc']]
        else:
            pass

        df.to_csv(self.processed_fp, index=False)


if __name__ == '__main__':
    hh101_pp = HH101PreProcessor(v={
        'c_inc': ['date'],
    })
    hh101_pp.execute()
