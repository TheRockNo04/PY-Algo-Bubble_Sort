import random
A = [2,10,8,6,13,5]#[x for x in range(1,101)]

sorted_element_index = 0
for x in A:
    sorted_element_index += 1
    for i in range(sorted_element_index, len(A)):
        if A[i] > A[i+1]:
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
print(A)


