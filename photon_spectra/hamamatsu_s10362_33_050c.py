import numpy as np
from . import utils


def init():
    _hamamatsu2009mppc = "".join(
        [
            "@manual{hamamatsu2009mppc,"
            "organization={HAMAMATSU PHOTONICS K.K., Solid State Division},"
            "title={MPPC (multi-pixel photon Counter), S10362-33 series},"
            "number={Cat. No. KAPD1023E05},"
            "year={2009},"
            "month={11},"
            "}"
        ]
    )

    _anderhub2013design = "".join(
        [
            "@article{anderhub2013design,"
            "title={Design and operation of FACT--"
            "the first G-APD Cherenkov telescope},"
            "author={Anderhub, H and Backes, M and Biland, A and "
            "Boccone, Vittorio and Braun, I and Bretz, T and Buss, J and "
            "Cadoux, Franck and Commichau, V and Djambazov, L and others},"
            "journal={Journal of Instrumentation},"
            "volume={8},"
            "number={06},"
            "pages={P06008},"
            "year={2013},"
            "publisher={IOP Publishing}"
            "}"
        ]
    )

    _hamamatsu_s10362_33_050c = np.array(
        [
            # wavelength/m, efficiency/1
            [2.39e-07, 0.00e00],  # conservative guess
            [3.00e-07, 0.00e00],
            [3.19e-07, 1.22e-01],
            [3.24e-07, 2.00e-01],
            [3.33e-07, 3.00e-01],
            [3.40e-07, 3.54e-01],
            [3.44e-07, 3.72e-01],
            [3.51e-07, 3.89e-01],
            [3.59e-07, 4.02e-01],
            [3.78e-07, 4.30e-01],
            [3.89e-07, 4.69e-01],
            [3.92e-07, 4.76e-01],
            [4.00e-07, 4.85e-01],
            [4.25e-07, 5.15e-01],
            [4.32e-07, 5.29e-01],
            [4.44e-07, 5.31e-01],
            [4.62e-07, 5.28e-01],
            [4.89e-07, 5.02e-01],
            [5.00e-07, 4.91e-01],
            [5.54e-07, 4.03e-01],
            [5.77e-07, 3.64e-01],
            [6.00e-07, 3.29e-01],
            [6.16e-07, 3.01e-01],
            [6.49e-07, 2.52e-01],
            [6.90e-07, 1.99e-01],
            [7.00e-07, 1.91e-01],
            [7.48e-07, 1.46e-01],
            [7.88e-07, 1.13e-01],
            [8.09e-07, 1.00e-01],
            [8.55e-07, 6.70e-02],
            [9.00e-07, 4.40e-02],
        ]
    )

    _max_pde_according_to_fact = 0.33
    _hamamatsu_s10362_33_050c[:, 1] /= _hamamatsu_s10362_33_050c[:, 1].max()
    _hamamatsu_s10362_33_050c[:, 1] *= _max_pde_according_to_fact

    assert utils.is_strictly_monotonic_increasing(
        _hamamatsu_s10362_33_050c[:, 0],
    )

    return {
        "wavelength": _hamamatsu_s10362_33_050c[:, 0],
        "value": _hamamatsu_s10362_33_050c[:, 1],
        "units": ["m", "1"],
        "reference": _hamamatsu2009mppc + _anderhub2013design,
    }
