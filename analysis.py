import pandas as pd
df=pd.read_csv("sales.csv")
total_sales=df["sales"].sum()
region_sales=df.groupby("region")['sales'].sum().reset.index()
product_sales=df.groupby('product')["sales"].sum().idxmax()
print(total_sales)
print(region_sales)
print(product_sales)

region_sales.to_csv("region_sales.csv", ascending=False)