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
