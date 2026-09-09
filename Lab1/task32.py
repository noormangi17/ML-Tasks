import pandas as pd
scores={
    "Student":["Noor","Shabab","Zain","Dua","Faryal","Sajni","Suhana","Sejul","Shifa","Alia"],
    "English":[98,87,54,67,87,88,75,89,96,93],
    "Math":[73,66,87,45,67,98,43,56,78,98],
    "Science":[43,44,76,78,98,76,34,54,67,89]
}
df=pd.DataFrame(scores)
df['Average']=df.groupby('Student')[["English","Math","Science"]].mean().mean(axis=1).round(2).values
print(df)