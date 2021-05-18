import pandas as pd
import string
import re

def process(x):
    x = re.sub(r'([?.,!])$',r' \1', x)
    return x
        
if __name__ == '__main__':
    counsel = {
        'counsel_chat' : './Data/20200325_counsel_chat.csv',
        'counsel_chat_1' : './Data/counselchat-data.csv',
    }
    scrap = {
        'scrap' : './Data/scrap.csv',
        'scrap_context' : './Data/scrap_context.csv',
    }

    for name in counsel:
        print(name, counsel[name])
        pd_name = pd.read_csv(counsel[name])
        pd_name = pd.DataFrame(pd_name, columns=['questionTitle', 'answerText'])
        pd_name = pd_name.replace(r'"', r'', regex=True)
        pd_name['questionTitle'] = '0.0 '+ pd_name['questionTitle'].astype(str)
        pd_name['answerText'] = '1.0 '+ pd_name['answerText'].astype(str)
        pd_name['questionTitle'] = pd_name['questionTitle'].apply(process)
        pd_name['answerText'] = pd_name['answerText'].apply(process)
        print(pd_name)
        pd_name.to_csv('./Data/'+name+'.tsv', sep='\t', index=False)

    for name in scrap:
        print(name, scrap[name])
        pd_name = pd.read_csv(scrap[name])
        pd_name = pd.DataFrame(pd_name, columns=['title', 'response'])
        pd_name = pd_name.replace(r'"', r'', regex=True)
        pd_name['title'] = '0.0 '+ pd_name['title'].astype(str)
        pd_name['response'] = '1.0 '+ pd_name['response'].astype(str)
        pd_name['title'] = pd_name['title'].apply(process)
        pd_name['response'] = pd_name['response'].apply(process)
        print(pd_name)
        pd_name.to_csv('./Data/'+name+'.tsv', sep='\t', index=False)
 
