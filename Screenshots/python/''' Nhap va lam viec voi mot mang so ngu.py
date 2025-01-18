''' Nhap va lam viec voi mot mang so nguyen'''

# nhap mang so nguyen co n phan tu 
def nhapmang():
    n = int(input(" so phan tu cua mang "))
    int_array = []
    for i in range(n):
        obj_i = int(input(" nhap phan tu thu "+ str(i)+": "))
        int_array.append(obj_i)
    return int_array



if __name__ == "__main__":
   mangsn = nhapmang() 
print(" mang da nhap ")
print(mangsn)
   
