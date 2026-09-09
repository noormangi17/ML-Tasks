import pandas as pd
data={
    "date":["2026-08-11","2026-08-12","2026-08-01","2026-08-09"],
    "sales":[400,500,300,800]
}
df=pd.DataFrame(data)
df['date']=pd.to_datetime(df['date'])
df=df.sort_values('date')
import matplotlib.pyplot as plt
df.plot(x='date',y='sales')
plt.show()