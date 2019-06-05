import os
from unittest import TestCase

import pandas

from WarbleContext import settings
from WarbleContext.preprocess.hh101 import HH101PreProcessor


class TestHH101PreProcessor(TestCase):
    def test_1(self):
        v = {'c_inc': ['date']}
        r_hh101 = pandas.read_csv(os.path.join(settings.RAW_OUTPUT_PATH, 'hh101', 'hh101', 'rawdata.txt'))

        HH101PreProcessor(v=v).execute()

        act_p_hh101 = pandas.read_csv(os.path
                                      .join(settings.PROCESSED_OUTPUT_PATH, 'hh101.pre.dat'), sep=',')
        for col_name in r_hh101.columns:
            if col_name == 'date':
                self.assertTrue(col_name in act_p_hh101.columns)
            else:
                self.assertFalse(col_name in act_p_hh101.columns)

    def test_2(self):
        v = {'c_exc': ['date', 'time']}

