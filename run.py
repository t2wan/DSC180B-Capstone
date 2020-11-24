import sys
import os
import json
import requests
import gzip
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import numpy as np
sys.path.insert(0, 'src')
from etl import get_data
from eda import do_eda
from auto import autophrase
from test import test
def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''

    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        get_data(**data_cfg)
    

    if 'eda' in targets:
        with open('config/eda-params.json') as fh:
            eda_cfg = json.load(fh)
        do_eda(**eda_cfg)


    if 'auto' in targets:
        with open('config/auto-params.json') as fh:
            auto_cfg = json.load(fh)
        autophrase(**auto_cfg)

    if 'test' in targets:
        with open('config/test-params.json') as fh:
            test_cfg = json.load(fh)
        test(**test_cfg)
   

    return
if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
