
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
import scipy.constants as const
import math
from decimal import *

getcontext().prec = 7


# In[ ]:

def integration_layer_bin(variable, i, fx, dx, nd):
    variable[i] = ((fx[0]) * (dx[0]-0.)/2.)
    for j in range(0,nd-1):
    #   IWC_psd[i] = (IWC_psd[i] + (numd[j]*mass[j] + numd[j+1]*mass[j+1]) * (Ldim[j+1] - Ldim[j])/2.)
        variable[i] = (variable[i] + np.trapz(fx[j:j+2],dx[j:j+2]))
    variable[i] = (variable[i] + (fx[nd-1]) * (dx[nd-1] - dx[nd-2])/2.)
    return(variable);


# In[ ]:

# pro sub24hnum, slp2, y_sim, iwcpsd, nbin, deltaz

#### READ IN SCATTERING MODEL ###########################
# line 4:
# readfile='B6pr_2_dimensional_and_mass_oriented_24.0GHz.txt'
    scat_mod = pd.read_csv('%s/%s' %(txt_dir,model),                    header=3,  names = ['r_ev','mass', 'C_bk', 'C_sca', 'C_ext', 'Ldim','none'],                     sep = '\s+', engine= 'python')
##############################################


# line 22:
# radar_freq = 24.0e9                 ; Hz
# pi         = 3.1415926554
# c          = 2.9979e8               ; m/s
# k_sq_water = 0.92                   ; based upon MRR guide? p.13 in MRR-Physical Basics   
# waveln_mm  = c/radar_freq*1000.0    ; mm


#### READ IN BASE PARTICLE PROPERTIES ###########################
# line 30 & line 51: 
# for i=0,nd-1 do begin
#     readf,2, v1,v2,v3,v4,v5,v6
#     ldim(i) = v1/1000.0              ; for mm
#     rev(i)  = v1/1000.0              ;   for mm
#     cbk(i)  = v3
#     cext(i) = v4                     ;  was v4
#     mass(i) = v2*1000.0              ;  for grams
#     ;area(i) = v6
# endfor;i
##############################################
    
    
#### MAKE SIMPLE log PSD ###########################
# line 74:
# for k=0, 0  do begin     ; each vertical profile

# line 106:
# for i=0,nbin-1 do begin
#    lamb(i)=10^slp2(i)
#    n0(i)=10^slp2(i+nbin)

# line 117:
# for j=0,nbin-1 do begin             ; each vertical radar bin 
#      for i=0,nd-1 do begin
#           numd(i)=n0(j)*exp(-lamb(j)*ldim(i))          ;   per (m^3 mm) 
##############################################

#### INTEGRATE TO FIND IWP/SWC IN EACH LAYER/RADAR BIN BASED UPON PSD ###########################
# line 124:
# iwcpsd(j)=numd(0)*mass(0)*(ldim(0)-0.)/2.
# for i=0,nd-2 do begin
#    iwcpsd(j)=iwcpsd(j)+(numd(i)*mass(i)+numd(i+1)*mass(i+1))*(ldim(i+1)-ldim(i))/2.0
# iwcpsd(j)=iwcpsd(j)+numd(nd-1)*mass(nd-1)*(ldim(nd-1)-ldim(nd-2))/2.
##############################################

#### INTEGRATE TO FIND NUMBER, EXTINCTION, BACKSCATTER, ETC ###########################
# line 136:
# nt(j)=numd(0)*(ldim(0)-0.)/2.
# for i=0,nd-2 do begin
#    nt(j)=nt(j)+(numd(i)+numd(i+1))*(ldim(i+1)-ldim(i))/2.0
# nt(j)=nt(j)+numd(nd-1)*(ldim(nd-1)-ldim(nd-2))/2.
##############################################

#### ACCOUNT FOR ATTENUATION THROUGH LAYERS WITHIN RADAR BINS ###########################
# line 162:
# snow_ext_accum = snow_ext_accum + snowext(j)*deltaz*1.0        ; 1.0 here is a scaling factor

