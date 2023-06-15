import numpy as np
from . import utils


def init():
    _gaug2013night = "".join(
        [
            "@article{gaug2013night,"
            "title={Night Sky Background Analysis for the "
            "Cherenkov Telescope Array using the Atmoscope instrument},"
            "author={Gaug, Markus and others},"
            "journal={arXiv preprint arXiv:1307.3053},"
            "year={2013}"
            "},"
            "Figure 4. The CTA icrc2013 proceeding claims the data (black solid line) "
            "of Figure 4 to be from 'Benn Ch.R., Ellison S.R., La Palma tech. note, "
            "2007' but actual I did not find ths data in the specified "
            "technical note 115. There is sth. similar but not down to this "
            "low wavelengths."
        ]
    )

    h = 6.626e-34  # [J s]
    c = 299792458

    # 1 Jy = 10^-26 J/(s m^2 Hz)
    # wavelength [nm], flux [Jy / (deg^2)] // [10^-26 J/(s m^2 Hz deg^2)]
    raw = np.array(
        [
            [240, 8],  # extrapolated
            [270, 11],  # extrapolated
            [300, 14.7],  # extrapolated
            [330, 15.7],
            [340, 20],
            [394, 30],
            [395, 145],
            [396, 30],
            [433, 40],
            [435, 81],
            [437, 40],
            [462, 50],
            [485, 60],
            [525, 80],
            [555, 97],
            [557.5, 948],
            [561, 93],
            [585, 105],
            [591, 424],
            [595, 146],
            [600, 130],
            [605, 106],
            [627, 161],
            [630, 851],
            [632, 145],
            [638, 371],
            [640, 105],
            [645, 105],
            [647, 140],
            [660, 140],
            [670, 105],
            [678, 105],
            [685, 217],
            [701, 140],
        ]
    )

    raw[:, 0] *= 1e-9  # from nm to m -> wavelength [m]

    raw[:, 1] *= 1e-26  # from Jy to J -> flux [J / (s m^2 Hz deg^2)]

    square_deg_2_steradian = (2.0 * np.pi / 360) ** 2.0
    raw[:, 1] /= square_deg_2_steradian
    # from deg^2 to sr -> flux [J / (s m^2 Hz sr)]

    f = c / raw[:, 0]
    # remove frequency
    raw[:, 1] *= f  # from Hz to 1 -> flux [J / (s m^2 1 sr)]

    lamb = raw[:, 0]
    raw[:, 1] /= lamb  # from Hz to 1 -> flux [J / (s m^2 m sr)]

    # differential flux
    raw[:, 1] /= (h * c) / raw[:, 0]  # flux [1 / (s m^2 m sr)]

    _la_palma_2013_benn = raw

    assert utils.is_strictly_monotonic_increasing(_la_palma_2013_benn[:, 0])

    return {
        "wavelength": _la_palma_2013_benn[:, 0],
        "value": _la_palma_2013_benn[:, 1],
        "units": ["m", "m^{-2} sr^{-1} s^{-1} m^{-1}"],
        "reference": _gaug2013night,
    }
