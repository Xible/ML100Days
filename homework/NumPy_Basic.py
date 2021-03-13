import numpy as np

## 等差產生一個有 21 的元素的陣列 (從0開始，直到 20)
np_List = np.arange(21)
print("np_List play : " ,np_List)

## 從上述產生的 List 中，挑選為 2 倍數的元素
TakeEven = np_List[0::2]
print("np_List even number : ",TakeEven)

## 從上述產生的 List 中，挑選為 3 倍數的元素
TakeThree = np_List[3::3]
print("np_List even number : ",TakeThree)

print ("\n#### 以下為自主練習產生等差陣列用法")

## 等差產生一個從 5 開始，到 20 結束的陣列 (元素並不會包含到 20)
testArange = np.arange(5,20,3) #依照起始值、結束值、間隔值做等差的數字序列
print("Arange List : ", testArange)

## 等差產生一個從 5 開始，到 20 結束的陣列 (等差的值是由產生的 num 數量去計算決定)
testLinspace = np.linspace(5, 20, num=5, endpoint=True, dtype=int) #依照起始值、結束值、陣列數量、是否包含結束值、陣列元素型態做等差的數字序列
print("Linspace List : ", testLinspace)