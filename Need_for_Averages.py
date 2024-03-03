#The need for Averages
prob_dic = {
    0 : 1, 
    1 : 1, 
    2 : 1, 
    3 : 0.75, 
    4 : 0.5, 
    5 : 0}

couples = [17465, 19015, 18565, 18499, 17507, 16145]

def cal_nfa(p_dic, c_list) : 
    expected = 0
    for i in range(0,6) : 
        expected += 2 * c_list[i] * p_dic[i]
    
    return expected

print(cal_nfa(prob_dic, couples))
    
