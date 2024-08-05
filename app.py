import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



dataset=pd.read_csv("Data.csv")

independent_variables_x= dataset.iloc[:,:-1].values
dependent_variables_y = dataset.iloc[:, -1].values

print(independent_variables_x)
print(dependent_variables_y)






# # x=(x-x_min)/(x_max-x_min)   


# salaries=[70_000,60_000,52_000]
# age=[45,44,40]

# def normalize_data(data):
#  for person in data:
#    print((person-min(data))/(max(data)-min(data)))


# normalize_data(salaries)
# normalize_data(age)
   
   