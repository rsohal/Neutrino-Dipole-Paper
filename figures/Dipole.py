import numpy as np
import matplotlib
matplotlib.use("PDF")
import pylab as py

figdir = "./figures/Dipole/"
dir = figdir+"Placeholder_Data/"

hratio = 0.85
fs     = 11
fs2    = 10
fig_width_pt  = 350.
inches_per_pt = 1. / 72.27
fig_width     = fig_width_pt * inches_per_pt
fig_height    = fig_width * hratio  #* golden_mean
fig_size      = [fig_width, fig_height]
params        = {'backend': 'ps', 'axes.labelsize': fs, 'text.fontsize': fs, \
                'legend.fontsize': fs2, 'xtick.labelsize': fs, 'ytick.labelsize': fs, \
                'text.usetex': True, 'figure.figsize': fig_size}
dip1 = np.genfromtxt(dir+'0.2ev_dmnu_velbin1_dipo.dat', skip_header=9)
dip2 = np.genfromtxt(dir+'0.2ev_dmnu_velbin2_dipo.dat', skip_header=9)
dip3 = np.genfromtxt(dir+'0.2ev_dmnu_velbin3_dipo.dat', skip_header=9)
dip4 = np.genfromtxt(dir+'0.2ev_dmnu_velbin4_dipo.dat', skip_header=9)

py.rcParams.update(params)
py.figure(1)
py.clf()
py.loglog(dip1[:,0], dip1[:,1], label=r"$0-5214 km/s$")
py.loglog(dip2[:,0], dip2[:,1], label=r"$5214-7853 km/s$")
py.loglog(dip3[:,0], dip3[:,1], label=r"$7853-11280 km/s$")
py.loglog(dip4[:,0], dip4[:,1], label=r"$>11280 km/s$")

py.xlabel(r"$r\ [{\rm Mpc}/h]$")
py.ylabel(r"Dipole Correlation")
lg = py.legend(loc="lower left", fancybox=True, numpoints=1)
lg.draw_frame(False)

py.savefig(figdir+'dipolefig.pdf')
