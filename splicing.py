#splicing
sentense = 'ooHnGRjycK02c467VemAm8bRzmcDPm8HAszRM8blqBTLSUcAIzX01zaJjeRjSC3KahTUeDI9udpzPhrynosomawsPpb5jCs9YmAFCCwxfScD48Mu5oUuJjPlNfMb2hkErwDV9BwED74gp9dxWiFHsLod6zXl95808Nra5FSLT0gBSfzrDQmP78cyaneab6DQMWA.'

numbers = [76, 85, 182, 187]

def SMTW(sentense, numbers) : 
    sentense = list(sentense)
    word1 = ''.join(sentense[numbers[0]:numbers[1]+1])
    word2 = ''.join(sentense[numbers[2]:numbers[3]+1])
    
    return print(f'{word1} {word2}')

SMTW(sentense, numbers)
