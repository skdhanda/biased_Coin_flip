#!/usr/bin/python
seq="forgeeksskeegfor"
#seq="geeeksdfds"
class Solution(object):
    def countSubstrings(self, S):
        """
        :type s: str
        :rtype: int
        """
        pal_list=[]
        N = len(S)
        ans = 0
        
        for center in xrange(2*N -1):
            left = center / 2
            right = left + center % 2
            pal=''
            while left >= 0 and right < N and S[left] == S[right]:
              if left==right:
                pal=S[left]
              else:
                pal=S[left]+pal+S[right]
              if len(pal) >1:
                pal_list.append(pal)
              ans += 1
              left -= 1
              right += 1
        print pal_list
        pal_len=[len(x) for x in pal_list]
        max_len=max(pal_len)
        print max_len
        ind=pal_len.index(max_len)
        print pal_list[ind]
        return ans
s=Solution()
s.countSubstrings(seq)
