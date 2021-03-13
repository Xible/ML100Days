import numpy as np

# 產生一個 30 個元素的一維陣列
array1 = np.array(range(30))
print("\n一開始的一維陣列\n", array1)

# 將上述陣列重新塑形成 5*6 的二維陣列
trans_array = np.reshape(array1, (5,6), order='F')
print("\n重塑成 5*6 的二維陣列\n", trans_array)

# 將該二維陣列中的值除 6，並找出餘 1 的索引值（預期會有 2 個陣列)
check_array = np.where(trans_array %6 == 1)
print("\n索引值為 : \n", check_array)