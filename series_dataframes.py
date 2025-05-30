import pandas as pd

odd_numbers = pd.Series([1,3,5,7,9])


data = { "product": ["Apple","Banana","Orange"],
        "price": [0.5,0.3,0.7],
        "quantity": [10,15,7]
}

df = pd.DataFrame(data)


# print(df[['quantity', 'price']])

# print(df.iloc[2])

ex = df[df['price']<0.6]


df['discount'] = df['price'] - 0.05

df['final_price'] = df['price'] - df['discount']


# df.drop('discount',axis=1,inplace=True)

df.sort_values(by='final_price', ascending=False, inplace=True)

df.rename(columns={'quantity': 'stock'}, inplace=True)
print(df)

df.reset_index(drop=True,inplace=True)
print(df)