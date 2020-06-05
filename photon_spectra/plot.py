import photon_spectra
import numpy as np

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

wavelengths = np.linspace(240e-9, 700e-9, 501)
equal = photon_spectra.make_equal_sampling(wavelengths=wavelengths)

c = {
    'dpi': 200,
    'rows': 800,
    'cols': 1200,
    'path': '',
    'axes_margins': [.12, .12, .85, .85]
}

figsize = (c['cols']/c['dpi'], c['rows']/c['dpi'])

fig = plt.figure(figsize=figsize, dpi=c['dpi'])
ax = fig.add_axes(c['axes_margins'])
lbenn, = ax.plot(
    wavelengths,
    equal['night_sky']['la_palma_benn_ellison'],
    '-k',
    label='Benn, and Ellison, 1998')
lhof, = ax.plot(
    wavelengths,
    equal['night_sky']['la_palma_preuss'],
    '--k',
    label='Preuss, Hermann, Hofmann, and Kohnle, 2002')
ax.semilogy()
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel('Wavelength / m')
ax.set_ylabel('Differential flux / m$^{-2}$ sr$^{-1}$ s$^{-1}$ m$^{-1}$')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
ax.legend(handles=[lbenn, lhof])
fig.savefig('./readme/nsb.png')


fig = plt.figure(figsize=figsize, dpi=c['dpi'])
ax = fig.add_axes(c['axes_margins'])
lcer, = plt.plot(
    wavelengths,
    equal['cherenkov']['la_palma_2km_asl_zenith_0deg'],
    label='3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 0deg')
lcer70, = plt.plot(
    wavelengths,
    equal['cherenkov']['la_palma_2km_asl_zenith_70deg'],
    label='3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 70deg')
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel('Wavelength / m')
ax.set_ylabel('Relative / 1')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
ax.legend(handles=[lcer, lcer70])
fig.savefig('./readme/cherenkov.png')


fig = plt.figure(figsize=figsize, dpi=c['dpi'])
ax = fig.add_axes(c['axes_margins'])
lcer, = plt.plot(
    wavelengths,
    equal['photon_detection_efficieny']['hamamatsu_s10362_33_050c'],
    label='Hamamatsu, s10362_33_050c, FACT SiPM')
lcer70, = plt.plot(
    wavelengths,
    equal['photon_detection_efficieny']['hamamatsu_r11920_100_05'],
    label='Hamamatsu, r11920_100_05, CTA LST PMT')
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel('Wavelength / m')
ax.set_ylabel('Photon detection efficieny / 1')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
ax.legend(handles=[lcer, lcer70])
fig.savefig('./readme/pde.png')


fig = plt.figure(figsize=figsize, dpi=c['dpi'])
ax = fig.add_axes(c['axes_margins'])
legend_handles = []
for name in equal['transmissivity']:
    leg, = plt.plot(
        wavelengths,
        equal['transmissivity'][name],
        label=name)
    legend_handles.append(leg)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel('Wavelength / m')
ax.set_ylabel('Transmissivity / 1')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
ax.legend(handles=legend_handles)
fig.savefig('./readme/transmission.png')


fig = plt.figure(figsize=figsize, dpi=c['dpi'])
ax = fig.add_axes(c['axes_margins'])
legend_handles = []
for mirror_name in equal['reflectivity']:
    leg, = plt.plot(
        wavelengths,
        equal['reflectivity'][mirror_name],
        label=mirror_name)
    legend_handles.append(leg)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel('Wavelength / m')
ax.set_ylabel('Reflectivity / 1')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
ax.legend(handles=legend_handles)
fig.savefig('./readme/cta_mirrors.png')


fig = plt.figure(figsize=figsize, dpi=c['dpi'])
ax = fig.add_axes(c['axes_margins'])
legend_handles = []
for name in equal['photon_detection_efficieny']:
    if 'ccd' in name:
        leg, = plt.plot(
            wavelengths,
            equal['photon_detection_efficieny'][name],
            label=name)
        legend_handles.append(leg)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel('Wavelength / m')
ax.set_ylabel('Photon detection efficieny / 1')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
ax.legend(handles=legend_handles)
fig.savefig('./readme/ccd.png')
