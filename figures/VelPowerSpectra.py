import numpy as np
import matplotlib
matplotlib.use("PDF")
import pylab as py

figdir = "./figures/VelPowerSpectra/"
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

rdmnunu1 = np.genfromtxt(dir+'0.000ngp_recdm_1tf_nunu.dat')
rdmnunu2 = np.genfromtxt(dir+'0.000ngp_recdm_2tf_nunu.dat')
rdmnunu3 = np.genfromtxt(dir+'0.000ngp_recdm_3tf_nunu.dat')
rdmnunu4 = np.genfromtxt(dir+'0.000ngp_recdm_4tf_nunu.dat')
totnunu1 = np.genfromtxt(dir+'0.000ngp_totvel_1_nunu.dat')
totnunu2 = np.genfromtxt(dir+'0.000ngp_totvel_2_nunu.dat')
totnunu3 = np.genfromtxt(dir+'0.000ngp_totvel_3_nunu.dat')
totnunu4 = np.genfromtxt(dir+'0.000ngp_totvel_4_nunu.dat')

py.rcParams.update(params)
py.figure(1)
py.clf()
py.loglog(rdmnunu1[:,0], rdmnunu1[:,1], 'r', label=r"$0-5214 km/s$")
py.loglog(rdmnunu2[:,0], rdmnunu2[:,1], 'b', label=r"$5214-7853 km/s$")
py.loglog(rdmnunu3[:,0], rdmnunu3[:,1], 'g', label=r"$7853-11280 km/s$")
py.loglog(rdmnunu4[:,0], rdmnunu4[:,1], color='black', ls='--', label=r"$>11280 km/s$")
py.loglog(totnunu1[:,0], totnunu1[:,1], 'r--')
py.loglog(totnunu2[:,0], totnunu2[:,1], 'b--')
py.loglog(totnunu3[:,0], totnunu3[:,1], 'g--')
py.loglog(totnunu4[:,0], totnunu4[:,1], color='black')

py.xlabel(r"$k\ [h/{\rm Mpc}]$")
py.ylabel(r"$\Delta_{vv}^2$")
lg = py.legend(loc="lower left", fancybox=True, numpoints=1)
lg.draw_frame(False)

py.savefig(figdir+'velpower.pdf')