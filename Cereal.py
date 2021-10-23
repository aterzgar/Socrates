#load libraries
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas import read_csv


#load dataset
url = 'cereal.csv'
dataset=read_csv(url)

#finding out if there is amy null values
print(dataset.isnull().sum())

#transforming manufacturer from single letter to their full names

dataset['mfr'] = dataset['mfr'].replace(
    {
        'A':'American Home Food Products',
        'G':'General Mills',
        'K':'Kelloggs',
        'N':'Nabisco',
        'P':'Post',
        'Q':'Quaker Oats',
        'R':'Ralston Purina',
    }
)
#print(dataset.head())
...
# class distribution
print(dataset.groupby('mfr').size())


#group by manufacturer and get sample size
entries_for_manufacturer = dataset.groupby('mfr').size()

#plot bar chart

plt.figure(1, figsize=(14,7))
plt.subplot(211)
plt.title('Entries per manufacturer')
sns.barplot(x=entries_for_manufacturer.index, y=entries_for_manufacturer)
plt.ylabel('Entries')
plt.xlabel('Manufacturer')


# groupby manufacturer and get mean values
calories_for_manufacturer = dataset.groupby('mfr').mean().calories

# plot a bar chart
plt.subplot(212)
plt.title('Average calories per manufacturer')
sns.barplot(x=calories_for_manufacturer.index, y=calories_for_manufacturer)
plt.xlabel("Manufacturer")
plt.ylabel("Calories")
plt.show()