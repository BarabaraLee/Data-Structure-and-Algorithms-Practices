class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        :time complexity: O(n)
        :space complexity: O(n)
        """
        from collections import Counter
        
        banned = set(banned)
        for c in ",.:;!?'":
            paragraph = paragraph.replace(c, " ")
        
        seq = [x for x in paragraph.lower().split() ]
        word_dict = Counter(seq)
        
        mc_word = ""
        mc_cnt = 0
        for word in word_dict:
            if word_dict[word] > mc_cnt and word not in banned:
                mc_cnt = word_dict[word]
                mc_word = word
                
        return mc_word