import subprocess
import os

def autophrase(input_path):
    mycwd = os.getcwd()
    if input_path== "data/raw/DBLP.csv":
        subprocess.run(['brew','install','gcc6'])
        subprocess.run(['brew','update'])
        os.chdir('AutoPhrase')
        subprocess.run(['chmod','+x','auto_phrase.sh'])
        subprocess.run(['./auto_phrase.sh'])

        os.rename('/AutoPhrase/models/DBLP/AutoPhrase.txt', '/data/outputs/AutoPhrase.txt')
        os.rename('/AutoPhrase/models/DBLP/AutoPhrase_multi-words.txt', '/data/outputs/AutoPhrase_multi-words.txt')
        os.rename('/AutoPhrase/models/DBLP/AutoPhrase_single-word.txt', '/data/outputs/AutoPhrase_single-word.txt')
        os.rename('/AutoPhrase/models/DBLP/token_mapping.txt', '/data/outputs/token_mapping.txt')
        os.rename('/AutoPhrase/models/DBLP/segmentation.model', '/data/outputs/tsegmentation.model')
        os.chdir(mycwd)
        return
