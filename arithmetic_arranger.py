#!/usr/bin/env python
# coding: utf-8

# In[48]:


probs=['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']
arithmetic_arranger(probs)


# In[47]:


def arithmetic_arranger(problems,display=False):
    num=len(problems)
    try:
        if num > 5:
            raise BaseException
    except:
          return('Error: Too many problems.')

    stripped=[s.split(' ') for s in problems]
    try:
        for i in range(num):
            if stripped[i][1]!=('+') and stripped[i][1]!=('-'):
                raise BaseException
    except:
        return('Error: Operator must be \'+\' or \'-\'.')


    lengths=[max(len(stripped[s][0]),len(stripped[s][2])) for s in range(num)]
    try:
        if max(lengths)>4:
            raise BaseException
    except:
        return('Error: Numbers cannot be more than four digits.')

    op = {'+': lambda x, y: x + y,
            '-': lambda x, y: x - y}
    try:
          sums=[op[stripped[i][1]](int(stripped[i][0]),int(stripped[i][2])) for i in range(num)]
    except:
          return('Error: Numbers must only contain digits.')

    lengths=[s+2 for s in lengths]
    top=''
    spaces=[lengths[s]-len(stripped[s][0]) for s in range(num)]
    for i in range(num):
        top=top+spaces[i]*' '+stripped[i][0]+4*' '
        

    bottom=''
    spaces=[lengths[s]-len(stripped[s][2]) for s in range(num)]
    for i in range(num):
        bottom=bottom+stripped[i][1]+(spaces[i]-1)*' '+stripped[i][2]+4*' '
     
    dashes=''
    for i in range(num):
        dashes=dashes+'-'*lengths[i]+' '*4
    
    sums=[str(sums[i]) for i in range(num)]
    last=''
    spaces=[lengths[s]-len(sums[s]) for s in range(num)]
    for i in range(num):
        last=last+' '*spaces[i]+sums[i]+' '*4
    
    if display==True:
        arranged_problems=(top.rstrip()+'\n'+bottom.rstrip()+'\n'+dashes.rstrip()+'\n'+last.rstrip())
    else:
        arranged_problems=(top.rstrip()+'\n'+bottom.rstrip()+'\n'+dashes.rstrip())
    return arranged_problems



# In[ ]:




