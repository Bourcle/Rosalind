#Brief introduction to graph theory
def fastq2adj_dic(file) : 
    dic = {}
    adj_dic = {}
    with open(file) as f : 
        for line in f : 
            line = line.strip()
            if '>' in line : 
                read_id = line.replace('>', '')
                dic.setdefault(read_id, [])
                adj_dic.setdefault(read_id, [])
            else : 
                dic[read_id].append(line)
    key_list = dic.keys()
    for i in key_list : 
        dic[i] = ''.join(dic[i])
        dic[i] = list(dic[i])
        start = ''.join(dic[0:3])
        end = ''.join(dic[-3:-1])
        adj_dic[i].append(start)
        adj_dic[i].append(end)
    
    df = pd.DataFrame(
        adj_dic, 
        index = ['Start', 'End']).T

    return df


def print_adj(df) : 
    random_row = df.sample(n=3).index.to_list()
    adj_list = []
    for i in random_row : 
        for j in df.columns.to_list : 
            if df.loc[i, 'End'].values[0] == df.loc[j, 'Start'].values[0] & df.loc[i, 'End'].values[0] != df.loc[i, 'Start'].values[0] : 
                adj_list.append(f'{i} {j}')
            else : continue
            
    return adj_list


file = '/Users/idean/Downloads/rosalind_grph.txt'

df = fastq2adj_dic(file)
adj_list = print_adj(df)

for i in adj_list : 
    print(i)


