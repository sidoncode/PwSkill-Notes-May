import numpy as np

x = np.array([1,2,3])
y = np.array([4,5,6])

print(np.add(x,y))
print(np.multiply(x,y))
print(np.dot(x,y))
print(np.exp(x))
print(np.sqrt(y))

arr = np.array(     
    [
        [1,2],
        [3,4]     
    ]
)

print(np.mean(arr))       # 2.5
print(np.std(arr))        # Standard deviation
print(np.min(arr))        # 1
print(np.max(arr))        # 4
print(np.sum(arr, axis=0))# Sum by columns: [4, 6]
print(np.sum(arr, axis=1))# Sum by rows: [3, 7]