# line 168:
# Ze_ss(j) = eta(j)*waveln_mm^4.0/(k_sq_water*pi^5.0)*1e6       ; from Norm 2015? Eq. 15?
# Ze_ss_atten(j) = Ze_ss(j)*snow_atten*snow_atten               ; 2 way attenuation
# Ze_fin(j)=10.*alog10(ze_ss_atten(j))
##############################################

#### USE THE GEOMETRIC MEAN OF Ze_ss, Ze_ss_ext TO ESTIMATE THE MULTIPLE SCATTERED Ze ###########################
#### GIVES dBZe HALFWAY BETWEEN THE TWO ###########################
#### SEE MATROSOV AND BATTAGLIA, (2009), AND WOOD (2011, DISSERTATION, SEC. 7.2, 7.3.1)
# line 180:
# Ze_ms(j) = 10.*alog10(sqrt(Ze_ss(j)*Ze_ss_atten(j)))
# y_sim(j) = Ze_fin(j)
##############################################


# In[ ]:

def sub24hnum(slp2,nbin,dz):
    txt_dir = '../../Retrieval/unchanged/part_scat_forward_model'
    model = 'B6pr_2_dimensional_and_mass_oriented_24.0GHz.txt'


#### READ IN SCATTERING MODEL ###########################
# readfile='B6pr_2_dimensional_and_mass_oriented_24.0GHz.txt'
    scat_mod = pd.read_csv('%s/%s' %(txt_dir,model),                    header=3,  names = ['r_ev','mass', 'C_bk', 'C_sca', 'C_ext', 'Ldim','none'],                     sep = '\s+', engine= 'python')
##############################################


# line 22:
# Rayleigh approximation?:
    radar_freq = 24.0e9                  # radar frequency in [Hz]
    Pi         = const.pi                        # Pi
    c          = const.speed_of_light             # speed of light in [m/s]
    K_sq_water = 0.92                    # dielectric factor abs(K)^2_liquid = 0.92       (AOS740 7-9)
    wavel_mm   = (c/radar_freq) * 1000.    # wavelength, lambda in [mm] 

#### READ IN BASE PARTICLE PROPERTIES ###########################
# line 30 & line 51:
 #   Ldim   = scat_mod['Ldim']/1000.          # [um]
    r_ev   = (scat_mod['r_ev']/1000.).astype(np.float64)    # effective radius [um] --> [mm]
    Ldim   = (scat_mod['r_ev']/1000.).astype(np.float64)    # [mm]
    C_bk   = (scat_mod['C_bk']).astype(np.float64)          # backscatter coefficient [m^2]
#C_ext = scat_mod['C_ext']        # extinction coefficient [m^2]
    C_scat = (scat_mod['C_sca']).astype(np.float64)         # scattering coefficient [m^2]
    mass   = (scat_mod['mass']*1000.).astype(np.float64)    # mass [kg]  -->
#area = scat_mod['Ldim']          # [um]
#maxd = 
##############################################
    nd = r_ev.shape[0]
## in retrieval:
    C_ext = C_scat.astype(np.float64)
    
    
#### MAKE SIMPLE log PSD ###########################
# line 74:
    lamb = np.zeros(shape = nbin,dtype=np.float64)
    N0   = np.zeros(shape = nbin,dtype=np.float64)
    numd = np.zeros(shape = nd,dtype=np.float64)
    for k in range(0,1):
        IWC_psd  = np.zeros(shape=nbin,dtype=np.float64)
        n_tot    = np.zeros(shape=nbin,dtype=np.float64)
        eta      = np.zeros(shape=nbin,dtype=np.float64)
        snow_ext = np.zeros(shape=nbin,dtype=np.float64)
        IWC      = np.zeros(shape=nbin,dtype=np.float64)
        mind     = np.zeros(shape=(nbin,nd),dtype=np.float64)
        
        Ze_ss            = np.zeros(shape=nbin)       # singly-scattered nonattenuated reflectivity Zess,na
        Ze_ss_atten      = np.zeros(shape=nbin)       # singly-scattered attenuated reflectivity Zess,a 
        Ze_fin           = np.zeros(shape=nbin)
        Ze_multiple_scat = np.zeros(shape=nbin)
        y_sim            = np.zeros(shape=nbin)       # simulated refelectivities
        snow_ext_accum = 0.0
