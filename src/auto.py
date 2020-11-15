import subprocess
def autophrase(input_path):

    if input_path== "data/raw/DBLP.csv":
        subprocess.run(['brew','install','gcc6'])
        subprocess.run(['brew','update'])
        subprocess.run(['cd/AutoPhrase'])
        subprocess.run(['auto_phrase.sh'])
        subprocess.run(['cd'])
        return
