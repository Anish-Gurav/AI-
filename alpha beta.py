#!/usr/bin/env python
# coding: utf-8    
 
# In[ ]:





# In[ ]:


def alpha_beta(node,depth,a,b,maximizing_player):
    if depth==0 or isinstance(node,int):
        return node
    if maximizing_player:
        max_eval=-1000
        for child in node:
            eval=alpha_beta(child,depth-1,a,b,False)
            max_eval=max(max_eval,eval)
            a=max(a,eval)
            if b<=a:
                break
        return max_eval
    else:
        min_eval=1000
        for child in node:
            eval=alpha_beta(child,depth-1,a,b,True)
            min_eval=min(min_eval,eval)
            b=min(b,eval)
            if b<=a:
                break
        return min_eval

game_tree=[[3,5],[6,9],[1,2],[0,-1]]
result=alpha_beta(game_tree,depth=3,a=-1000,b=1000,maximizing_player=True)
print(result)
