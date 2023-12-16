import numpy as np
from . import utils


def init():
    _corsika2018cherenkov = "".join(
        [
            "A simulation with KIT CORSIKA\\n"
            "The wavelength distribution of photons from gamma-ray air-showers "
            "below 5 GeV observed on 5000m a.s.l.\\n"
            "This corresponds somewhat to the southern site of the "
            "Cherenkov-Telescope-Array "
            "(CTA). Similar to Chile, Paranal, ESO site.\\n"
            "RUNNR    1\\n"
            "EVTNR    1\\n"
            "NSHOW    256\\n"
            "PRMPAR   1 # gamma\\n"
            "ESLOPE  -2.0\\n"
            "ERANGE  0.25 1000\\n"
            "THETAP  0.  0.\\n"
            "PHIP    0.  360.\\n"
            "SEED 1 0 0\\n"
            "SEED 2 0 0\\n"
            "SEED 3 0 0\\n"
            "SEED 4 0 0\\n"
            "OBSLEV  5000.0e2\\n"
            "FIXCHI  0.\\n"
            "MAGNET 1e-99 1e-99\\n"
            "ELMFLG  T   T\\n"
            "MAXPRT  1\\n"
            "PAROUT  F F\\n"
            "TELESCOPE  0. 0. 0. 7.5e2\\n"
            "ATMOSPHERE 26 T\\n"
            "CWAVLG 250 700\\n"
            "CSCAT 1 570e2 0.0\\n"
            "CERQEF F T F\\n"
            "CERSIZ 1\\n"
            "CERFIL F\\n"
            "TSTART T\\n"
            "EXIT\\n"
        ]
    )

    _cherenkov_gamma_below_5gev_5000m_asl = np.array(
        [
            [2.40000000e-07, 0.00000000e00],
            [2.44646465e-07, 0.00000000e00],
            [2.49292929e-07, 1.28584002e01],
            [2.53939394e-07, 1.89062687e01],
            [2.58585859e-07, 2.49155464e01],
            [2.63232323e-07, 3.76854591e01],
            [2.67878788e-07, 3.06495341e01],
            [2.72525253e-07, 4.37530296e01],
            [2.77171717e-07, 6.43925610e01],
            [2.81818182e-07, 1.09197643e02],
            [2.86464646e-07, 1.06076217e02],
            [2.91111111e-07, 1.14208696e02],
            [2.95757576e-07, 1.36431704e02],
            [3.00404040e-07, 1.47571721e02],
            [3.05050505e-07, 1.65428835e02],
            [3.09696970e-07, 2.13305955e02],
            [3.14343434e-07, 2.06611321e02],
            [3.18989899e-07, 2.04165725e02],
            [3.23636364e-07, 2.34034144e02],
            [3.28282828e-07, 2.32703553e02],
            [3.32929293e-07, 2.44016757e02],
            [3.37575758e-07, 2.57018627e02],
            [3.42222222e-07, 2.22228858e02],
            [3.46868687e-07, 2.48239572e02],
            [3.51515152e-07, 2.01528796e02],
            [3.56161616e-07, 2.47853106e02],
            [3.60808081e-07, 2.13527950e02],
            [3.65454545e-07, 2.01270850e02],
            [3.70101010e-07, 2.24419372e02],
            [3.74747475e-07, 2.15301099e02],
            [3.79393939e-07, 2.16120582e02],
            [3.84040404e-07, 1.92481544e02],
            [3.88686869e-07, 2.10157172e02],
            [3.93333333e-07, 1.91410655e02],
            [3.97979798e-07, 1.91327752e02],
            [4.02626263e-07, 1.74028653e02],
            [4.07272727e-07, 1.73433129e02],
            [4.11919192e-07, 1.98846208e02],
            [4.16565657e-07, 1.90611780e02],
            [4.21212121e-07, 1.67582106e02],
            [4.25858586e-07, 1.82958088e02],
            [4.30505051e-07, 1.80669245e02],
            [4.35151515e-07, 1.69886641e02],
            [4.39797980e-07, 1.73631975e02],
            [4.44444444e-07, 1.44618841e02],
            [4.49090909e-07, 1.78527860e02],
            [4.53737374e-07, 1.59513286e02],
            [4.58383838e-07, 1.66752129e02],
            [4.63030303e-07, 1.66223158e02],
            [4.67676768e-07, 1.65897055e02],
            [4.72323232e-07, 1.46680296e02],
            [4.76969697e-07, 1.38808617e02],
            [4.81616162e-07, 1.35004126e02],
            [4.86262626e-07, 1.29230137e02],
            [4.90909091e-07, 1.61761829e02],
            [4.95555556e-07, 1.50250424e02],
            [5.00202020e-07, 1.33481091e02],
            [5.04848485e-07, 1.21934093e02],
            [5.09494949e-07, 1.35807900e02],
            [5.14141414e-07, 1.29900385e02],
            [5.18787879e-07, 1.18963925e02],
            [5.23434343e-07, 1.36826847e02],
            [5.28080808e-07, 1.18849061e02],
            [5.32727273e-07, 1.33128837e02],
            [5.37373737e-07, 1.35855056e02],
            [5.42020202e-07, 1.34671449e02],
            [5.46666667e-07, 1.03850866e02],
            [5.51313131e-07, 1.13031141e02],
            [5.55959596e-07, 1.24517770e02],
            [5.60606061e-07, 1.09291481e02],
            [5.65252525e-07, 1.16133735e02],
            [5.69898990e-07, 1.20050102e02],
            [5.74545455e-07, 1.00969110e02],
            [5.79191919e-07, 8.62872872e01],
            [5.83838384e-07, 1.02808893e02],
            [5.88484848e-07, 8.93935356e01],
            [5.93131313e-07, 9.61792588e01],
            [5.97777778e-07, 1.01241367e02],
            [6.02424242e-07, 1.19140853e02],
            [6.07070707e-07, 1.08966376e02],
            [6.11717172e-07, 9.34824162e01],
            [6.16363636e-07, 9.51472178e01],
            [6.21010101e-07, 9.23424129e01],
            [6.25656566e-07, 8.87091694e01],
            [6.30303030e-07, 9.49905057e01],
            [6.34949495e-07, 8.73973598e01],
            [6.39595960e-07, 7.72781677e01],
            [6.44242424e-07, 8.51370249e01],
            [6.48888889e-07, 8.89904525e01],
            [6.53535354e-07, 6.25598819e01],
            [6.58181818e-07, 1.02272764e02],
            [6.62828283e-07, 8.62880793e01],
            [6.67474747e-07, 8.21491632e01],
            [6.72121212e-07, 8.63049884e01],
            [6.76767677e-07, 7.11814370e01],
            [6.81414141e-07, 6.33166795e01],
            [6.86060606e-07, 7.80860019e01],
            [6.90707071e-07, 7.78624163e01],
            [6.95353535e-07, 7.63400726e01],
            [7.00000000e-07, 6.65096836e01],
        ]
    )

    assert utils.is_strictly_monotonic_increasing(
        _cherenkov_gamma_below_5gev_5000m_asl[:, 0]
    )

    return {
        "wavelength": _cherenkov_gamma_below_5gev_5000m_asl[:, 0],
        "value": _cherenkov_gamma_below_5gev_5000m_asl[:, 1],
        "units": ["m", "1"],
        "reference": _corsika2018cherenkov,
        "key": "cherenkov_chile",
    }
