import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('monthly_expenses.csv')
grouped=df.groupby('category')['expense'].sum()
grouped.plot(kind='pie',autopct="%1.1f%%")
plt.show()