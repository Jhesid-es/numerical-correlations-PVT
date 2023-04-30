from PcTcBrownEtAll import pscHC_GN, ygHC
ge: float = float(input('Ingresa el valor de gravedad especifica: '))
correction: bool = True if str(input('Quiere realizar correcion por N2, CO2, y H2S? (Si/No)')) == 'Si' else False
if (correction):
    yn2: float = float(input('Ingrese fraccion de N2: '))
    yco2: float = float(input('Ingrese fraccion de CO2: '))
    yh2s: float = float(input('Ingrese fraccion de H2S: '))
    ge = ygHC(ge,yn2,yco2,yh2s)
    print(f'La presion psudo-critica es: {pscHC_GN(ge)} y la nueva gravedad especifica es {ge}')
else:
    print('La presion psudo-critica es: ', pscHC_GN(ge))

