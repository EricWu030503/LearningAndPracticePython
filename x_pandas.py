import pandas as pd
import re
pd.set_option("display.max_rows", None, "display.max_columns", None) #enable to print all the rows and columns
df_csv=pd.read_csv('/Users/owen/Desktop/pokemon_data.csv')
df_xlsx=pd.read_excel('/Users/owen/Desktop/pokemon_data.xlsx')
df_txt=pd.read_csv('/Users/owen/Desktop/pokemon_data.txt',delimiter='\t')
print(df_csv)
print(df_xlsx.head(3)) #print out first three rows
print(df_txt.tail(3)) #print out last three rows
print(df_csv.columns) #headers
print(df_csv['Name']) #print out the name column
print(df_csv['Name'][0:5]) #print out the first 5 items in name column
print(df_csv.Name) #print out the name column
print(df_csv[['Type 1','Name','HP']]) #print out these three columns
print(df_csv.iloc[2]) #print out the third row
print(df_csv.iloc[2:4]) #print out the third row and fourth row
print(df_csv.iloc[2,1]) #print out the item in third row second column
for index, row in df_csv.iterrows():
    print(index,row['Name']) #print out all the names with index
print(df_csv.loc[df_csv['Type 1']=='Grass']) #print out all the rows with type1 grass
print(df_csv.describe()) #provide statistical data on different columns
print(df_csv.sort_values('Name')) #sort the data based on names in alphabetical order
print(df_csv.sort_values('Name',ascending=False)) #sort the data based on names in alphabetical order(z-a)
print(df_csv.sort_values(['HP','Name'])) #sort the data based on two categories and HP has the priority since it is the first one
df_csv['Total']=df_csv['HP']+df_csv['Attack']+df_csv['Defense']+df_csv['Sp. Atk']+df_csv['Sp. Def']+df_csv['Speed'] #create a new column Total as the sum
df_csv=df_csv.drop(columns='Name') #delete a column
df_csv['Total']=df_csv.iloc[:,4:10].sum(axis=1) #create a new column Total as the sum; axis=1 means adding horizontally and axis=0 means adding vertically
cols=list(df_csv.columns)
df_csv=df_csv[cols[0:10]+[cols[-1]]+cols[10:12]] #move the last column to the middle
df_csv.to_csv("modified.csv", index=False) #save your file in form of csv
df_csv.to_excel("modified.xlsx",index=False) #save the data in form of excel
df_csv.to_csv("modified.txt",index=False,sep='\t') #save the data in form of txt
print(df_csv.loc[(df_csv['Type 1']=='Grass')&(df_csv['Type 2']=='Poison')]) #print out all the rows with type1 grass and type2 poison
print(df_csv.loc[(df_csv['Type 1']=='Grass')|(df_csv['Type 2']=='Poison')]) #print out all the rows with type1 grass or type2 poison
print(df_csv.loc[(df_csv['Type 1']=='Grass')&(df_csv['Type 2']=='Poison')&(df_csv['HP']>70)]) #print out all the rows with type1 grass and type2 poison and HP greater than 70
new_dt=df_csv.loc[(df_csv['Type 1']=='Grass')&(df_csv['Type 2']=='Poison')]
new_dt.reset_index(drop=True, inplace=True) #drop the old index and reset new index
print(df_csv.loc[df_csv['Name'].str.contains('Mega')]) #print out the rows with names containing Mega
print(df_csv.loc[~df_csv['Name'].str.contains('Mega')]) #print out the rows without names containing Mega
print(df_csv.loc[df_csv["Type 1"].str.contains('Fire|Grass',regex=True)]) #print out all rows with type1 Fire or Grass
print(df_csv.loc[df_csv["Type 1"].str.contains('fire|grass',flags=re.I,regex=True)]) #not case-sensitive
print(df_csv.loc[df_csv['Name'].str.contains('^pi[a-z]*',flags=re.I, regex=True)]) #print out all rows with names beginning with pi
df_csv.loc[df_csv["Type 1"]=="Fire",'Type 1']="Flamer" #change all type1 Fire into Flamer
df_csv.loc[df_csv["Type 1"]=="Fire",'Legendary']=True #set all Legendary equals True if the type1 is Fire 
df_csv.loc[df_csv["Type 1"]=="Fire",['Legendary','Generation']]=[True,4]
print(df_csv.groupby(["Type 1"]).mean()) #give the average values of other columns based on different type 1
print(df_csv.groupby(["Type 1"]).mean().sort_values('Defense',ascending=False))
print(df_csv.groupby(["Type 1"]).sum())
print(df_csv.groupby(["Type 1"]).count())
print(df_csv.groupby(["Type 1"]).count()['#']) #get the count of specific column
