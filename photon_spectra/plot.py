import photon_spectra
import numpy as np

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

c = {
    "dpi": 200,
    "rows": 800,
    "cols": 1200,
    "path": "",
    "axes_margins": [0.12, 0.12, 0.85, 0.85],
}


def equal_group(group, common_wavelength):
    eq = {}
    for key in group:
        eq[key] = photon_spectra.utils.make_values_for_common_wavelength(
            wavelength=group[key]["wavelength"],
            value=group[key]["value"],
            common_wavelength=common_wavelength,
        )
    return eq


common_wavelength = np.linspace(240e-9, 700e-9, 501)


figsize = (c["cols"] / c["dpi"], c["rows"] / c["dpi"])

# NSB
# ===
nsb = {
    "nsb_la_palma_2013_benn": photon_spectra.nsb_la_palma_2013_benn.init(),
    "nsb_la_palma_2002_hofmann": photon_spectra.nsb_la_palma_2002_hofmann.init(),
}
eqnsb = equal_group(nsb, common_wavelength)

fig = plt.figure(figsize=figsize, dpi=c["dpi"])
ax = fig.add_axes(c["axes_margins"])
(lbenn,) = ax.plot(
    common_wavelength,
    eqnsb["nsb_la_palma_2013_benn"],
    "-k",
    label="Benn, and Ellison, 1998",
)
(lhof,) = ax.plot(
    common_wavelength,
    eqnsb["nsb_la_palma_2002_hofmann"],
    "--k",
    label="Preuss, Hermann, Hofmann, and Kohnle, 2002",
)
ax.semilogy()
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel("Wavelength / m")
ax.set_ylabel("Differential flux / m$^{-2}$ sr$^{-1}$ s$^{-1}$ m$^{-1}$")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid(color="k", linestyle="-", linewidth=0.66, alpha=0.1)
ax.legend(handles=[lbenn, lhof])
fig.savefig("./readme/nsb.png")

# CHERENKOV EMISSION
# ==================
cer = {
    "cherenkov_chile": photon_spectra.cherenkov_chile.init(),
    "cherenkov_la_palma_zd70deg": photon_spectra.cherenkov_la_palma.init(
        zenith_distance_deg=70
    ),
    "cherenkov_la_palma_zd00deg": photon_spectra.cherenkov_la_palma.init(
        zenith_distance_deg=0
    ),
}
eqcer = equal_group(cer, common_wavelength)


fig = plt.figure(figsize=figsize, dpi=c["dpi"])
ax = fig.add_axes(c["axes_margins"])
(lcer,) = plt.plot(
    common_wavelength,
    eqcer["cherenkov_la_palma_zd00deg"],
    label="3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 0deg",
)
(lcer70,) = plt.plot(
    common_wavelength,
    eqcer["cherenkov_la_palma_zd70deg"],
    label="3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 70deg",
)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel("Wavelength / m")
ax.set_ylabel("Relative / 1")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid(color="k", linestyle="-", linewidth=0.66, alpha=0.1)
ax.legend(handles=[lcer, lcer70])
fig.savefig("./readme/cherenkov.png")

# PDE
# ===
pde = {
    "hamamatsu_r11920_100_05": photon_spectra.hamamatsu_r11920_100_05.init(),
    "hamamatsu_s10362_33_050c": photon_spectra.hamamatsu_s10362_33_050c.init(),
}
eqpde = equal_group(pde, common_wavelength)


fig = plt.figure(figsize=figsize, dpi=c["dpi"])
ax = fig.add_axes(c["axes_margins"])
(lcer,) = plt.plot(
    common_wavelength,
    eqpde["hamamatsu_s10362_33_050c"],
    label="Hamamatsu, s10362_33_050c, FACT SiPM",
)
(lcer70,) = plt.plot(
    common_wavelength,
    eqpde["hamamatsu_r11920_100_05"],
    label="Hamamatsu, r11920_100_05, CTA LST PMT",
)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel("Wavelength / m")
ax.set_ylabel("Photon detection efficieny / 1")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid(color="k", linestyle="-", linewidth=0.66, alpha=0.1)
ax.legend(handles=[lcer, lcer70])
fig.savefig("./readme/pde.png")

