matrix = []
while True:
    a = input().split()
    if a == ['end']:
        break
    else:
        matrix.append(a)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if 0 <= i - 1 < len(matrix):
            i1 = i - 1            
            if 0 <= i + 1 < len(matrix):
                i2 = i + 1                
                if 0 <= j - 1 < len(matrix[i]):
                    i3 = j - 1                     
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
                else:
                    i3 = len(matrix[i]) - 1                      
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
            else:
                i2 = 0                
                if 0 <= j - 1 < len(matrix[i]):
                    i3 = j - 1                    
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
                else:
                    i3 = len(matrix[i]) - 1                    
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
        else:
            i1 = len(matrix) - 1
            if 0 <= i + 1 < len(matrix):
                i2 = i + 1                
                if 0 <= j - 1 < len(matrix[i]):
                    i3 = j - 1                    
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
                else:
                    i3 = len(matrix[i]) - 1
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
            else:
                i2 = 0                
                if 0 <= j - 1 < len(matrix[i]):
                    i3 = j - 1                    
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
                else:
                    i3 = len(matrix[i]) - 1                    
                    if 0 <= j + 1 < len(matrix[i]):
                        i4 = j + 1
                    else:
                        i4 = 0
        
        num = int(matrix[i1][j]) + int(matrix[i2][j]) + int(matrix[i][i3]) + int(matrix[i][i4])
        print(num, end=' ')
    print()