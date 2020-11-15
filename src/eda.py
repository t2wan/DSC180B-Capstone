import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import numpy as np

def do_eda(out_dir):
    data = pd.read_csv('data/raw/DBLP.csv')
    data['length'] = data['sentence'].apply(lambda x: len(str(x).split(' ')))
    #length outlier
    plt.hist(data['length'], bins = 100)  
    plt.title('DBLP set')
    plt.savefig(out_dir+'/outlier.png')

    sns.boxplot(x=data['length']).set_title('box plot of length of sentences')
    plt.savefig(out_dir+'/boxplot.png')

    mean = data['length'].describe()['mean']
    std = data['length'].describe()['std']

    percent = mean+std*3
    cleaned = data[data['length']<percent]
    plt.hist(cleaned['length'], bins = 20)  
    plt.title('Cleaned set')
    plt.savefig(out_dir+'/Cleaned set.png')

    prev = 0
    output = Counter({})
    print('Tokenizing..this may take more than 10 mins')
    for i in tqdm((np.arange(10000,2773022,10000).tolist()+[2773022])):
        tokens = data['sentence'][prev:i].str.split(expand=True).stack().value_counts().to_dict()
        output += Counter(tokens)
        prev = i
    
    token_arr = list(output.values())
    num_rare = sum(i < 5 for i in token_arr)

    plt.hist(list(output.values()), bins = 500)
    plt.title('tokens distribution')
    plt.savefig(out_dir+'/Token Distribution.png')

    strs = 'Mean for length distribution is ' + str(mean) + '. Std is ' + str(std) + '. Number of Rare tokens is ' + str(num_rare) +' .'

    f = open(out_dir+"description.txt", "a")
    f.write(strs)
    f.close()

    return