# TRANSMISSION
# ============
tra = {
    "cta_mst_flash_cam_entrance_window": photon_spectra.cta_flash_cam_entrance_window.init(),
    "silica_glass_suprasil_311_312_313": photon_spectra.silica_glass_suprasil_311_312_313.init(
        "transmission"
    ),
    "veritas_nsb_filter_2015": photon_spectra.veritas_nsb_filter_2015.init(),
}
eqtra = equal_group(tra, common_wavelength)

fig = plt.figure(figsize=figsize, dpi=c["dpi"])
ax = fig.add_axes(c["axes_margins"])
legend_handles = []
for key in eqtra:
    (leg,) = plt.plot(common_wavelength, eqtra[key], label=key)
    legend_handles.append(leg)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel("Wavelength / m")
ax.set_ylabel("Transmissivity / 1")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid(color="k", linestyle="-", linewidth=0.66, alpha=0.1)
ax.legend(handles=legend_handles)
fig.savefig("./readme/transmission.png")

# REFLECTIVITY
# ============
ref = {
    "hess_ct5_mirror_new": photon_spectra.hess_ct5_mirror.init("new"),
    "hess_ct5_mirror_degraded": photon_spectra.hess_ct5_mirror.init(
        "degraded"
    ),
    "cta_mst_dielectric_before": photon_spectra.cta_mirrors.init(
        "cta_mst_dielectric_before"
    ),
    "cta_mst_dielectric_after": photon_spectra.cta_mirrors.init(
        "cta_mst_dielectric_after"
    ),
    "cta_mst_Al_SiO2_HfO2_SiO2_before": photon_spectra.cta_mirrors.init(
        "cta_mst_Al_SiO2_HfO2_SiO2_before"
    ),
    "cta_mst_Al_SiO2_HfO2_SiO2_after": photon_spectra.cta_mirrors.init(
        "cta_mst_Al_SiO2_HfO2_SiO2_after"
    ),
    "cta_mst_Al_SiO2_before": photon_spectra.cta_mirrors.init(
        "cta_mst_Al_SiO2_before"
    ),
    "cta_mst_Al_SiO2_after": photon_spectra.cta_mirrors.init(
        "cta_mst_Al_SiO2_after"
    ),
    "cta_astri_SiO2_mixed_multilayer_yellow": photon_spectra.cta_mirrors.init(
        "cta_astri_SiO2_mixed_multilayer_yellow"
    ),
    "cta_astri_SiO2_TiO2_mulitlayer": photon_spectra.cta_mirrors.init(
        "cta_astri_SiO2_TiO2_mulitlayer"
    ),
    "cta_astri_SiO2_mixed_multilayer_orange": photon_spectra.cta_mirrors.init(
        "cta_astri_SiO2_mixed_multilayer_orange"
    ),
    "cta_astri_Al_SiO2": photon_spectra.cta_mirrors.init("cta_astri_Al_SiO2"),
}
eqref = equal_group(ref, common_wavelength)

fig = plt.figure(figsize=figsize, dpi=c["dpi"])
ax = fig.add_axes(c["axes_margins"])
legend_handles = []
for key in eqref:
    (leg,) = plt.plot(common_wavelength, eqref[key], label=key)
    legend_handles.append(leg)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel("Wavelength / m")
ax.set_ylabel("Reflectivity / 1")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid(color="k", linestyle="-", linewidth=0.66, alpha=0.1)
ax.legend(handles=legend_handles)
fig.savefig("./readme/cta_mirrors.png")


# CCD
# ===
ccd = {
    "red": photon_spectra.ccd_rgb.init("red"),
    "green": photon_spectra.ccd_rgb.init("green"),
    "blue": photon_spectra.ccd_rgb.init("blue"),
}
eqccd = equal_group(ccd, common_wavelength)

fig = plt.figure(figsize=figsize, dpi=c["dpi"])
ax = fig.add_axes(c["axes_margins"])
legend_handles = []
for key in eqccd:
    (leg,) = plt.plot(common_wavelength, eqccd[key], label=key, color=key)
    legend_handles.append(leg)
ax.set_xlim([200e-9, 700e-9])
ax.set_xlabel("Wavelength / m")
ax.set_ylabel("Photon detection efficieny / 1")
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.grid(color="k", linestyle="-", linewidth=0.66, alpha=0.1)
ax.legend(handles=legend_handles)
fig.savefig("./readme/ccd.png")
