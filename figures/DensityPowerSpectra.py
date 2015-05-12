import numpy as np
import matplotlib
matplotlib.use("PDF")
import pylab as py

figdir = "./figures/DensityPowerSpectra/"
dir = figdir+"Placeholder_Data/"

hratio = 0.85
fs     = 11
fs2    = 10
fig_width_pt  = 400.
inches_per_pt = 1. / 72.27
fig_width     = fig_width_pt * inches_per_pt
fig_height    = fig_width * hratio  #* golden_mean
fig_size      = [fig_width, fig_height]
params        = {'backend': 'ps', 'axes.labelsize': fs, 'text.fontsize': fs, \
                'legend.fontsize': fs2, 'xtick.labelsize': fs, 'ytick.labelsize': fs, \
                'text.usetex': True, 'figure.figsize': fig_size}
xmin= 1e-2
xmax= 1e1
ymin= 1e-4
ymax= 0.5e0

nunu1 = np.genfromtxt(dir+'0.000ngpps_1_nunu.dat')
nunu2 = np.genfromtxt(dir+'0.000ngpps_2_nunu.dat')
nunu3 = np.genfromtxt(dir+'0.000ngpps_3_nunu.dat')
nunu4 = np.genfromtxt(dir+'0.000ngpps_4_nunu.dat')
nunutf = np.genfromtxt(dir+'mom_default_pk_th_all.dat')

py.rcParams.update(params)
py.figure(1)
py.clf()
py.loglog(nunu1[:,0], nunu1[:,1], 'r', label=r"$Q_1$")#label=r"$0-5214 km/s$")
py.loglog(nunu2[:,0], nunu2[:,1], 'b', label=r"$Q_2$") #label=r"$5214-7853 km/s$")
py.loglog(nunu3[:,0], nunu3[:,1], 'g', label=r"$Q_3$") #label=r"$7853-11280 km/s$")
py.loglog(nunu4[:,0], nunu4[:,1], 'k', label=r"$Q_4$") #label=r"$>11280 km/s$")
py.loglog(nunutf[:,0], nunutf[:,2], 'r--')
py.loglog(nunutf[:,0], nunutf[:,3], 'b--')
py.loglog(nunutf[:,0], nunutf[:,4], 'g--')
py.loglog(nunutf[:,0], nunutf[:,5], 'k--')

py.xlabel(r"$k\ [h/{\rm Mpc}]$")
py.axes().set_xlim((xmin,xmax))
py.ylabel(r"$\Delta_{vv}^2$")
py.axes().set_ylim((ymin,ymax))
lg = py.legend(loc="lower left", fancybox=True, numpoints=1)
lg.draw_frame(False)

py.savefig(figdir+'denpower.pdf')
