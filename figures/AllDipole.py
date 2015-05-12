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

xmin=0
xmax=1e2
ymin=1e-4
ymax=1e-1

dipsim = np.genfromtxt(dir+'sim/dipole_0.dat')#, skip_header=9)
diprdm = np.genfromtxt(dir+'rdm/dipole_0.dat')#, skip_header=9)
#diprha = np.genfromtxt(dir+'rha/dipole_0.dat')#, skip_header=9)

py.rcParams.update(params)
py.figure(1)
py.clf()

py.loglog(dipsim[:,0], dipsim[:,1], 'c', label=r"${\rm Sim}$")
py.loglog(diprdm[:,0], diprdm[:,1], 'c--', label=r"${\rm Rec DM}$")


py.xlabel(r"$r\ [{\rm Mpc}/h]$")
#py.axes().set_xlim((xmin,xmax))
py.ylabel(r'${\rm Dipole \, Correlation}$')
#py.axes().set_ylim((ymin,ymax))

py.axes().set_xlim((xmin, xmax))
py.axes().set_ylim((ymin, ymax))


lg = py.legend(loc="upper right", fancybox=True, numpoints=1)
lg.draw_frame(False)

py.savefig(figdir+'alldipolefig.pdf')
