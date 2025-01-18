
def nhap_matran(row, col):
    
    if (row > 0) & (col > 0):
        m = row
        n = col
        matran = [] # ma tran rong
        for i in range(m):
            # nhap vao tung hang
            row =[]
        for j in range (n):
            x= int(input(" phan tu " +str(i) +", "+str(j)+ " ="))
            row = row + [x] # them phan tu x vao cuoi dong 
            matran.append(row) # them tung dong vao mang tran
        return matran
    else:
        return None
    
def hienthimatran(Matrix, row, clo):
    for i in range(row):
        for j in range (col):
            print(str(Matrix[i][j])+", ", end=' ')
            

if __name__ == "__main__":
    m = int(input(" so hang "))
    n = int(input(" so cot "))
    matran = nhap_matran(row=m,col=n)
    print(" ma tran da nhap ")
    # print(matran)
    hienthimatran(matran,m,n)


        
                
    