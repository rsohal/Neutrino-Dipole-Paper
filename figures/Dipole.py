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

#dip1 = np.genfromtxt(dir+'0.2ev_dmnu_velbin1_dipo.dat', skip_header=9)
#dip2 = np.genfromtxt(dir+'0.2ev_dmnu_velbin2_dipo.dat', skip_header=9)
#dip3 = np.genfromtxt(dir+'0.2ev_dmnu_velbin3_dipo.dat', skip_header=9)
#dip4 = np.genfromtxt(dir+'0.2ev_dmnu_velbin4_dipo.dat', skip_header=9)

dipsim1 = np.genfromtxt(dir+'sim/dipole_1tf_0.dat')#, skip_header=9)
dipsim2 = np.genfromtxt(dir+'sim/dipole_2tf_0.dat')#, skip_header=9)
dipsim3 = np.genfromtxt(dir+'sim/dipole_3tf_0.dat')#, skip_header=9)
dipsim4 = np.genfromtxt(dir+'sim/dipole_4tf_0.dat')#, skip_header=9)

diprdm1 = np.genfromtxt(dir+'rdm/dipole_1tf_0.dat')#, skip_header=9)
diprdm2 = np.genfromtxt(dir+'rdm/dipole_2tf_0.dat')#, skip_header=9)
diprdm3 = np.genfromtxt(dir+'rdm/dipole_3tf_0.dat')#, skip_header=9)
diprdm4 = np.genfromtxt(dir+'rdm/dipole_4tf_0.dat')#, skip_header=9)

diprha1 = np.genfromtxt(dir+'rha/dipole_1tf_0.dat')#, skip_header=9)
diprha2 = np.genfromtxt(dir+'rha/dipole_2tf_0.dat')#, skip_header=9)
diprha3 = np.genfromtxt(dir+'rha/dipole_3tf_0.dat')#, skip_header=9)
diprha4 = np.genfromtxt(dir+'rha/dipole_4tf_0.dat')#, skip_header=9)


py.rcParams.update(params)
py.figure(1)
py.clf()
py.loglog(dipsim1[:,0], dipsim1[:,1], 'r', label=r"$0-5214 km/s$")
py.loglog(dipsim2[:,0], dipsim2[:,1], 'b', label=r"$5214-7853 km/s$")
py.loglog(dipsim3[:,0], dipsim3[:,1], 'g', label=r"$7853-11280 km/s$")
py.loglog(dipsim4[:,0], dipsim4[:,1], 'k', label=r"$>11280 km/s$")

py.loglog(diprdm1[:,0], diprdm1[:,1], 'r--')
py.loglog(diprdm2[:,0], diprdm2[:,1], 'b--')
py.loglog(diprdm3[:,0], diprdm3[:,1], 'g--')
py.loglog(diprdm4[:,0], diprdm4[:,1], 'k--')

py.loglog(diprha1[:,0], diprha1[:,1], 'r-.')
py.loglog(diprha2[:,0], diprha2[:,1], 'b-.')
py.loglog(diprha3[:,0], diprha3[:,1], 'g-.')
py.loglog(diprha4[:,0], diprha4[:,1], 'k-.')


py.xlabel(r"$r\ [{\rm Mpc}/h]$")
py.axes().set_xlim((xmin,xmax))
py.ylabel(r"Dipole Correlation")
py.axes().set_ylim((ymin,ymax))
lg = py.legend(loc="upper right", fancybox=True, numpoints=1)
lg.draw_frame(False)

py.savefig(figdir+'dipolefig.pdf')
