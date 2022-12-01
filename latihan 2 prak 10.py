print("Program sebuah fungsi sorting berdasarkan metode bubble sort menggunakan konsep rekursif")
print("=================================================================================")
def tukar(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    
def bubbleSort(A, n):
    for i in range(n-1):
        if A[i] > A[i + 1]:
            tukar(A, i, i + 1)
    if n - 1 > 1:
        bubbleSort(A, n - 1)
        
print("List yang sudah disorting")        
A = [-2, 5, 28, 11, 88, 3, 69]
bubbleSort(A, len(A))
print("")
print(A)