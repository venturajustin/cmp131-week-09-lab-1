#Justin Ventura CMP131 week 9 11/12/26
def kinenergy (m,v):
    ke = 0.5*m*v*v
    return ke 

def display (ke):
   print("",ke)

def main():
   m = float(input(""))
   v = float(input(""))
   ke = kinenergy(m,v)
   display (ke)
main()

