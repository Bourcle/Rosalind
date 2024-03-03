def rabbit_pairs_mortal(n, m) : 
    a = 1
    total = [] #값들을 list로 받음
    for i in range(1, n+1): #range는 끝이 n+1이 되어야 한다.
        if i == 1 or i ==  2 : 
            total.append(a)
        if i > 2 and i <= m : 
            value = total[i - 2] + total[i - 3]
            total.append(value)
        if i > m : 
            value = sum(total[i - (m + 1) : i - 2])
            total.append(value)
    return total[-1]



# Example usage
month = 96
life = 17

result = rabbit_pairs_mortal(month, life)
print(result)
