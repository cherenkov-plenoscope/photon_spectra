from cherenkov_la_palma import cherenkov_histogram_on_ground
from cherenkov_la_palma import cherenkov_histogram_on_ground_zenith_distance_70deg
from hamamatsu_r11920_100_05 import hamamatsu_r11920_100_05
from hamamatsu_s10362_33_050c import hamamatsu_s10362_33_050c
from nsb_la_palma_2002_hoffmann import la_palma_2002_hoffmann
from nsb_la_palma_2013_benn import la_palma_2013_benn
from veritas_nsb_filter_2015 import veritas_nsb_filter_2015

import numpy as np
import matplotlib.pyplot as plt

wavelength = np.linspace(200e-9, 700e-9, 1337)

cherenkov_la_palma = np.interp(
    x=wavelength,
    xp=cherenkov_histogram_on_ground[:, 0],
    fp=cherenkov_histogram_on_ground[:, 1],)
cherenkov_la_palma[wavelength < 250e-9] = np.nan

cherenkov_la_palma_zd_70deg = np.interp(
    x=wavelength,
    xp=cherenkov_histogram_on_ground_zenith_distance_70deg[:, 0],
    fp=cherenkov_histogram_on_ground_zenith_distance_70deg[:, 1],)
cherenkov_la_palma_zd_70deg[wavelength < 250e-9] = np.nan

sipm = np.interp(
    x=wavelength,
    xp=hamamatsu_s10362_33_050c[:, 0],
    fp=hamamatsu_s10362_33_050c[:, 1],)

pmt = np.interp(
    x=wavelength,
    xp=hamamatsu_r11920_100_05[:, 0],
    fp=hamamatsu_r11920_100_05[:, 1],)

nsb_diff_la_palma_hoffmann = np.interp(
    x=wavelength,
    xp=la_palma_2002_hoffmann[:, 0],
    fp=la_palma_2002_hoffmann[:, 1],)

nsb_diff_la_palma_hoffmann[wavelength < 362e-9] = np.nan
nsb_diff_la_palma_hoffmann[wavelength > 550e-9] = np.nan

nsb_diff_la_palma_benn = np.interp(
    x=wavelength,
    xp=la_palma_2013_benn[:, 0],
    fp=la_palma_2013_benn[:, 1],)

nsb_filter = np.interp(
    x=wavelength,
    xp=veritas_nsb_filter_2015[:, 0],
    fp=veritas_nsb_filter_2015[:, 1],)

plt.figure()
lbenn, = plt.plot(wavelength, nsb_diff_la_palma_benn, label='night-sky-background, La Palma, Benn')
lhoff, = plt.plot(wavelength, nsb_diff_la_palma_hoffmann, label='night-sky-background, La Palma, Hoffmann')
plt.semilogy()
plt.ylabel('differential flux/(m^-2 sr^-1 m^-1)')
plt.xlabel('wavelength/m')
plt.legend(handles=[lbenn, lhoff])
plt.savefig('./readme/nsb.png')

plt.figure()
lsipm, = plt.plot(wavelength, sipm, label='FACT SiPM')
lpmt, = plt.plot(wavelength, pmt, label='CTA LST PMT')
plt.ylabel('photon-detection-efficiency/1')
plt.xlabel('wavelength/m')
plt.legend(handles=[lsipm, lpmt])
plt.savefig('./readme/pde.png')

plt.figure()
lcer, = plt.plot(wavelength, cherenkov_la_palma,
	label='3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 0deg')
lcer70, = plt.plot(wavelength, cherenkov_la_palma_zd_70deg,
	label='3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 70deg')
plt.ylabel('relative/1')
plt.xlabel('wavelength/m')
plt.legend(handles=[lcer, lcer70])
plt.savefig('./readme/cherenkov.png')

plt.figure()
lfilter, = plt.plot(wavelength, nsb_filter, label='VERITAS night-sky-background filter')
plt.ylabel('transmission/1')
plt.xlabel('wavelength/m')
plt.legend(handles=[lfilter])
plt.savefig('./readme/transmission.png')