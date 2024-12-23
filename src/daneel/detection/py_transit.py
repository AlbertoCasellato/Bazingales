import batman
import numpy as np
import matplotlib.pyplot as plt

data_light_curve = np.genfromtxt('ExoCTK_results.txt',usecols=[8,10],skip_header=2)

c1 = np.mean(data_light_curve[:,0])
c2 = np.mean(data_light_curve[:,1])

params = batman.TransitParams()
params.t0 = 0.                            #  #time of inferior conjunction
params.per = 3.21                           #orbital period
params.rp = 0.7                             #planet radius (in units of stellar radii)
params.a = 0.0384 * 149597870707/6957e8     #semi-major axis (in units of stellar radii)    1 AU = 149597870707 m ; 1 Rsun = 6957e8 m
params.inc = 90.                          #  #orbital inclination (in degrees)
params.ecc = 0.                           #  #eccentricity
params.w = 90.                            #  #longitude of periastron (in degrees)
params.u = [c1, c2]                         #limb darkening coefficients [u1, u2]
params.limb_dark = "quadratic"              #limb darkening model

t = np.linspace(-1.7, 1.7, 100)
m = batman.TransitModel(params, t)          #initializes model
flux = m.light_curve(params)                #calculates light curve

# plot
plt.plot(t, flux)
plt.xlabel("Time from central transit")
plt.ylabel("Relative flux")
plt.savefig('HAT-P-12b_assignment1_taskF.png')
# plt.show()