
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
dat = open("/Users/James/Downloads/recent-grads.csv", "r")
recent_grads = pd.read_csv(dat)


# "%matplotlib inline" is a jupyter magic command so the plots are in line.

# In[2]:


table = recent_grads.iloc[0,:]


# In[3]:


table


# In[4]:


recent_grads.head()


# In[5]:


recent_grads.tail()


# In[6]:


recent_grads.describe()


# In[7]:


print(recent_grads.shape)
raw_data_count = 173
recent_grads = recent_grads.dropna()
print(recent_grads.shape)
cleaned_data_count = 172


# In[8]:


recent_grads.plot(x='Sample_size', y='Employed', kind='scatter')


# The scatter plot is displayed immediately after running the above code, because of the Jupyter magic code inline at the top.

# In[9]:


ax = recent_grads.plot(x='Sample_size', y='Median', kind='scatter')
ax.set_title('Median vs. Sample_size')


# In[10]:


ax = recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter')
ax.set_title('Unemployment Rate vs. Sample_size')


# In[11]:


ax = recent_grads.plot(x='Full_time', y='Median', kind='scatter')
ax.set_title('Median vs. Full Time')


# In[12]:


ax = recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter')
ax.set_title('Unemployment_rate vs. Share Women')


# In[13]:


ax = recent_grads.plot(x='Men', y='Median', kind='scatter')
ax.set_title('Median vs. Men')


# In[14]:


ax = recent_grads.plot(x='Women', y='Median', kind='scatter')
ax.set_title('Median vs. Women')


# 
#     Rank - Rank by median earnings (the dataset is ordered by this column).
#     Major_code - Major code.
#     Major - Major description.
#     Major_category - Category of major.
#     Total - Total number of people with major.
#     Sample_size - Sample size (unweighted) of full-time.
#     Men - Male graduates.
#     Women - Female graduates.
#     ShareWomen - Women as share of total.
#     Employed - Number employed.
#     Median - Median salary of full-time, year-round workers.
#     Low_wage_jobs - Number in low-wage service jobs.
#     Full_time - Number employed 35 hours or more.
#     Part_time - Number employed less than 35 hours.
# 

# Looking at median vs sample size, it appears that as number of students graduating from a particular subject increases, the median full-time wage does not increase, if anything it's slightly lower. Unemployment doesn't have a strong correlation though.
# It does appear that as more graduates are employed full time from a subject, the pay decreases. So more jobs for a certain subject means a lower pay from this data.

# In[15]:


ax = recent_grads['Sample_size'].hist(bins=30, range=(0,3000))
ax.set_xlabel("Sample Size")
ax.set_ylabel("Frequency")


# In[16]:


ax = recent_grads['Median'].hist(bins=30, range=(20000,80000))
ax.set_xlabel("Median FT Salary")
ax.set_ylabel("Frequency")


# In[17]:


ax = recent_grads['Employed'].hist(bins=30, range=(0,100000))
ax.set_xlabel("Number Employed")
ax.set_ylabel("Frequency")


# In[18]:


ax = recent_grads['Full_time'].hist(bins=30, range=(0,175000))
ax.set_xlabel("Number Employed Full Time")
ax.set_ylabel("Frequency")


# In[19]:


ax = recent_grads['ShareWomen'].hist(bins=15, range=(0,1))
ax.set_xlabel("Women as a share of total")
ax.set_ylabel("Frequency")


# In[20]:


ax = recent_grads['Unemployment_rate'].hist(bins=15, range=(0,0.2))
ax.set_xlabel("Rate of Unemployment")
ax.set_ylabel("Frequency")


# In[21]:


ax = recent_grads['Men'].hist(bins=25, range=(0,150000))
ax.set_xlabel("Number of Male Graduates")
ax.set_ylabel("Frequency")


# In[22]:


ax = recent_grads['Women'].hist(bins=25, range=(0,200000))
ax.set_xlabel("Number of Female Graduates")
ax.set_ylabel("Frequency")


# In[23]:


from pandas.plotting import scatter_matrix


# In[24]:


scatter_matrix(recent_grads[["Sample_size", "Median"]], figsize=(10,10))


# In[25]:


scatter_matrix(recent_grads[["Sample_size", "Median", "Unemployment_rate"]], figsize=(10,10))


# In[26]:


recent_grads[:10]['ShareWomen'].plot(kind='bar')


# In[27]:


recent_grads[-10:]['Women'].plot(kind='bar')


# In[28]:


recent_grads[:10]['Unemployment_rate'].plot(kind='bar')


# In[29]:


recent_grads[-10:]['Unemployment_rate'].plot(kind='bar')

