#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[6]:


df = pd.read_excel('./datasets/prep1.xlsx', index_col=0)
df.head()


# In[7]:


for i in range(1, 3):
    data =  pd.read_excel('./datasets/prep{}.xlsx'.format(i), index_col=0) #뒤에 0을 안 넣어주면 unnamed=0생김
    df = pd.concat([df, data], ignore_index=True)


# In[8]:


df.to_excel('./datasets/prep.xlsx')


# In[9]:


import pandas_profiling
data = pd.read_excel('./datasets/prep.xlsx',encoding='latin1')
# 윈도우 바탕화면에서 작업한 저자의 경우에는
# data = pd.read_csv(r'C:\Users\USER\Desktop\spam.csv',encoding='latin1')


# In[10]:


health=data.profile_report() # 프로파일링 결과 리포트를 pr에 저장


# In[11]:


health.to_file('./health_report.html')


# In[ ]:




