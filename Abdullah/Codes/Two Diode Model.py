from scipy.special import lambertw
from scipy.constants import e, Boltzmann
from numpy import exp, linspace, log
from pylab import plot, show, xlabel, ylabel

# Parameters
Iph = 4.85e-5 # Amps
I01 = 1.5e-5 # Amps
I02 = 2.4e-7 # Amps
n1 = 2.4
n2 = 9.5
Rs = 0 # Ohms
Rp1 = 1e8 # Ohms
Rp2 = 4.6e4 # Ohms
T = 300 # K

# Injected Current Values
I = linspace(-5.5e-5,0.1e-5,5)

# Voltage calculation (method 1)
z1 = (e/(n1*Boltzmann*T)) * I01*Rp1 * exp( (e/(n1*Boltzmann*T)) * Rp1 * (I+Iph+I01))
w1 = lambertw(z1,k=0,tol=1e-15)

z2 = e/(n2*Boltzmann*T)*I02*Rp2*exp(-e/(n2*Boltzmann*T)*Rp2*(I-I02))
w2 = lambertw(z2,k=0,tol=1e-15)

Vf = (I+Iph+I01)*Rp1 \
    - (n1*Boltzmann*T)/e*w1 \
    + (n2*Boltzmann*T)/e*w2 \
    + (I-I02)*Rp2 + I*Rs

# Ploting
plot(Vf,I,"b-")
xlabel('V (volts)')
ylabel('I (amps)')
show()

# Voltage calculation (method 2)
x1 = log(e/(n1*Boltzmann*T)*I01*Rp1)+e/(n1*Boltzmann*T)*Rp1*(I+Iph+I01)
g1 = log(lambertw(exp(x1),k=0,tol=1e-15))

x2 = log(e/(n2*Boltzmann*T)*I01*Rp2)-e/(n2*Boltzmann*T)*Rp2*(I-I02)
g2 = log(lambertw(exp(x2),k=0,tol=1e-15))

Vg = I*Rs \
    + (n1*Boltzmann*T)/e*g1 - (n2*Boltzmann*T)/e*g2 \
    - (n1*Boltzmann*T)/e*log(e/(n1*Boltzmann*T)*I01*Rp1) \
    + (n2*Boltzmann*T)/e*log(e/(n2*Boltzmann*T)*I02*Rp2)

# Ploting
plot(Vg,I,"b-")
xlabel('V (volts)')
ylabel('I (amps)')
show()


