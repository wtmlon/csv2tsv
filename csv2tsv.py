import pandas as pd

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
        pd_name = pd_name.replace(r'([?.,!"])', r' \1', regex=True)
        pd_name.columns=['0.0 question', ' 1.0 answer']
        print(pd_name)
        pd_name.to_csv('./Data/'+name+'.tsv', sep='\t', index=False)

    for name in scrap:
        print(name, scrap[name])
        pd_name = pd.read_csv(scrap[name])
        pd_name = pd.DataFrame(pd_name, columns=['title', 'response'])
        pd_name = pd_name.replace(r'([?.,!"])', r' \1', regex=True)
        pd_name.columns=['0.0 question', '  1.0 answer']
        print(pd_name)
        pd_name.to_csv('./Data/'+name+'.tsv', sep='\t', index=False)
 
