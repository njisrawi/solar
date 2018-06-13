from scipy.special import lambertw
from scipy.constants import e, k
from numpy import exp, linspace, log
from pylab import plot, show, xlabel, ylabel

# Constants
q = e
kB = k

# Conditions (Blue solar cell)
Iph = 0.1023 # Amps
I0 = 0.1036E-6 # Amps
n = 1.5019
Rs = 0.06826 # Ohms
Rp = 1000 # Ohms
T = 300 # K

# Current
I = linspace(-0.11,0,1000)

# Voltage calculation (method 1)
z = ( q/(n*kB*T) ) * I0 * Rp * exp(  (q/(n*kB*T)) * Rp * (I + Iph + I0)  )
w = lambertw(z,0)
V1 = I*Rs
V2 = (I+Iph+I0)*Rp
V3 = -((n*kB*T)/q) * w
Vf = V1 + V2 + V3

# Voltage calculation (method 2)
x = log( (q/(n*kB*T)) * I0 * Rp ) + (q/(n*kB*T)) * Rp * (I+Iph+I0)
g = log(lambertw(exp(x),0))
V1 = I*Rs
V2 = ((n*kB*T)/q) * g
V3 = -((n*kB*T)/q) * log( (q/(n*kB*T)) * I0 * Rp )
Vg = V1 + V2 + V3

# Ploting
plot(Vf,I,"r-")
xlabel('V (volts)')
ylabel('I (amps)')
show()
plot(Vg,I,"b-")
xlabel('V (volts)')
ylabel('I (amps)')
show()

# Conditions (Grey solar cell)
Iph = 0.5610 # Amps
I0 = 5.514E-6 # Amps
n = 1.7225
Rs = 0.07769 # Ohms
Rp = 25.9 # Ohms
T = 307 # K

# Current
I = linspace(-0.6,0,1000)

# Voltage calculation (method 1)
z = ( q/(n*kB*T) ) * I0 * Rp * exp(  (q/(n*kB*T)) * Rp * (I + Iph + I0)  )
w = lambertw(z,0)
V1 = I*Rs
V2 = (I+Iph+I0)*Rp
V3 = -((n*kB*T)/q) * w
Vf = V1 + V2 + V3

# Voltage calculation (method 2)
x = log( (q/(n*kB*T)) * I0 * Rp ) + (q/(n*kB*T)) * Rp * (I+Iph+I0)
g = log(lambertw(exp(x),0))
V1 = I*Rs
V2 = ((n*kB*T)/q) * g
V3 = -((n*kB*T)/q) * log( (q/(n*kB*T)) * I0 * Rp )
Vg = V1 + V2 + V3

# Ploting
plot(Vf,I,"r-")
xlabel('V (volts)')
ylabel('I (amps)')
show()
plot(Vg,I,"b-")
xlabel('V (volts)')
ylabel('I (amps)')
show()