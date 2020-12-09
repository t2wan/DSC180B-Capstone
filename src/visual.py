import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import numpy as np

def visual(out_dir,input_path,file,autophrase,multi_word,single_word,token_mapping):
    data_kk_single = pd.read_csv(input_path+single_word, sep="\t",header = None,names=['value', 'phrase'])
    data_kk_multi = pd.read_csv(input_path+multi_word, sep="\t",header = None,names=['value', 'phrase'])

    #single-word distribution
    plt.figure()
    plt.hist(data_kk_single['value'])
    plt.title('result of '+file+' single value distribution')
    plt.savefig(input_path+ 'single_value_distribution'+'.png')
    plt.close()
    #multi-word distribution
    plt.figure()
    plt.hist(data_kk_multi['value'])
    plt.title('result of '+ file+' multi-words value distribution')
    plt.savefig(input_path+ 'multi_value_distribution'+'.png')
    plt.close()

    return
