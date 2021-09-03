#滑动窗口for包含字串
#s1="ab"
#s2="eidbaoo"
#check wheter the permutation of s1 is in s2
import collections
def slidewindow(s,t):
     window = collections.defaultdict(int)
     need = collections.defaultdict(int)
     #给taget计数
     for i in t: need[i] += 1
     left = 0
     right = 0
     valid = 0
     while right<len(s):
         c = s[right]
         right += 1
         if need[c] >0:
             window[c]+=1
             if window[c]==need[c]:
                valid += 1
         #Judge the left is supposed to change
         while right-left>=2: #len(t):
             if valid==2: #len(need):
                 return True
             d = s[left]
             left += 1
             if need[d]>0:
                 if window[d]==need[d]:
                     valid -=1
                 window[d] -= 1
     return False,len(need),need

if __name__ == "__main__":
    s1="ab"
    s2="eidabobo"
    print(slidewindow(s2,s1))

















