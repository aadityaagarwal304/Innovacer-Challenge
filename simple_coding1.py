import pandas as pd
import numpy as np

data= pd.read_csv("C:/Users/aaditya_agarwal23/Desktop/Innovacer/DeduplicationProblem.csv")

def get_title(name):
    if ' ' in name:
        return name.split(' ')[1].strip()
    else:
        return 'Unknown'
c_dict={}

data['Title'] = data['lastname'].map(lambda x: get_title(x))

def get_title(name):
    if ' ' in name:
        return name.split(' ')[0].strip()
    else:
        return name

def get_middlename(name):
    if ' ' in name:
        return name.split(' ')[1].strip()
    else:
        return 'Unknown'

data['LastName'] = data['lastname'].map(lambda x: get_title(x))


data['middlename'] = data['firstname'].map(lambda x: get_middlename(x))

data['Name']= data.firstname+' ' + data.LastName

grouped = data.groupby('dob')

data.dob= pd.to_datetime(data.dob)

data= data.sort_values('dob', ascending=0)
data = data.reset_index(drop=True)

a=data.dob.unique()

dob_count= len(a)

dob_freq= data.dob.value_counts()
dob_freq= dob_freq.sort_index(ascending=0)
initial=0
for x in xrange(0,dob_count):
    
    c_dict[x]=data.iloc[initial:initial+dob_freq[x],:]
    initial= initial+ dob_freq[x]
    
    initial1=0
    
for x in xrange(0,dob_count):
    for y in range(initial1,initial1+len(c_dict[x])):
        
        if c_dict[x].Name.value_counts()[c_dict[x].Name[y]] == 1:
             c_dict[x].Unique[y]=1
        elif c_dict[x].Title.value_counts()[c_dict[x].Title[y]]=='Unknown':
             c_dict[x].Unique[y]=0
        elif c_dict[x].Title.value_counts()[c_dict[x].Title[y]]=='Unknown':
             c_dict[x].Unique[y]=1
        else:
             c_dict[x].Unique[y]=0  
    initial1= initial1+len(c_dict[x])   
      