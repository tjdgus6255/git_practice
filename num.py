import numpy as np

list_A = [1, 2, 3]
list_B = [1, 1, 1]
list_C = list_A + list_B
print(list_C)

np_list_A = np.array(list_A)
np_list_B = np.array(list_B, dtype=float)
np_list_C = np_list_A + np_list_B
print(np_list_C.shape)

arr = np.array(range(1,9))
# print(arr.shape)
# print(arr)
arr2 = np.reshape(arr, [2,2,2])
print(arr2.shape)
print(arr2)

import numpy as np

arr = np.array