import numpy as np


def make_values_for_common_wavelength(wavelength, value, common_wavelength):
    below = common_wavelength < np.min(wavelength)
    above = common_wavelength > np.max(wavelength)
    invalid = below + above
    rec = np.interp(x=common_wavelength, xp=wavelength, fp=value)
    rec[invalid] = np.nan
    return rec


def is_strictly_monotonic_increasing(x):
    assert len(x) >= 2
    for i in range(len(x) - 1):
        if x[i + 1] <= x[i]:
            return False
    return True


"""
_ps = {}
_ps["reflectivity"] = {}
for key in cta_mirrors.reflectivities:
    _ps["reflectivity"][key] = cta_mirrors.reflectivities[key]
for key in hess_ct5_mirror.reflectivities:
    _ps["reflectivity"][key] = hess_ct5_mirror.reflectivities[key]


_ps["transmissivity"] = {}
_ps["transmissivity"][
    "cta_mst_flash_cam_entrance_window"
] = cta_flash_cam_entrance_window.transmisson
_ps["transmissivity"][
    "silica_glass_suprasil_311_312_313"
] = silica_glass_suprasil_311_312_313.transmission
_ps["transmissivity"][
    "veritas_nsb_filter_2015"
] = veritas_nsb_filter_2015.transmission

_ps["refractivity"] = {}
_ps["refractivity"][
    "silica_glass_suprasil_311_312_313"
] = silica_glass_suprasil_311_312_313.refraction


_ps["photon_detection_efficieny"] = {}
for key in ccd_rgb.efficiency:
    _ps["photon_detection_efficieny"][key] = ccd_rgb.efficiency[key]

_ps["photon_detection_efficieny"][
    "hamamatsu_s10362_33_050c"
] = hamamatsu_s10362_33_050c.efficiency
_ps["photon_detection_efficieny"][
    "hamamatsu_r11920_100_05"
] = hamamatsu_r11920_100_05.efficiency

_ps["day_sky"] = {}
_ps["day_sky"]["blue_sky_diffuse"] = blue_sky_diffuse.emission
_ps["day_sky"][
    "sunlight_at_sea_level"
] = sunlight_at_sea_level.differential_flux

_ps["night_sky"] = {}
_ps["night_sky"][
    "la_palma_benn_ellison"
] = nsb_la_palma_2013_benn.differential_flux
_ps["night_sky"][
    "la_palma_preuss"
] = nsb_la_palma_2002_hofmann.differential_flux

_ps["cherenkov"] = {}
_ps["cherenkov"]["chile_5km_asl"] = cherenkov_chile.intensity
_ps["cherenkov"][
    "la_palma_2km_asl_zenith_0deg"
] = cherenkov_la_palma.intensities[0]
_ps["cherenkov"][
    "la_palma_2km_asl_zenith_70deg"
] = cherenkov_la_palma.intensities[70]

photon_spectra = _ps
"""
