import cmath
import math


def cardinal(cardinal_num):
    sum = cardinal_num - 1
    nz = int(math.sqrt(sum))
    nt = sum - nz ** 2
    ny = int(math.sqrt(nt))
    nx = nt - ny ** 2
    return nx, ny, nz


def psibox(x, cardinal_num, L):
    nx, ny, nz = cardinal(cardinal_num)
    k = 2 * math.pi / L * cmath.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
    return cmath.exp(1j * k * x)
