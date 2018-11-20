import numpy as np
import os
import equal_sampling as es
import matplotlib.pyplot as plt

out_dir = os.path.join('examples', 'nigh_sky_background')
os.makedirs(out_dir, exist_ok=True)


fig = plt.figure(figsize=(6, 4), dpi=200)
ax = fig.add_axes([.12, .12, .85, .85])

plt.figure()
lbenn, = ax.plot(
    es.wavelength,
    es.nsb_diff_la_palma_benn,
    '-k',
    label='Benn, and Ellison, 1998')
lhof, = ax.plot(
    es.wavelength,
    es.nsb_diff_la_palma_2002_hofmann,
    '--k',
    label='Preuss, Hermann, Hofmann, and Kohnle, 2002')
ax.semilogy()
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel(r'Wavelength / m')
ax.set_ylabel(r'Differential flux / m$^{-2}$ s$^{-1}$ sr$^{-1}$ m$^{-1}$')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.grid(color='k', linestyle='-', linewidth=0.66, alpha=0.1)
ax.legend(handles=[lbenn, lhof])
fig.savefig(os.path.join(out_dir, 'nsb_la_palma.png'))
