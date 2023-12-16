import numpy as np
from . import utils


def init():
    _toyama2013novel = "".join(
        [
            "@article{toyama2013novel,"
            "title={Novel photo multiplier tubes for the "
            "Cherenkov Telescope array project},"
            "author={Toyama, Takeshi and Mirzoyan, Razmik and "
            "Dickinson, Hugh and Fruck, Christian and Hose, Juergen and "
            "Kellermann, Hanna and Knoetig, Max and Lorenz, Eckart and "
            "Menzel, Uta and Nakajima, Daisuke and others},"
            "journal={arXiv preprint arXiv:1307.5463},"
            "year={2013}"
            "}"
        ]
    )

    _kalekin2018average = "".join(
        [
            "Average of 382 PMTs in 420 measurements."
            "Oleg Kalekin, University Erlangen, March 2018."
        ]
    )

    _hamamatsu_r11920_100_05_sample = np.array(
        [
            # wavelength/m, efficiency/1
            [200e-9, 0.0000],
            [220e-9, 0.0149],
            [240e-9, 0.0673],
            [260e-9, 0.1812],
            [280e-9, 0.2758],
            [300e-9, 0.3686],
            [320e-9, 0.3866],
            [340e-9, 0.3975],
            [360e-9, 0.4017],
            [380e-9, 0.4083],
            [400e-9, 0.4010],
            [420e-9, 0.3764],
            [440e-9, 0.3576],
            [460e-9, 0.3143],
            [480e-9, 0.2782],
            [500e-9, 0.2480],
            [540e-9, 0.1257],
            [580e-9, 0.0837],
            [620e-9, 0.0396],
            [660e-9, 0.0107],
            [701e-9, 0.0001],
        ]
    )

    _sample_220nm = _hamamatsu_r11920_100_05_sample[1]
    assert utils.is_close(_sample_220nm[0], 220e-9)
    _sample_240nm = _hamamatsu_r11920_100_05_sample[2]
    assert utils.is_close(_sample_240nm[0], 240e-9)

    _hamamatsu_r11920_100_05 = np.array(
        [
            # wavelength/m, efficiency/1
            [200e-9, 0.0000],
            _sample_220nm,
            _sample_240nm,
            [2.50000e-07, 8.18886e-02],
            [2.55000e-07, 9.39379e-02],
            [2.60000e-07, 1.08774e-01],
            [2.65000e-07, 1.25239e-01],
            [2.70000e-07, 1.43531e-01],
            [2.75000e-07, 1.72292e-01],
            [2.80000e-07, 2.04453e-01],
            [2.85000e-07, 2.34614e-01],
            [2.90000e-07, 2.61815e-01],
            [2.95000e-07, 2.83185e-01],
            [3.00000e-07, 2.96615e-01],
            [3.05000e-07, 3.07959e-01],
            [3.10000e-07, 3.17670e-01],
            [3.15000e-07, 3.25178e-01],
            [3.20000e-07, 3.32991e-01],
            [3.25000e-07, 3.43457e-01],
            [3.30000e-07, 3.54165e-01],
            [3.35000e-07, 3.61050e-01],
            [3.40000e-07, 3.63635e-01],
            [3.45000e-07, 3.63309e-01],
            [3.50000e-07, 3.61762e-01],
            [3.55000e-07, 3.60855e-01],
            [3.60000e-07, 3.62325e-01],
            [3.65000e-07, 3.67381e-01],
            [3.70000e-07, 3.75693e-01],
            [3.75000e-07, 3.84741e-01],
            [3.80000e-07, 3.90440e-01],
            [3.85000e-07, 3.93774e-01],
            [3.90000e-07, 3.94982e-01],
            [3.95000e-07, 3.93193e-01],
            [4.00000e-07, 3.89664e-01],
            [4.05000e-07, 3.86041e-01],
            [4.10000e-07, 3.82430e-01],
            [4.15000e-07, 3.78400e-01],
            [4.20000e-07, 3.74011e-01],
            [4.25000e-07, 3.69019e-01],
            [4.30000e-07, 3.63354e-01],
            [4.35000e-07, 3.57448e-01],
            [4.40000e-07, 3.51572e-01],
            [4.45000e-07, 3.45754e-01],
            [4.50000e-07, 3.39110e-01],
            [4.55000e-07, 3.29952e-01],
            [4.60000e-07, 3.17899e-01],
            [4.65000e-07, 3.03786e-01],
            [4.70000e-07, 2.89969e-01],
            [4.75000e-07, 2.77766e-01],
            [4.80000e-07, 2.67441e-01],
            [4.85000e-07, 2.58627e-01],
            [4.90000e-07, 2.51829e-01],
            [4.95000e-07, 2.45976e-01],
            [5.00000e-07, 2.40780e-01],
            [5.05000e-07, 2.34528e-01],
            [5.10000e-07, 2.25942e-01],
            [5.15000e-07, 2.12880e-01],
            [5.20000e-07, 1.94423e-01],
            [5.25000e-07, 1.72919e-01],
            [5.30000e-07, 1.53248e-01],
            [5.35000e-07, 1.37555e-01],
            [5.40000e-07, 1.25647e-01],
            [5.45000e-07, 1.16511e-01],
            [5.50000e-07, 1.09241e-01],
            [5.55000e-07, 1.03210e-01],
            [5.60000e-07, 9.79524e-02],
            [5.65000e-07, 9.32636e-02],
            [5.70000e-07, 8.88079e-02],
            [5.75000e-07, 8.44240e-02],
            [5.80000e-07, 8.00710e-02],
            [5.85000e-07, 7.55250e-02],
            [5.90000e-07, 7.10969e-02],
            [5.95000e-07, 6.66160e-02],
            [6.00000e-07, 6.21910e-02],
            [6.05000e-07, 5.80740e-02],
            [6.10000e-07, 5.39486e-02],
            [6.15000e-07, 5.00819e-02],
            [6.20000e-07, 4.61419e-02],
            [6.25000e-07, 4.24419e-02],
            [6.30000e-07, 3.88429e-02],
            [6.35000e-07, 3.54064e-02],
            [6.40000e-07, 3.19362e-02],
            [6.45000e-07, 2.88636e-02],
            [6.50000e-07, 2.58871e-02],
            [6.55000e-07, 2.29940e-02],
            [6.60000e-07, 2.07012e-02],
            [6.65000e-07, 1.86464e-02],
            [6.70000e-07, 1.60931e-02],
            [6.75000e-07, 1.36905e-02],
            [6.80000e-07, 1.15776e-02],
            [6.85000e-07, 9.72286e-03],
            [6.90000e-07, 7.86738e-03],
            [6.95000e-07, 6.77048e-03],
            [7.00000e-07, 5.94595e-03],
            [701e-9, 0.0001],
        ]
    )

    assert utils.is_strictly_monotonic_increasing(
        _hamamatsu_r11920_100_05[:, 0]
    )

    return {
        "wavelength": _hamamatsu_r11920_100_05[:, 0],
        "value": _hamamatsu_r11920_100_05[:, 1],
        "units": ["m", "1"],
        "reference": _toyama2013novel + _kalekin2018average,
        "key": "hamamatsu_r11920_100_05",
    }
