import subprocess
import os

def test(input_file):
    mycwd = os.getcwd()
    #subprocess.run(['brew','install','gcc6'])
    #subprocess.run(['brew','update'])
    os.rename('./test/'+input_file, './AutoPhrase/data/EN/'+input_file)
    os.chdir('AutoPhrase')
    subprocess.run(['chmod','+x','auto_phrase.sh'])
    subprocess.run(['./auto_phrase.sh',input_file])

    os.chdir(mycwd)
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase.txt', './data/outputs/AutoPhrase.txt')
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase_multi-words.txt', './data/outputs/AutoPhrase_multi-words.txt')
    os.rename('./AutoPhrase/models/DBLP/AutoPhrase_single-word.txt', './data/outputs/AutoPhrase_single-word.txt')
    os.rename('./AutoPhrase/models/DBLP/token_mapping.txt', './data/outputs/token_mapping.txt')
    os.rename('./AutoPhrase/models/DBLP/segmentation.model', './data/outputs/segmentation.model')
    os.rename('./AutoPhrase/data/EN/'+input_file,'./test/'+input_file)

    print("You can now see the results in ./data/outputs folder!")

    return
