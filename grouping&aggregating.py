import pandas as pd

data = { 'product': ['Apple', 'Banana','Orange','Apple','Orange','Apple','Orange'],
        "price" : [0.3,0.5,0.7,0.3,0.7,0.3,0.7],
        "Quantity": [10,12,3,5,7,12,8]
}

df = pd.DataFrame(data)


t_price = df.groupby('product')['price'].sum()
print(t_price)

max_qty = df.groupby('product')['Quantity'].max()
print(max_qty)
summury = df.groupby('product').agg({
    'price':['sum','mean']
    
})
print(summury)