# line 106:
        for j in range(0,nbin):
            lamb[j] = (10.**(slp2[j]))
            N0[j]   = (10**(slp2[j+nbin]))

# line 117:
        for j in range(0,nbin):
            for i in range(0, nd):
                numd[i] = (N0[j]*math.exp( (- lamb[j] * Ldim[i])) )     # size distribution n(D) = n0 exp(-lambda*D)
                                                                        # per [m^3 mm]                
##############################################

#### INTEGRATE TO FIND IWP/SWC IN EACH LAYER/RADAR BIN BASED UPON PSD ###########################
# line 124:
            IWC_psd[j] = ((numd[0]*mass[0]) * (Ldim[0]-0.)/2.)          # ice water content psd
            for i in range(0,nd-1):
                IWC_psd[j] = (IWC_psd[j] + (numd[i]*mass[i] + numd[i+1]*mass[i+1]) * (Ldim[i+1] - Ldim[i])/2.)
            IWC_psd[j] = (IWC_psd[j] + (numd[nd-1]*mass[nd-1]) * (Ldim[nd-1] - Ldim[nd-2])/2.)
##############################################

#### INTEGRATE TO FIND NUMBER, EXTINCTION, BACKSCATTER, ETC ###########################
# line 136:
            n_tot    = integration_layer_bin(n_tot, j, numd, Ldim,nd)           # total number concentration
            eta      = integration_layer_bin(eta, j, numd*C_bk, Ldim, nd)       # 
            snow_ext = integration_layer_bin(snow_ext, j, numd*C_ext, Ldim, nd) #
            IWC      = integration_layer_bin(IWC, j, numd*mass, Ldim, nd)       # ice water content
            
            mind[j,0] = numd[0]*mass[0] * (Ldim[0]-0.)/2.
            for i in range(0,nd-1):
                mind[j,i] = np.trapz(numd[i:i+2]*mass[i:i+2], Ldim[i:i+2])
            mind[j,i] = numd[nd-1]*mass[nd-1] * (Ldim[nd-1] - Ldim[nd-2])/2.
##############################################

#### ACCOUNT FOR ATTENUATION THROUGH LAYERS WITHIN RADAR BINS ###########################
# line 162:
            snow_ext_accum   = (snow_ext_accum + snow_ext[j]*dz*1.0)        # 1. is scaling factor
            snow_attenuation = (np.exp(-snow_ext_accum))                    # Beer's law exp (−β*s)
# line 168:
            ## Wood, 2C-SNOW-PROFILE Eq. 17, 19
            Ze_ss[j]       = ((eta[j]*wavel_mm**4)/ (K_sq_water*const.pi**5)*10**6)   # singly-scattered nonattenuated reflectivity Zess,na at range bin i
            Ze_ss_atten[j] = (Ze_ss[j] * snow_attenuation**2  )                       # singly-scattered attenuated reflectivity Zess,a 
            Ze_fin[j]      = (10.*math.log10(Ze_ss_atten[j]))       ## in [dBZ]
##############################################

#### USE THE GEOMETRIC MEAN OF Ze_ss, Ze_ss_ext TO ESTIMATE THE MULTIPLE SCATTERED Ze ###########################
#### GIVES dBZe HALFWAY BETWEEN THE TWO ###########################
#### SEE MATROSOV AND BATTAGLIA, (2009), AND WOOD (2011, DISSERTATION, SEC. 7.2, 7.3.1)
# line 180:
            Ze_multiple_scat[j] = (10.*math.log10(np.sqrt(Ze_ss[j]*Ze_ss_atten[j])))  ## in [dBZ]
            y_sim = (Ze_fin )                                                         ## simulated reflectivities in [dBz]
            y_sim = y_sim.astype(np.float64)
            IWC_psd = IWC_psd.astype(np.float64)
##############################################
    return(y_sim,IWC_psd);

