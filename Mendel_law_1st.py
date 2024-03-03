#Mendel's First Law (Random Variable)
def cal_prob(k, m, n) : 
    total = k + m + n
    p_total = total - 1
    p_k, p_m, p_n = k - 1, m - 1, n -1 
    
    k_k = k / total * p_k / p_total
    k_m = k / total * m / p_total
    k_n = k / total * n / p_total
    m_k = m / total * k / p_total
    m_m = m / total * p_m / p_total * 3/4
    m_n = m / total * n / p_total * 1/2
    n_k = n / total * k / p_total 
    n_m = n / total * m / p_total * 1/2
    
    probability = k_k + k_m + k_n + m_k + m_m + m_n + n_k + n_m
    
    return probability

k, m, n = 19, 17, 18    
cal_prob(k, m, n)
