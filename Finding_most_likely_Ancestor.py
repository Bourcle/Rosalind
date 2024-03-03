#Finding a Most Likely common Ancestor
    
def fastq2dic(file) : 
    dic = {}
    with open(file) as f : 
        for line in f : 
            line = line.strip()
            if '>' in line : 
                read_id = line.replace('>', '')
                dic.setdefault(read_id, [])
            else : 
                dic[read_id].append(line)
    key_list = dic.keys()
    for i in key_list : 
        dic[i] = ''.join(dic[i])
        dic[i] = list(dic[i])
    
    key_name = list(dic.keys())[0]
    length = len(dic[key_name])
    
    df = pd.DataFrame(
        dic, 
        index=range(0, length+1)
        ).T
    return df


def finding_max(list) : 
    cal_dic = {'A':[], 'G':[], 'T':[], 'C':[]}
    for i in cal_dic.keys() : 
        cal_dic[i].append(list.count(i)) 
    code = max(cal_dic, key = cal_dic.get)
    
    return code, cal_dic
    
    
def finding_con(file) : 
    df = fastq2dic(file)
    cal_list = []
    profile_dic = {'A':[], 'G':[], 'T':[], 'C':[]}
    for i in df.columns : 
        code, cal_dic = finding_max(df[i].tolist())
        cal_list.append(code)
        for j in profile_dic.keys() : 
            #profile_dic[j].append(str(cal_dic[j]).replace('[', '').replace(']', ''))
            profile_dic[j].append(', '.join(map(str, cal_dic[j])))
    
    consensus = ''.join(cal_list)
    
    return consensus, profile_dic, cal_dic

file = '/Users/idean/Downloads/rosalind_cons.txt'
consensus, profile_dic, cal_dic = finding_con(file)
A_items = ' '.join(profile_dic['A'])
C_items = ' '.join(profile_dic['C'])
G_items = ' '.join(profile_dic['G'])
T_items = ' '.join(profile_dic['T'])

print(f'{consensus}\nA: {A_items}\nC: {C_items}\nG: {G_items}\nT: {T_items}')
