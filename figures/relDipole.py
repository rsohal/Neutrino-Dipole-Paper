import numpy as np
import matplotlib
matplotlib.use("PDF")
import pylab as py

figdir = "./figures/Dipole/"
dir = figdir+"Placeholder_Data/"

hratio = 0.85
golden_mean = 1.618
fs     = 11
fs2    = 10
fig_width_pt  = 350.
inches_per_pt = 1. / 72.27
fig_width     = fig_width_pt * inches_per_pt
fig_height    = fig_width * hratio  * golden_mean
fig_size      = [fig_width, fig_height]
params        = {'backend': 'ps', 'axes.labelsize': fs, 'text.fontsize': fs, \
                'legend.fontsize': fs2, 'xtick.labelsize': fs, 'ytick.labelsize': fs, \
                'text.usetex': True, 'figure.figsize': fig_size}

xmin=0
xmax=1e2
ymin=1e-4
ymax=8e-2#1e-1

#dip1 = np.genfromtxt(dir+'0.2ev_dmnu_velbin1_dipo.dat', skip_header=9)
#dip2 = np.genfromtxt(dir+'0.2ev_dmnu_velbin2_dipo.dat', skip_header=9)
#dip3 = np.genfromtxt(dir+'0.2ev_dmnu_velbin3_dipo.dat', skip_header=9)
#dip4 = np.genfromtxt(dir+'0.2ev_dmnu_velbin4_dipo.dat', skip_header=9)

dipsim = np.genfromtxt(dir+'sim/dipole_0.dat')#, skip_header=9)
dipsim1 = np.genfromtxt(dir+'sim/dipole_1tf_0.dat')#, skip_header=9)
dipsim2 = np.genfromtxt(dir+'sim/dipole_2tf_0.dat')#, skip_header=9)
dipsim3 = np.genfromtxt(dir+'sim/dipole_3tf_0.dat')#, skip_header=9)
dipsim4 = np.genfromtxt(dir+'sim/dipole_4tf_0.dat')#, skip_header=9)

diprdm = np.genfromtxt(dir+'rdm/dipole_0.dat')#, skip_header=9)
diprdm1 = np.genfromtxt(dir+'rdm/dipole_1tf_0.dat')#, skip_header=9)
diprdm2 = np.genfromtxt(dir+'rdm/dipole_2tf_0.dat')#, skip_header=9)
diprdm3 = np.genfromtxt(dir+'rdm/dipole_3tf_0.dat')#, skip_header=9)
diprdm4 = np.genfromtxt(dir+'rdm/dipole_4tf_0.dat')#, skip_header=9)

diprdm1_nl = np.genfromtxt(dir+'rdm_nl/dipole_1nl_0.dat')#, skip_header=9)
diprdm2_nl = np.genfromtxt(dir+'rdm_nl/dipole_2nl_0.dat')#, skip_header=9)
diprdm3_nl = np.genfromtxt(dir+'rdm_nl/dipole_3nl_0.dat')#, skip_header=9)
diprdm4_nl = np.genfromtxt(dir+'rdm_nl/dipole_4nl_0.dat')#, skip_header=9)

py.rcParams.update(params)
#py.figure(1)
fig = py.figure()
py.clf()

#py.loglog(dipsim[:,0], dipsim[:,1], 'c', label=r"All")
#py.loglog(diprdm[:,0], diprdm[:,1], 'c--')


ax1 = py.subplot(411)
py.loglog(dipsim1[:,0], dipsim1[:,1], 'r', label=r"$Q_1$")#label=r"$0-5214 km/s$")
py.loglog(diprdm1[:,0], diprdm1[:,1], 'r--')
py.loglog(diprdm1_nl[:,0], diprdm1_nl[:,1], 'r-.')
lg = py.legend(loc="upper right", fancybox=True, numpoints=1)
lg.draw_frame(False)

ax2 = py.subplot(412, sharex=ax1, sharey=ax1)
py.loglog(dipsim2[:,0], dipsim2[:,1], 'b', label=r"$Q_2$")#label=r"$5214-7853 km/s$")
py.loglog(diprdm2[:,0], diprdm2[:,1], 'b--')
py.loglog(diprdm2_nl[:,0], diprdm2_nl[:,1], 'b-.')
lg = py.legend(loc="upper right", fancybox=True, numpoints=1)
lg.draw_frame(False)

ax3 = py.subplot(413, sharex=ax1, sharey=ax1)
py.loglog(dipsim3[:,0], dipsim3[:,1], 'g', label=r"$Q_3$")#label=r"$7853-11280 km/s$")
py.loglog(diprdm3[:,0], diprdm3[:,1], 'g--')
py.loglog(diprdm3_nl[:,0], diprdm3_nl[:,1], 'g-.')
lg = py.legend(loc="upper right", fancybox=True, numpoints=1)
lg.draw_frame(False)

ax4 = py.subplot(414, sharex=ax1, sharey=ax1)
py.loglog(dipsim4[:,0], dipsim4[:,1], 'k', label=r"$Q_4$")#label=r"$>11280 km/s$")
py.loglog(diprdm4[:,0], diprdm4[:,1], 'k--')
py.loglog(diprdm4_nl[:,0], diprdm4_nl[:,1], 'k--')
lg = py.legend(loc="upper right", fancybox=True, numpoints=1)
lg.draw_frame(False)

py.xlabel(r"$r\ [{\rm Mpc}/{\rm h}]$")
#py.axes().set_xlim((xmin,xmax))
#py.ylabel(r"Dipole Correlation")
#py.axes().set_ylim((ymin,ymax))
fig.text(0.03, 0.5, r'${\rm Dipole\, Correlation}$', ha='center', va='center', rotation='vertical')

ax1.set_xlim((xmin, xmax))
ax2.set_xlim((xmin, xmax))
ax3.set_xlim((xmin, xmax))
ax4.set_xlim((xmin, xmax))
ax1.set_ylim((ymin, ymax))
ax2.set_ylim((ymin, ymax))
ax3.set_ylim((ymin, ymax))
ax4.set_ylim((ymin, ymax))

py.setp(ax1.get_xticklabels(), visible=False)
py.setp(ax2.get_xticklabels(), visible=False)
py.setp(ax3.get_xticklabels(), visible=False)

py.subplots_adjust(hspace=0.)

py.savefig(figdir+'dipolefig.pdf')
