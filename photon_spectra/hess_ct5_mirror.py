import numpy as np
from . import utils


def init(key="degraded"):
    """
    keys = [new, degraded]
    """
    _m = {}

    _cornils2005optical = "".join(
        [
            "@inproceedings{cornils2005optical,"
            "title={The optical system of the HESS II telescope},"
            "author={Cornils, R and Bernloehr, Konrad and Heinzelmann, Goetz and "
            "Hofmann, Werner and Panter, Michael},"
            "booktitle={International Cosmic Ray Conference},",
            "volume={5}," "pages={171}," "year={2005}",
        ]
    )

    _m["new"] = np.array(
        [
            # wavelength/m, reflectivity/1
            [2.00e-07, 7.55056e-01],
            [2.85e-07, 7.90921e-01],
            [2.90e-07, 7.92809e-01],
            [3.00e-07, 7.97528e-01],
            [3.10e-07, 8.06966e-01],
            [3.20e-07, 8.14517e-01],
            [3.30e-07, 8.15460e-01],
            [3.40e-07, 8.21123e-01],
            [3.50e-07, 8.30562e-01],
            [4.00e-07, 8.40000e-01],
            [4.30e-07, 8.40000e-01],
            [4.50e-07, 8.40000e-01],
            [4.75e-07, 8.40000e-01],
            [4.90e-07, 8.40000e-01],
            [5.10e-07, 8.40000e-01],
            [5.30e-07, 8.40000e-01],
            [5.50e-07, 8.40000e-01],
            [5.90e-07, 8.40000e-01],
            [6.10e-07, 8.40000e-01],
            [6.40e-07, 8.49438e-01],
            [8.00e-07, 8.49438e-01],
        ]
    )

    _gaug2019using = "".join(
        [
            "@article{gaug2019using,"
            "title={Using Muon Rings for the Calibration of the "
            "Cherenkov Telescope Array: A systematic review of the method "
            "and its potential accuracy},"
            "author={Gaug, Markus and Fegan, Steven and Mitchell, AMW and "
            "Maccarone, Maria-Concetta and Mineo, Teresa and Okumura, Akira},"
            "journal={The Astrophysical Journal Supplement Series},"
            "volume={243},"
            "number={1},"
            "pages={11},"
            "year={2019},"
            "publisher={IOP Publishing}"
        ]
    )

    _degradation_factor = 0.71
    _m["degraded"] = _m["new"].copy()
    _m["degraded"][:, 1] *= _degradation_factor

    assert utils.is_strictly_monotonic_increasing(_m[key][:, 0])

    return {
        "wavelength": _m[key][:, 0],
        "value": _m[key][:, 1],
        "units": ["m", "1"],
        "reference": _cornils2005optical + _gaug2019using,
        "key": "hess_ct5_mirror_{:s}".format(key),
    }
