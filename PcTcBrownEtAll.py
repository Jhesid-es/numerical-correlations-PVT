
def ygHC(yg,yn2,yco2,yh2s):
    ygHCcorr: float = (yg-0.967*yn2-1.52*yco2-1.18*yh2s)/(1-yn2-yco2-yh2s)
    return ygHCcorr
#Gas Natural
def pscHC_GN(ygHC):
    pscHC_GN: float= 677+15*ygHC-37.5*ygHC**2
    return pscHC_GN
def tscHC_GN(ygHC):
    tscHC_GN = 168 +325*ygHC-12.5*ygHC**2
    return tscHC_GN
#Gas Condensado
def pscHC_GC(ygHC):
    pscHC_GC= 706+51.7*ygHC-11.1*ygHC**2
    return pscHC_GC
def tscHC_GC(ygHC):
    tscHC_GC = 187 +330*ygHC-71.5*ygHC**2
    return tscHC_GC
