import subprocess
import os

def test(output_path):
    mycwd = os.getcwd()
    #subprocess.run(['brew','install','gcc6'])
    #subprocess.run(['brew','update'])
    os.rename('./test/DBLP.05K.txt', './AutoPhrase/data/EN/DBLP.05K.txt')
    os.chdir('AutoPhrase')
    subprocess.run(['chmod','+x','auto_phrase.sh'])
    subprocess.run(['./auto_phrase.sh','DBLP.05k.txt'])

    os.chdir(mycwd)
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase.txt', '.'+output_path + '/AutoPhrase.txt')
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase_multi-words.txt', '.'+output_path+'/AutoPhrase_multi-words.txt')
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase_single-word.txt', '.'+output_path +'/AutoPhrase_single-word.txt')
    os.rename('./AutoPhrase/models/DBLP/token_mapping.txt', '.'+output_path + '/token_mapping.txt')
    os.rename('./AutoPhrase/models/DBLP/segmentation.model', '.'+output_path +'/segmentation.model')

    return