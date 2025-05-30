import pandas as pd

# data_read = pd.read_csv("sales_data_sample.csv", encoding= "latin1")

# print(data_read)

# data_read_excel = pd.read_excel("SampleSuperstore.xlsx")


# print(data_read_excel.info())

data = {
        "name" : ["kul",'karan','Anant'],
        "age": [33,33,1],
        "blood_grp" : ["A+",'o+',"o+"],
        "salary": [60000,140000,0]

}

dataframe = pd.DataFrame(data)


dataframe["bouns"] = dataframe['salary']*0.1
print(dataframe)

dataframe.insert(0,"id",[1,2,3])
print(dataframe)

dataframe.loc[1,"age"] = 34
print(dataframe)