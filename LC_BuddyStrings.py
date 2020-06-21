class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        :time complexity: O(n)
        :space complexity: O(1)
        """
        if len(A) == len(B):
            ind1, ind2 = -1, -1
            for i in range(len(A)):
                if A[i] != B[i]:
                    if ind1 == -1:
                        ind1 = i
                    elif ind1 != -1 and ind2 == -1:
                        ind2 = i
                    else:
                        return False

            if A[ind1] == B[ind2] and A[ind2] == B[ind1]:
                if (ind1!=-1 and ind2!=-1) or (ind1==-1 and ind2==-1):
                    return True
        
        return False