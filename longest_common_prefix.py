# Problem: Two Sum (LeetCode #1)
# Link: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
#
# Description:
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target. You may assume 
# that each input would have exactly one solution.

# Complexity:
# Time: O(n) - Single pass through the hash map
# Space: O(n) - Storing elements in the dictionary

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        out=''
        commonl=[]
        maxprefix=''
        s1=strs[0]
        #flag=0

       
        for i in range(len(s1)): #0->5 0
            flag=0 #0
            for j in range(i,len(s1)+1): #0->6 0 
                prefix=''.join(s1[i:j]) #[0:0] -> ''

                if prefix!='':
                    #print(prefix) 
                    for s2 in strs[1:]:
                        if prefix not in s2:
                            flag=1
                            break
                        if len(prefix)>len(maxprefix):
                            maxprefix=prefix
                            #print('max:',maxprefix)
                        commonl.append(prefix)
                        #print(commonl)

                        
                    if flag==1:
                        break

        return maxprefix


# Solution explained:

