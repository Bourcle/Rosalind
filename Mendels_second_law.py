#Meddel's Second Law
def binomial_coefficient(n, k):
    # Calculate binomial coefficient using dynamic programming
    dp = [0] * (k + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            dp[j] = dp[j] + dp[j - 1]
            j -= 1
            
    return dp[k]

def calculate_probability(k, N):
    # Probability of each individual having genotype Aa Bb
    prob_AaBb = 1/4  # Probability of inheriting each allele independently
    
    # Initialize probability of having at least N organisms with genotype Aa Bb
    total_probability = 0
    
    # Calculate probability using binomial distribution #적어도 N이상이면 정확히 N일떄의 확률을 구한 다음 그 이후의 확률을 다 더하면 됨
    for n in range(N, 2**k + 1):  # Iterate over possible numbers of organisms with genotype Aa Bb #AaBb냐 아니냐로 나뉘기 떄문에 이항분포라서 2의 k제곱임
        probability_of_N = binomial_coefficient(2**k, n) * (prob_AaBb ** n) * ((1 - prob_AaBb) ** (2**k - n))
        total_probability += probability_of_N
    
    return total_probability
