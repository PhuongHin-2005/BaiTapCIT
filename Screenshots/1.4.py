def thetichhinhtron(r):
    v = (4*r*r*r)/3
    return v

def dientichhinhtron(r):
    s = r*r*3,14
    return s

r = int(input("nhap ban kinh hinh tròn"))
the_tich = thetichhinhtron(r)
print("the tich hinh tron=%f"%(the_tich))   

