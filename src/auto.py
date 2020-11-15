import subprocess
import
def autophrase(input_path):

    if input_path== "data/raw/DBLP.csv":
        subprocess.run(['brew','install','gcc6'])
        subprocess.run(['brew','update'])
        os.chdir('AutoPhrase')
#        subprocess.call(["cd", "AutoPhrase"])
        subprocess.run(['chmod','+x','auto_phrase.sh'])
        subprocess.run(['./auto_phrase.sh'])
        subprocess.run(['cd'])
        return
