### Background

The purpose of phrase mining is to extract high-quality phrases from a large amount of text corpus. It identifies the phrases instead of an unigram word, which provides a much more understanding of the text.  In this study, we apply AutoPhrase method into two different datasets and compare the decreasing quality ranked list of phrase ranked list in multi-words and single word. Our datasets are from the abstract of Scientific papers in English with the English knowledge base from Wikipedia. Through this project, we will be able to understand the advantages of the AutoPhrase method and how to implement Autophrase in two datasets by identifying different outcomes it produces. 

### Purpose of the Code

For Final Replication, our code would do the data ingestion proportion first, to pull data as the input corpus for future use from the cloud. Then to perform some basic EDA on it. At the end we would run the autophrase algorithm along with phrasal segmentation,analyzing the results.

### Code Content
Some Python Scripts, involved in etl.py, eda.py, auto.py, and visual.py to download, process data,analyze, and visualize data.

	
### How to Run the Code

To get the data, 


run python run.py etl


This downloads the data from Kaggle in the directory specified in config/etl-params.json and do data cleaning.


To do the eda for the data, 


run python run.py eda


This performs EDA and saves the figures in the location specified in config/eda-params.json.


To run autophrase algorithm, 


run python run.py auto


This performs autophrase algorithm and saves the results in the location specified in config/auto-params.json.


To analyze the output of autophrase, 


run python run.py visual


This performs analysis on the results and saves the figures in the location specified in config/visual-params.json.


To run whole project,

###run python run.py all


To make a test run,

###run python run.py test






### Work Cited

Professor Jingbo Shang’s Github: https://github.com/shangjingbo1226/AutoPhrase
Jingbo Shang, Jialu Liu, Meng Jiang, Xiang Ren, Clare R Voss, Jiawei Han, "Automated Phrase Mining from Massive Text Corpora", accepted by IEEE Transactions on Knowledge and Data Engineering, Feb. 2018.

### Responsibilities
We discussed the general idea of the replication project and outlined the steps of the process together.
Tiange Wan: majority of code portion, revised the report portion.
Yicen Ma: majority of report portion, revised the code portion.





