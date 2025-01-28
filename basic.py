#https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf
#https://leetcode.com/problems/two-sum/description/

def two_sum(b,t):
    m={} # to store the key value of value : index
    for i,n in enumerate(b):#iterates through the index and the number in the list
        d = t-n #difference between the target and the number
        if d in m: #if the difference is in the dictionary
            return [i,m[d]]
        m[n]=i #add the number and the index to dictionary 
    return []
    
#Driver Code

b=[1,3,4,6,2]
t=6
print(two_sum(b,t))
