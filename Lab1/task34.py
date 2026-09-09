import pandas as pd
import numpy as np
data={
    "name":["Zain","Noor","Aisha","Ghani","Mehdi"],
    "scores":[98,np.nan,np.nan,78,56]
}
df=pd.DataFrame(data)
df['scores']=df['scores'].fillna(df['scores'].mean()).round(2)
print(df)