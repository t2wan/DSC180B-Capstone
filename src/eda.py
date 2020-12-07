import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import numpy as np

def do_eda(out_dir,input_path1,input_path2,file1,file2):
    data_kk = pd.read_csv(input_path2, header=None, names=['sentence'])
    data_kk['length'] = data_kk['sentence'].apply(lambda x: len(str(x).split(' ')))
    #length outlier
    plt.figure()
    plt.hist(data_kk['length'], bins = 100)  
    plt.title(file2+'_outlier')
    plt.savefig(out_dir+ file2+'_outlier'+'.png')
    plt.close()
    #box plot length
    plt.figure()
    sns.boxplot(x=data_kk['length']).set_title('box plot of length sentences '+file2)
    plt.savefig(out_dir+file2+'_boxplot.png')
    plt.close()
    #cleaned
    mean_kk = data_kk['length'].describe()['mean']
    std_kk = data_kk['length'].describe()['std']
    percent_kk = mean_kk+std_kk*3
    cleaned_kk = data_kk[data_kk['length']<percent_kk]
    plt.figure()
    plt.hist(cleaned_kk['length'], bins = 20)  
    plt.title('Cleaned set '+file2)
    plt.savefig(out_dir+file2+' cleaned_set.png')
    plt.close()
    #token
    tokens_kk = data_kk['sentence'].str.split(expand=True).stack().value_counts().to_dict()
    token_arr_kk = list(tokens_kk.values())
    plt.figure()
    plt.hist(list(tokens_kk.values()), bins = 50)
    plt.title('tokens distribution of '+ file2)
    plt.savefig(out_dir+file2+' tokens_distribution.png')
    plt.close()
    
    num_rare_kk = sum(i < 5 for i in token_arr_kk)
    strs_kk = 'Mean for length distribution of '+ file2+ ' is ' + str(mean_kk) + '. Standard deviation is ' + str(std_kk) + '. Number of Rare tokens is ' + str(num_rare_kk) +' .'
    f = open(out_dir+ file2 +" description.txt", "a")
    f.write(strs_kk)
    f.close()

    data = pd.read_csv(input_path1, header=None, names=['sentence'])
    data['length'] = data['sentence'].apply(lambda x: len(str(x).split(' ')))
    #length outlier
    plt.figure()
    plt.hist(data['length'], bins = 100)  
    plt.title(file1+'_outlier')
    plt.savefig(out_dir+ file1+'_outlier'+'.png')
    plt.close()
    #box plot length
    plt.figure()
    sns.boxplot(x=data['length']).set_title('box plot of length sentences '+file1)
    plt.savefig(out_dir+file1+'_boxplot.png')
    plt.close()

    mean = data['length'].describe()['mean']
    std = data['length'].describe()['std']
    percent = mean+std*3
    cleaned = data[data['length']<percent]
    plt.figure()
    plt.hist(cleaned['length'], bins = 20)  
    plt.title('Cleaned set '+file1)
    plt.savefig(out_dir+file1+' cleaned_set.png')
    plt.close()

    prev = 0
    output = Counter({})
    print('Tokenizing..this may take more than 10 mins')
    for i in tqdm((np.arange(10000,2773022,10000).tolist()+[2773022])):
        tokens = data['sentence'][prev:i].str.split(expand=True).stack().value_counts().to_dict()
        output += Counter(tokens)
        prev = i
    
    token_arr = list(output.values())
    num_rare = sum(i < 5 for i in token_arr)

    plt.figure()
    plt.hist(list(output.values()), bins = 80)
    plt.title('tokens distribution of '+ file1)
    plt.savefig(out_dir+file1+' tokens_distribution.png')
    plt.close()

    strs = 'Mean for length distribution is ' + str(mean) + '. Std is ' + str(std) + '. Number of Rare tokens is ' + str(num_rare) +' .'
    f = open(out_dir+ file1 +" description.txt", "a")
    f.write(strs)
    f.close()

    return
