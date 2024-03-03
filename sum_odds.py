def sum_odds(num1, num2) : 
    output = 0
    for i in range(num1, num2+1) : 
        if i % 2 != 0 : 
            output += i
        else : 
            continue
    return output

print(sum_odds(4875, 9771))
