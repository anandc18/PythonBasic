import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np
nums = [1, 2, 3, 4,5]
s = pd.Series(nums)
print(s)

s = pd.Series(np.linspace(5, 20, 10)) # linspace(starting, end, items)
print(s)

data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
