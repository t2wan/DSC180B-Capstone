import subprocess
import os

def test(input_path):
   
    mycwd = os.getcwd()
#     subprocess.call(['brew','install','gcc6'], shell=True)
#     subprocess.call(['brew','update'], shell=True)
    os.rename('./test/'+ input_path, './AutoPhrase/data/EN/' + input_path)
    os.chdir('AutoPhrase')

    subprocess.call(['chmod','+x','auto_phrase.sh'], shell=True)
    subprocess.call(['./auto_phrase.sh'], shell=True)
    subprocess.call(['./auto_phrase.sh', input_path], shell=True)

    os.chdir(mycwd)
    
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase.txt', './data/outputs/test/AutoPhrase.txt')
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase_multi-words.txt', './data/outputs/test/AutoPhrase_multi-words.txt')
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase_single-word.txt', './data/outputs/test/AutoPhrase_single-word.txt')
    os.rename('./AutoPhrase/models/DBLP/token_mapping.txt', './data/outputs/test/token_mapping.txt')
    os.rename('./AutoPhrase/models/DBLP/segmentation.model', './data/outputs/test/segmentation.model')
    os.rename('./AutoPhrase/data/EN/'+ input_path, './test/' + input_path)

    return
