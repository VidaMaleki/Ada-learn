class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
            
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict= {}
        t_dict = {}
        for i, j in zip(s, t):
            s_dict[i] = s_dict.get(i, 0) +1
            t_dict[j] = t_dict.get(j, 0) +1
            
        evaluation = []
        for k, v in s_dict.items():
            if k in t_dict:
                if v == t_dict[k]:
                    evaluation.append("True")
                    
        if len(evaluation) == len(s_dict):
            return True
        return False
    
