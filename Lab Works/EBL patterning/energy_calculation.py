# Parameters
d_piezo=3000e-12 #3000 pm/V
Vin=50e-3 #50mV
Y=250e9 #250e9 Pa
area=1.5e3*3e3

for t_piezo in range(25,101,10):
    e_piezo=d_piezo*(Vin/(t_piezo*1e-9))
    stress=Y*e_piezo
    for t_magneto in range (1,20,0.3):
        energy=(3/2)*150e-6*area*t_magneto
