import cmath
import math

def cardinal_to_xyz(cardinal_num):
    total = cardinal_num - 1
    nz = int(math.sqrt(total))
    nt = total - nz**2
    ny = int(math.sqrt(nt))
    nx = nt - ny**2
    return nx, ny, nz

def psibox(x, cardinal_num, boxl):

    nx, ny, nz = cardinal_to_xyz(cardinal_num)
    k = 2*math.pi/L * cmath.sqrt(nx**2 + ny**2 + nz**2)
    return cmath.exp(1j*k*x)
