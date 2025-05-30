import pandas as pd 

df_product = pd.DataFrame({
    'product_id': [1,2,3],
    'product' : ['Apple','Banana','Orange']
})

df_sales = pd.DataFrame({
    'product' : ['Apple','Banana','Orange','Apple'],
    'Quantity': [10,15,7,5]
})

df_product.loc[len(df_product)] = [4,'Pineapple']
merged_in = pd.merge(df_sales,df_product, how= 'inner')

merged_left = pd.merge(df_sales,df_product, how= 'left')


merged_out= pd.merge(df_sales,df_product, how= 'outer')
print(merged_out)