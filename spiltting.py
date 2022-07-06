
digits = [2,3,2]

def plusOne(digits):
    s = ""
    for i in digits:
        s += str(i)
    q = int(s)+1
    q = list(str(q))
    q = [int(i) for i in q]
    return q
    

print(plusOne(digits))



board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

def isValidSudoku(board):
    # row = set()
    # column = set()
    row_list = []
    column_list = []
    for i in board:
        row = set()
        row_list = []
        for num in i:
            if num != '.':
                row.add(num)
                row_list.append(num)
        print(row_list)
        print(row)
        if len(row) == len(row_list):
            return True
        else:
            return False
    
    
    
    
print(isValidSudoku(board))


matrix = [[1,2,3],[4,5,6],[7,8,9]]
def rotate(matrix):
    m_copy = matrix.copy()
    print(m_copy)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            a = matrix[j][i]
            matrix[i].append(a)
            
    for i in range(len(m_copy)):
        a = len(m_copy[i])//2
        print(a)
        matrix[i][:a] = []
        
    print(m_copy)
    return matrix
            
            
print(rotate(matrix))