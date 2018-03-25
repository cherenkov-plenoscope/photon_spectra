import numpy as np

"""
@article{toyama2013novel,
  title={Novel photo multiplier tubes for the Cherenkov Telescope array project},
  author={Toyama, Takeshi and Mirzoyan, Razmik and Dickinson, Hugh and Fruck, Christian and Hose, J{\"u}rgen and Kellermann, Hanna and Kn{\"o}tig, Max and Lorenz, Eckart and Menzel, Uta and Nakajima, Daisuke and others},
  journal={arXiv preprint arXiv:1307.5463},
  year={2013}
}
"""

hamamatsu_r11920_100_05 = np.array([
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
])
