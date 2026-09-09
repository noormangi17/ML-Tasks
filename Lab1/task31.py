import pandas as pd
data={
    "name":["Shampoo","Chips","Moisturizer","Soap","Oil"],
    "price":[500,100,400,300,600],
    "quantity":[2,10,4,5,3]
}
df=pd.DataFrame(data)
df["total"]=df['price']*df['quantity']
print(df)