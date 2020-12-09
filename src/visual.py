import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import numpy as np

def visual(out_dir,input_path,file1,file2,autophrase,multi_word,single_word,token_mapping):
    data_kk_single = pd.read_csv(input_path+file2+single_word, sep="\t",header = None,names=['value', 'phrase'])
    data_single = pd.read_csv(input_path+file1+single_word, sep="\t",header = None,names=['value', 'phrase'])
    data_kk_multi = pd.read_csv(input_path+file2+multi_word, sep="\t",header = None,names=['value', 'phrase'])
    data_multi = pd.read_csv(input_path+file1+multi_word, sep="\t",header = None,names=['value', 'phrase'])
    #single-word distribution
    plt.figure()
    plt.hist(data_kk_single['value'])
    plt.title('result of '+file2+' single value distribution')
    plt.savefig(input_path+ file2+' single_value_distribution'+'.png')
    plt.close()
    #multi-word distribution
    plt.figure()
    plt.hist(data_kk_multi['value'])
    plt.title('result of '+ file2+' multi-words value distribution')
    plt.savefig(input_path+ file2+' multi_value_distribution'+'.png')
    plt.close()

    # DBLP
    plt.figure()
    plt.hist(data_single['value'])
    plt.title('result of '+file1+' single value distribution')
    plt.savefig(input_path+ file1+' single_value_distribution'+'.png')
    plt.close()

    plt.figure()
    plt.hist(data_multi['value'])
    plt.title('result of '+ file1+' multi-words value distribution')
    plt.savefig(input_path+ file1+' multi_value_distribution'+'.png')
    plt.close()

    #randomly pick
    high_quality = data_multi[data_multi['value']>=0.5]
    sample = high_quality.sample(n=100, replace = False).sort_values(by=['value'], ascending=False)
    sample.to_csv(input_path+'sample multi-words.txt', index=None, header = None, sep='\t')

    return
