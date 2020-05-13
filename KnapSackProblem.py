items = [(4,6), (12,13), (4,12), (19,15), 
         (1,2), (3,4), (2,6), (2,11), (6,9)]

weight = [None] + [x[0] for x in items]
value = [None] + [x[1] for x in items]
lookup_tbl = {}
def KS(cap_left, nitem_left):
    """TODO: write a function to output the maximum value that 
    a knapsack can contain given a list of items with (weight,value)
    pairs.
    ARGUMENTS: 
        * cap_left: capacity left of the Knapsack (integer)
        * nitem_left: number of items left to be considered, also 
        the index of the item under consideration (integer)
    RETURN: maximum value a knapsack can contain.
    """
    # memoization
    if (cap_left, nitem_left) in lookup_tbl:
        return lookup_tbl[(cap_left, nitem_left)]
    
    # base case
    if nitem_left == 0 or cap_left == 0:
        ret_value = 0
    
    # recursion
    elif weight[nitem_left] > cap_left:
        ret_value = KS(cap_left, nitem_left - 1)
    else:
        KS_n = KS(cap_left, nitem_left - 1)
        KS_y = value[nitem_left] + \
                KS(cap_left - weight[nitem_left], nitem_left - 1)
        ret_value = max(KS_n, KS_y)
        
    # keep a copy in the lookup table
    lookup_tbl[(cap_left, nitem_left)] = ret_value
    return ret_value
        
    
KS(25,9)
KS(30,9)

