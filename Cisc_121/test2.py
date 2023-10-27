def counting(arr,exp):
    n = len(arr)
    # The output array elements that will have sorted arr
    output = [0]` * (n)
    # initialize count array as 0
    count = [0] * (10)

    for i in arr:
        count[(i%(exp*(10)))//exp]+=1

    for i in range(1,len(count)):
        count[i]+=count[i-1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):

  max1 = max(arr)
  exp = 1
  while max1 / exp >= 1:
      counting(arr, exp)
      exp *= 10

  return arr


a=[10000,120,1223,5,621,199]
print(radixSort(a))
