import pandas as pd
import numpy as np

#Importing Data
data= pd.read_csv("C:/Users/aaditya_agarwal23/Desktop/Innovacer/DeduplicationProblem.csv")

#Function for extracting Title. For eg. JR
def get_title(name):
    if ' ' in name:
        return name.split(' ')[1].strip()
    else:
        return 'Unknown'
#Making a dictionary    
c_dict={}

#Seperating Title
data['Title'] = data['lastname'].map(lambda x: get_title(x))

#Extracting Lastname without Title
def get_title(name):
    if ' ' in name:
        return name.split(' ')[0].strip()
    else:
        return name

#Extracting middlename 
def get_middlename(name):
    if ' ' in name:
        return name.split(' ')[1].strip()
    else:
        return 'Unknown'

#Seperating Lastname
data['LastName'] = data['lastname'].map(lambda x: get_title(x))

#Seperating middlename from 1st name
data['middlename'] = data['firstname'].map(lambda x: get_middlename(x))

#Combining First and Last Name
data['Name']= data.firstname+' ' + data.LastName

#Grouping data by dob
grouped = data.groupby('dob')

#Sorting data acc to dob in descending order
data.dob= pd.to_datetime(data.dob)

data= data.sort_values('dob', ascending=0)
data = data.reset_index(drop=True)

a=data.dob.unique()

dob_count= len(a)

dob_freq= data.dob.value_counts()
dob_freq= dob_freq.sort_index(ascending=0)
initial=0

#Applying loop to form multiple data frames with same dob's in a dictionary
for x in xrange(0,dob_count):
    
    c_dict[x]=data.iloc[initial:initial+dob_freq[x],:]
    initial= initial+ dob_freq[x]
    
    initial1=0
    
#Applying nested loop to check for unique names in the dataframe    
for x in xrange(0,dob_count):
    for y in range(initial1,initial1+len(c_dict[x])):
        if c_dict[x].middlename.value_counts()[c_dict[x].middlename[y]] == 1:
            c_dict[x].Unique[y]=0
        elif c_dict[x].Name.value_counts()[c_dict[x].Name[y]] == 1:
             c_dict[x].Unique[y]=1
        elif c_dict[x].Title.value_counts()[c_dict[x].Title[y]]=='Unknown':
             c_dict[x].Unique[y]=0
        elif c_dict[x].Title.value_counts()[c_dict[x].Title[y]]=='Unknown':
             c_dict[x].Unique[y]=1
        else:
             c_dict[x].Unique[y]=0  
    initial1= initial1+len(c_dict[x])   
#Unique value gets listed out