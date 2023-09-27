class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1=0
        ptr2=0
        resStr=''
        maxLen=max(len(word1),len(word2))
        for i in range(0,maxLen):
            if(ptr1<len(word1)):
                resStr+=word1[ptr1]
                ptr1+=1
            if(ptr2<len(word2)):
                resStr+=word2[ptr2]
                ptr2+=1
        return resStr