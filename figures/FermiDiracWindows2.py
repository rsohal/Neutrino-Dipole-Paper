#Computes Fermi-Dirac distributions between regions
import numpy as np
import scipy.integrate as integ
import matplotlib
matplotlib.use('PDF')
import pylab as py
#Parameters to change: q = p/kT = mv/kT

#Ramanjit's bins
q0 = 0
q1r = 1.885688757
q2r = 2.83978398
q3r = 4.07890789
q4r = 15

#Our bins
#2bins:qb = np.array([0,4,15])
#4bins:qb = np.array([0,2.4,2.5,3.8,15])
qb = np.array([0,2.4,2.5,3.8,15])
Nb = qb.size #Number of bins
qbi = np.zeros(qb.size)

Nq = 2000 #Number of points in files
q = np.linspace(qb[0],qb[Nb-1],Nq) #q array
for b in range(qbi.size):
    for i in range(Nq):
        if (q[i] < qb[b]):
            qbi[b] = i

def FermiDirac(q):
    fd = np.zeros(q.size)
    if (q.size != 1):
        dq = q[1]-q[0]
    else:
        print "ERROR"
    for i in range(q.size):
        fd[i] = 1.0/(np.exp(q[i])+1.0)
    fd = fd / 4.0 / np.pi**3
    return fd

fd = FermiDirac(q)

#Gaussian multiplier
g = np.zeros([Nq,Nb-1])
sg = np.zeros(Nq)
a = 1#0.5/0.717711#1
sg = sg*a
s = 0.8
p=2

#First do bin 2
for i in range(Nq):
    if (1<Nb):
        if (q[i]<qb[1]):
            g[i,1] = a*np.exp(-(qb[1]-q[i])**p/s)
        elif (q[i]>qb[2]):
            g[i,1] = a*np.exp(-(q[i]-qb[2])**p/s)
        else:
            g[i,1] = a
    else:
        if (q[i]<qb[1]):
            g[i,1] = a*np.exp(-(qb[i]-q[i])**p/s)
        else:
            g[i,1] = a
    sg[i] = sg[i]+g[i,1]

#Loop through bins
for b in range(Nb-1):
    if (b != 1):
        for i in range(Nq):
            if (b<Nb-2):
                if (q[i] < qb[b+1]):
                    g[i,b] = a*1.0-sg[i]
                    sg[i] = sg[i] + g[i,b]
                    maxi = i
                else:
                    g[i,b] = g[maxi,b]*np.exp(-(q[i]-q[maxi])**p/s)
                    sg[i] =sg[i] + g[i,b]
            else:
                g[i,b] = a*1.0-sg[i]
                sg[i] = sg[i] + g[i,b]

#Plotting
colors=np.array(['brown','red','orange','pink','yellow'])
py.figure(1)
for b in range(Nb-1):
    py.semilogy(q[:],fd[:]*g[:,b],'--',color=colors[b])
py.semilogy(q[:],fd[:],':',color='black')
py.xlabel(r'$mv/kT$')
#py.axes().set_xlim((0.07,3))
py.ylabel(r'$\bar{n}$')
py.axvline(x=q1r,color='black')
py.axvline(x=q2r,color='black')
py.axvline(x=q3r,color='black')
py.axes().set_ylim((1e-8,1e-2))
#py.legend(loc='best',fancybox=True)
py.savefig('./figures/fdwindow.pdf')
py.close()

py.figure(1)
for b in range(Nb-1):
    py.plot(q[:],g[:,b],'-',color=colors[b])
py.plot(q,sg,':',color='black')
py.xlabel(r'q')
py.axes().set_ylim((0.,1.05))
py.ylabel(r'g(q)')
py.axvline(x=q1r,color='blue')
py.axvline(x=q2r,color='green')
py.axvline(x=q3r,color='red')
#py.savefig('./g.pdf')
py.close()

#Need to compute Omega for each!
m=0.2 #eV
deg=2 #Degeneracy
h=0.67
G = 6.67384*10.0**-11 #m^3 kg^-1 s^-2
H = 100*h # (km/s/Mpc)
Mpc = 3.08567758*10.0**22 / 1000.0 #km
H = H / Mpc #1/s

hbar = 1.05457173*10.0**-34 # m^2 kg / s
c = 299792458 #m/s
k = 1.3806488*10**-23 #m^2 kg /s^2 / K
T = (4.0/11.0)**(1.0/3.0) * 2.725 #K

evc2 = 1.782662*10**-36 #1ev/c^2 = 1.8*10**-36 kg

Omega = m * deg * (8*np.pi*G/3/H**2) * (k/hbar/c)**3 * (1.0/2.0/np.pi**2) * T**3 * evc2 # per eV

print "Total = " + str((Omega*1.80309*deg)**-1)

def fdq(q):
    return q**2/(np.exp(q)+1)

Itot,err = integ.quad(fdq,q[0],q[Nq-1])
trp = np.trapz(q**2*fd*4*np.pi**3,q)
trpb = np.zeros(Nb-1)
Ibin = np.zeros(Nb-1)
for b in range(Nb-1):
    trpb[b] = np.trapz(q[:]**2*fd[:]*g[:,b]*4*np.pi**3,q[:])
    Ibin[b],err = integ.quad(fdq,qb[b],qb[b+1])

print "Function Omega total: " + str(m/94.14/h**2)
print "Theory Omega total: " + str(Omega*Itot)
print "Actual Omega total: " + str(Omega*trp) + " (" + str(Omega*sum(trpb)) + ")"
    
print "Theory Omega bin: " + repr(Omega*Ibin)
print "Actual Omega bin: " + repr(Omega*trpb)

#Save files
#np.savetxt('FD.txt',np.array([q,fd]).T,newline='\n')
#for b in range(Nb-1):
#    np.savetxt('FD'+str(b)+'.txt',np.array([q[:],fd[:]*g[:,b]]).T,newline='\n')
