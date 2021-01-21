import numpy as np
import pandas as pd

array1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
array2 = pd.Series([4, 5, 6], index=['B', 'C', 'D'])

array = array1.add(array2, fill_value=0)
print(array)