import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
df=pd.read_csv("personality.csv")
df.columns
df['Stage_fear']=df['Stage_fear'].replace({"No":0,"Yes":1})
df['Personality']=df['Personality'].replace({"Extrovert":0,"Introvert":1})
df['Drained_after_socializing']=df['Drained_after_socializing'].replace({"No":0,"Yes":1})
sns.pairplot(df,hue='Personality')
plt.show()
df.corr()