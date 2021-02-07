import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from collections import Counter
from tqdm import tqdm
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import collections

def visual(out_dir,input_path,file,autophrase,multi_word,single_word,token_mapping):
    print("Creating Distribution graphs of the outputs")
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
    
    try:
        with open('data/raw/DBLP.5K.txt', 'r') as file:
            data = file.read().split('\n')
        ds = pd.read_csv('data/outputs/AutoPhrase_single-word.txt',sep='\t')
        
        
        #tf-idf top 20 
        tfIdfVectorizer=TfidfVectorizer(stop_words='english')
        tfIdf = tfIdfVectorizer.fit_transform(data)
        cum = []
        for i in tqdm(range(tfIdf.shape[0])):
            df = pd.DataFrame(tfIdf[i].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
            df = df[df['TF-IDF']!=0].sort_values('TF-IDF', ascending=False)
            cum.append(df['TF-IDF'].to_dict())
        counter = collections.Counter()
        for d in cum: 
            counter.update(d)
        res = pd.DataFrame({'Word':dict(counter).keys(),'Score':dict(counter).values()})
        res.sort_values('Score',ascending=False,inplace=True)
        res.to_csv('data/outputs/tfidf.csv',index=False)
        
        
        #autophrase top 20
        row = ds.columns.values
        ds.columns = ['Score','Word']
        ds.loc[len(df)] = row
        ds['Score'] = ds['Score'].apply(lambda x:float(x))
        ds.sort_values('Score',inplace=True,ascending=False)
        res.index = res.Word
        ds.index = ds.Word
        ds.to_csv('data/outputs/quality.csv',index=False)
        
        #multiplication top 20
        haha = {}
        for key in ds.Score.to_dict():
            try:
                value = (ds.Score.to_dict()[key] * res.Score.to_dict()[key])
                haha[key] = value
            except:
                pass
        lala = pd.DataFrame({'Word':haha.keys(),'Score':haha.values()})
        lala.sort_values('Score',ascending=False,inplace=True)
        lala.to_csv('data/outputs/multiplication.csv',index=False)
        
    except:
        print('This part works for test run only!')

    
    print("Done!")
    print("Distribution graphs are in the /data/outputs folder!")
    return
