from . import hess_ct5_mirror
from . import hamamatsu_s10362_33_050c
from . import hamamatsu_r11920_100_05
from . import veritas_nsb_filter_2015
from . import silica_glass_suprasil_311_312_313
from . import cta_flash_cam_entrance_window
from . import cta_mirrors
from . import ccd_rgb
from . import blue_sky_diffuse
from . import cherenkov_chile
from . import cherenkov_la_palma
from . import sunlight_at_sea_level
from . import nsb_la_palma_2013_benn
from . import nsb_la_palma_2002_hofmann
import numpy as np

_ps = {}
_ps["reflectivity"] = {}
for key in cta_mirrors.reflectivities:
    _ps["reflectivity"][key] = cta_mirrors.reflectivities[key]
for key in hess_ct5_mirror.reflectivities:
    _ps["reflectivity"][key] = hess_ct5_mirror.reflectivities[key]


_ps["transmissivity"] = {}
_ps["transmissivity"]["cta_mst_flash_cam_entrance_window"] = (
    cta_flash_cam_entrance_window.transmisson)
_ps["transmissivity"]["silica_glass_suprasil_311_312_313"] = (
    silica_glass_suprasil_311_312_313.transmission)
_ps["transmissivity"]["veritas_nsb_filter_2015"] = (
    veritas_nsb_filter_2015.transmission
)

_ps['refractivity'] = {}
_ps["refractivity"]["silica_glass_suprasil_311_312_313"] = (
    silica_glass_suprasil_311_312_313.refraction)


_ps["photon_detection_efficieny"] = {}
for key in ccd_rgb.efficiency:
    _ps["photon_detection_efficieny"][key] = ccd_rgb.efficiency[key]

_ps["photon_detection_efficieny"]["hamamatsu_s10362_33_050c"] = (
    hamamatsu_s10362_33_050c.efficiency
)
_ps["photon_detection_efficieny"]["hamamatsu_r11920_100_05"] = (
    hamamatsu_r11920_100_05.efficiency
)

_ps["day_sky"] = {}
_ps["day_sky"]["blue_sky_diffuse"] = blue_sky_diffuse.emission
_ps["day_sky"]["sunlight_at_sea_level"] = (
    sunlight_at_sea_level.differential_flux
)

_ps["night_sky"] = {}
_ps["night_sky"]["la_palma_benn_ellison"] = (
    nsb_la_palma_2013_benn.differential_flux
)
_ps["night_sky"]["la_palma_preuss"] = (
    nsb_la_palma_2002_hofmann.differential_flux
)

_ps["cherenkov"] = {}
_ps["cherenkov"]["chile_5km_asl"] = cherenkov_chile.intensity
_ps["cherenkov"]["la_palma_2km_asl_zenith_0deg"] = (
    cherenkov_la_palma.intensities[0]
)
_ps["cherenkov"]["la_palma_2km_asl_zenith_70deg"] = (
    cherenkov_la_palma.intensities[70]
)

photon_spectra = _ps


def _to_array_interp(wavelength_vs_value, wavelengths):
    arr = np.array(wavelength_vs_value)
    below = wavelengths < np.min(arr[:, 0])
    above = wavelengths > np.max(arr[:, 0])
    invalid = below + above
    rec = np.interp(x=wavelengths, xp=arr[:, 0], fp=arr[:, 1])
    rec[invalid] = np.nan
    return rec


def make_equal_sampling(wavelengths=np.linspace(200e-9, 701e-9, 502)):
    equal = {}
    for category in _ps:
        equal[category] = {}
        for name in _ps[category]:
            equal[category][name] = _to_array_interp(
                wavelength_vs_value=_ps[category][name]['wavelength_vs_value'],
                wavelengths=wavelengths)
    return equal
