import numpy as np

_preuss2002study = "".join([
    "@article{preuss2002study,"
    "title={Study of the photon flux from the night sky at La Palma "
    "and Namibia, in the wavelength region relevant for "
    "imaging atmospheric Cherenkov telescopes},"
    "author={Preuss, S and Hermann, G and Hofmann, W and Kohnle, A},"
    "journal={Nuclear Instruments and Methods in Physics Research Section A: "
    "Accelerators, Spectrometers, Detectors and Associated Equipment},"
    "volume={481},"
    "number={1},"
    "pages={229--240},"
    "year={2002},"
    "publisher={Elsevier}"
    "},Figure 8"
])

_la_palma_2002_hofmann = np.array([
    # wavelength [m], nsb flux [1/(s m^2 sr m)]
    [362.5e-9, 3.8e18],
    [410.0e-9, 4.3e18],
    [440.0e-9, 5.2e18],
    [450.0e-9, 5.5e18],
    [500.0e-9, 6.5e18],
    [550.0e-9, 7.3e18],
])

differential_flux = {
    "wavelength_vs_value": _la_palma_2002_hofmann,
    "units": ["m", "m^{-2} sr^{-1} s^{-1} m^{-1}"],
    "reference": _preuss2002study,
}
