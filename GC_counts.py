#GC contents (%)

import pandas as pd
dic = {}
with open('/Users/idean/Downloads/rosalind_gc.txt') as f : 
    for line in f : 
        line = line.strip()
        if '>' in line : 
            read_id = line.replace('>', '')
            dic.setdefault(read_id, [])
        else : 
            dic[read_id].append(line)

def gc_percent(string) : 
    total = len(string)
    n_GC = string.count('G') + string.count('C')
    
    percent = n_GC * 100 / total
    
    return percent

answer = {}
for i in dic.keys() : 
    dic[i] = ''.join(dic[i])
    answer.setdefault(i, '')
    answer[read_id] = gc_percent(dic[i])

df = pd.DataFrame(answer, index=[0]).T

#the answer is!?
print(f'{df[0].idxmax()}\n{max(df[0])}')
