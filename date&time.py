import pandas as pd 

data = {
    'product' : ['Apple','Banana','Orange','Apple','Banana'],
    'Quantity': [10,5,6,7,8],
    "Sales_date": ['2024-05-01','2024-06-02','2024-07-03','2024-08-04','2024-11-05']          
}

df = pd.DataFrame(data)


df['Sales_date'] = pd.to_datetime(df['Sales_date'])

df['month'] = df['Sales_date'].dt.month
df['day'] = df['Sales_date'].dt.day
df['weekday'] = df['Sales_date'].dt.weekday

print(df)

nov_sales = df[df['Sales_date'].dt.month ==11]
print(nov_sales)

month_sales = df.groupby(df['Sales_date'].dt.month)['Quantity'].sum()
print(month_sales)