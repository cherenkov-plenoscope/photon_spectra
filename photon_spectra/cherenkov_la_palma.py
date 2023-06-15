import numpy as np
from . import utils


def init(zenith_distance_deg=0):
    _corsika2018cherenkov = "".join(
        [
            "Simulated with corsika75600Linux_QGSII_urqmd\\n"
            "RUNNR    1\\n"
            "EVTNR    1\\n"
            "NSHOW    1\\n"
            "PRMPAR   1 # gamma\\n"
            "ESLOPE  -2.0\\n"
            "ERANGE  3000 3000\\n"
            "THETAP  {thetap:1.2f} {thetap:1.2f}\\n"
            "PHIP    0.  360.\\n"
            "SEED 1 0 0\\n"
            "SEED 2 0 0\\n"
            "SEED 3 0 0\\n"
            "SEED 4 0 0\\n"
            "OBSLEV  2200.0e2 # Roque de los Muchachos, La Palma\\n"
            "FIXCHI  0.\\n"
            "MAGNET 1e-99 1e-99\\n"
            "ELMFLG  T   T\\n"
            "MAXPRT  1\\n"
            "PAROUT  F F\\n"
            "TELESCOPE  0. 0. 0. 10e2 # instrument radius\\n"
            "ATMOSPHERE 8 T # MAGIC, Winter\\n"
            "CWAVLG 250 700\\n"
            "CSCAT 1 0.0 0.0\\n"
            "CERQEF F T F # pde, atmo, mirror\\n"
            "CERSIZ 1\\n"
            "CERFIL F\\n"
            "TSTART T\\n"
            "EXIT\\n"
        ]
    )

    _cer = {}

    _cer[0] = np.array(
        [
            [2.50e-07, 7.6536e-01],
            [2.51e-07, 1.0000e00],
            [2.52e-07, 9.9934e-01],
            [2.53e-07, 9.8728e-01],
            [2.54e-07, 9.9793e-01],
            [2.55e-07, 9.8019e-01],
            [2.56e-07, 9.6620e-01],
            [2.57e-07, 9.7011e-01],
            [2.58e-07, 9.7458e-01],
            [2.59e-07, 9.8353e-01],
            [2.60e-07, 9.5770e-01],
            [2.61e-07, 9.6742e-01],
            [2.62e-07, 9.6618e-01],
            [2.63e-07, 9.5718e-01],
            [2.64e-07, 9.6351e-01],
            [2.65e-07, 9.5276e-01],
            [2.66e-07, 9.4786e-01],
            [2.67e-07, 9.5367e-01],
            [2.68e-07, 9.4127e-01],
            [2.69e-07, 9.4334e-01],
            [2.70e-07, 9.2398e-01],
            [2.71e-07, 9.4077e-01],
            [2.72e-07, 9.3914e-01],
            [2.73e-07, 9.4241e-01],
            [2.74e-07, 9.3433e-01],
            [2.75e-07, 9.2814e-01],
            [2.76e-07, 9.2895e-01],
            [2.77e-07, 9.2556e-01],
            [2.78e-07, 9.3220e-01],
            [2.79e-07, 9.1225e-01],
            [2.80e-07, 9.2157e-01],
            [2.81e-07, 9.1899e-01],
            [2.82e-07, 9.1057e-01],
            [2.83e-07, 9.1139e-01],
            [2.84e-07, 9.0918e-01],
            [2.85e-07, 9.0882e-01],
            [2.86e-07, 9.0423e-01],
            [2.87e-07, 8.9992e-01],
            [2.88e-07, 8.8441e-01],
            [2.89e-07, 8.9230e-01],
            [2.90e-07, 8.8737e-01],
            [2.91e-07, 8.7092e-01],
            [2.92e-07, 8.7477e-01],
            [2.93e-07, 8.6297e-01],
            [2.94e-07, 8.5875e-01],
            [2.95e-07, 8.6447e-01],
            [2.96e-07, 8.6278e-01],
            [2.97e-07, 8.4414e-01],
            [2.98e-07, 8.3531e-01],
            [2.99e-07, 8.4888e-01],
            [3.00e-07, 8.3615e-01],
            [3.01e-07, 8.1257e-01],
            [3.02e-07, 8.2301e-01],
            [3.03e-07, 8.1979e-01],
            [3.04e-07, 8.2717e-01],
            [3.05e-07, 8.1277e-01],
            [3.06e-07, 8.1387e-01],
            [3.07e-07, 8.0775e-01],
            [3.08e-07, 8.0061e-01],
            [3.09e-07, 7.9756e-01],
            [3.10e-07, 7.9296e-01],
            [3.11e-07, 7.8718e-01],
            [3.12e-07, 7.9777e-01],
            [3.13e-07, 7.8788e-01],
            [3.14e-07, 7.7631e-01],
            [3.15e-07, 7.7818e-01],
            [3.16e-07, 7.6894e-01],
            [3.17e-07, 7.7980e-01],
            [3.18e-07, 7.5867e-01],
            [3.19e-07, 7.5913e-01],
            [3.20e-07, 7.6437e-01],
            [3.21e-07, 7.5151e-01],
            [3.22e-07, 7.4706e-01],
            [3.23e-07, 7.4910e-01],
            [3.24e-07, 7.5059e-01],
            [3.25e-07, 7.3410e-01],
            [3.26e-07, 7.3329e-01],
            [3.27e-07, 7.2401e-01],
            [3.28e-07, 7.2373e-01],
            [3.29e-07, 7.1989e-01],
            [3.30e-07, 7.1451e-01],
            [3.31e-07, 7.0803e-01],
            [3.32e-07, 7.0782e-01],
            [3.33e-07, 6.9943e-01],
            [3.34e-07, 6.9516e-01],
            [3.35e-07, 6.8624e-01],
            [3.36e-07, 6.9333e-01],
            [3.37e-07, 6.9299e-01],
            [3.38e-07, 6.7330e-01],
            [3.39e-07, 6.9300e-01],
            [3.40e-07, 6.7786e-01],
            [3.41e-07, 6.7160e-01],
            [3.42e-07, 6.7697e-01],
            [3.43e-07, 6.5797e-01],
            [3.44e-07, 6.5978e-01],
            [3.45e-07, 6.6336e-01],
            [3.46e-07, 6.6968e-01],
            [3.47e-07, 6.4466e-01],
            [3.48e-07, 6.4984e-01],
            [3.49e-07, 6.3788e-01],
            [3.50e-07, 6.3498e-01],
            [3.51e-07, 6.2654e-01],
            [3.52e-07, 6.2732e-01],
            [3.53e-07, 6.2605e-01],
            [3.54e-07, 6.2865e-01],
            [3.55e-07, 6.3782e-01],
            [3.56e-07, 6.2392e-01],
            [3.57e-07, 6.2891e-01],
            [3.58e-07, 6.1755e-01],
            [3.59e-07, 6.0574e-01],
            [3.60e-07, 6.0224e-01],
            [3.61e-07, 5.9931e-01],
            [3.62e-07, 6.0991e-01],
            [3.63e-07, 6.0833e-01],
            [3.64e-07, 6.0031e-01],
            [3.65e-07, 5.9227e-01],
            [3.66e-07, 5.8702e-01],
            [3.67e-07, 5.9322e-01],
            [3.68e-07, 5.8043e-01],
            [3.69e-07, 5.8152e-01],
            [3.70e-07, 5.7506e-01],
            [3.71e-07, 5.7819e-01],
            [3.72e-07, 5.7094e-01],
            [3.73e-07, 5.7243e-01],
            [3.74e-07, 5.7171e-01],
            [3.75e-07, 5.6212e-01],
            [3.76e-07, 5.5620e-01],
            [3.77e-07, 5.6922e-01],
            [3.78e-07, 5.4258e-01],
            [3.79e-07, 5.6375e-01],
            [3.80e-07, 5.5299e-01],
            [3.81e-07, 5.4737e-01],
            [3.82e-07, 5.4362e-01],
            [3.83e-07, 5.3931e-01],
            [3.84e-07, 5.4053e-01],
            [3.85e-07, 5.3298e-01],
            [3.86e-07, 5.4072e-01],
            [3.87e-07, 5.2577e-01],
            [3.88e-07, 5.2188e-01],
            [3.89e-07, 5.2355e-01],
            [3.90e-07, 5.2144e-01],
            [3.91e-07, 5.2419e-01],
            [3.92e-07, 5.2398e-01],
            [3.93e-07, 5.2200e-01],
            [3.94e-07, 5.1642e-01],
            [3.95e-07, 5.1080e-01],
            [3.96e-07, 5.0551e-01],
            [3.97e-07, 5.0449e-01],
            [3.98e-07, 5.1153e-01],
            [3.99e-07, 5.0258e-01],
            [4.00e-07, 5.0767e-01],
            [4.01e-07, 4.9791e-01],
            [4.02e-07, 4.9835e-01],
            [4.03e-07, 4.9056e-01],
            [4.04e-07, 4.9013e-01],
            [4.05e-07, 4.7759e-01],
            [4.06e-07, 4.9307e-01],
            [4.07e-07, 4.8737e-01],
            [4.08e-07, 4.9724e-01],
            [4.09e-07, 4.7913e-01],
            [4.10e-07, 4.7891e-01],
            [4.11e-07, 4.7081e-01],
            [4.12e-07, 4.7147e-01],
            [4.13e-07, 4.7218e-01],
            [4.14e-07, 4.6644e-01],
            [4.15e-07, 4.5862e-01],
            [4.16e-07, 4.6548e-01],
            [4.17e-07, 4.6763e-01],
            [4.18e-07, 4.5759e-01],
            [4.19e-07, 4.6239e-01],
            [4.20e-07, 4.4786e-01],
            [4.21e-07, 4.5065e-01],
            [4.22e-07, 4.4600e-01],
            [4.23e-07, 4.4124e-01],
            [4.24e-07, 4.4856e-01],
            [4.25e-07, 4.4620e-01],
            [4.26e-07, 4.4299e-01],
            [4.27e-07, 4.3794e-01],
            [4.28e-07, 4.4528e-01],
            [4.29e-07, 4.4492e-01],
            [4.30e-07, 4.3612e-01],
            [4.31e-07, 4.3065e-01],
            [4.32e-07, 4.3851e-01],
            [4.33e-07, 4.2952e-01],
            [4.34e-07, 4.2303e-01],
            [4.35e-07, 4.3569e-01],
            [4.36e-07, 4.3270e-01],
            [4.37e-07, 4.2945e-01],
            [4.38e-07, 4.3573e-01],
            [4.39e-07, 4.1314e-01],
            [4.40e-07, 4.1854e-01],
            [4.41e-07, 4.1404e-01],
            [4.42e-07, 4.2374e-01],
            [4.43e-07, 4.0759e-01],
            [4.44e-07, 4.1130e-01],
            [4.45e-07, 4.1088e-01],
            [4.46e-07, 4.0693e-01],
            [4.47e-07, 4.0986e-01],
            [4.48e-07, 4.0551e-01],
            [4.49e-07, 4.0090e-01],
            [4.50e-07, 4.0801e-01],
            [4.51e-07, 3.9305e-01],
            [4.52e-07, 3.9777e-01],
            [4.53e-07, 3.8838e-01],
            [4.54e-07, 3.9689e-01],
            [4.55e-07, 3.9532e-01],
            [4.56e-07, 3.9439e-01],
            [4.57e-07, 3.9685e-01],
            [4.58e-07, 3.9146e-01],
            [4.59e-07, 3.9276e-01],
            [4.60e-07, 3.8028e-01],
            [4.61e-07, 3.8954e-01],
            [4.62e-07, 3.8320e-01],
            [4.63e-07, 3.7083e-01],
            [4.64e-07, 3.6622e-01],
            [4.65e-07, 3.7319e-01],
            [4.66e-07, 3.6343e-01],
            [4.67e-07, 3.7019e-01],
            [4.68e-07, 3.6677e-01],
            [4.69e-07, 3.5868e-01],
            [4.70e-07, 3.6568e-01],
            [4.71e-07, 3.6860e-01],
            [4.72e-07, 3.6311e-01],
            [4.73e-07, 3.6526e-01],
            [4.74e-07, 3.6913e-01],
            [4.75e-07, 3.6756e-01],
            [4.76e-07, 3.5482e-01],
            [4.77e-07, 3.5982e-01],
            [4.78e-07, 3.6346e-01],
            [4.79e-07, 3.4881e-01],
            [4.80e-07, 3.4898e-01],
            [4.81e-07, 3.5451e-01],
            [4.82e-07, 3.4347e-01],
            [4.83e-07, 3.4594e-01],
            [4.84e-07, 3.4788e-01],
            [4.85e-07, 3.4820e-01],
            [4.86e-07, 3.5092e-01],
            [4.87e-07, 3.4020e-01],
            [4.88e-07, 3.4725e-01],
            [4.89e-07, 3.4035e-01],
            [4.90e-07, 3.4530e-01],
            [4.91e-07, 3.4238e-01],
            [4.92e-07, 3.3777e-01],
            [4.93e-07, 3.3994e-01],
            [4.94e-07, 3.3488e-01],
            [4.95e-07, 3.2334e-01],
            [4.96e-07, 3.3343e-01],
            [4.97e-07, 3.2973e-01],
            [4.98e-07, 3.3427e-01],
            [4.99e-07, 3.2357e-01],
            [5.00e-07, 3.1891e-01],
            [5.01e-07, 3.2254e-01],
            [5.02e-07, 3.2355e-01],
            [5.03e-07, 3.2666e-01],
            [5.04e-07, 3.2755e-01],
            [5.05e-07, 3.2289e-01],
            [5.06e-07, 3.1704e-01],
            [5.07e-07, 3.1394e-01],
            [5.08e-07, 3.0913e-01],
            [5.09e-07, 3.1200e-01],
            [5.10e-07, 3.1435e-01],
            [5.11e-07, 3.0396e-01],
            [5.12e-07, 3.1118e-01],
            [5.13e-07, 3.1324e-01],
            [5.14e-07, 3.0649e-01],
            [5.15e-07, 3.0311e-01],
            [5.16e-07, 3.0353e-01],
            [5.17e-07, 2.9753e-01],
            [5.18e-07, 3.0388e-01],
            [5.19e-07, 3.0171e-01],
            [5.20e-07, 2.9330e-01],
            [5.21e-07, 2.9376e-01],
            [5.22e-07, 2.9981e-01],
            [5.23e-07, 2.9965e-01],
            [5.24e-07, 3.0261e-01],
            [5.25e-07, 3.0403e-01],
            [5.26e-07, 2.9588e-01],
            [5.27e-07, 2.9290e-01],
            [5.28e-07, 2.9468e-01],
            [5.29e-07, 2.8785e-01],
            [5.30e-07, 2.8676e-01],
            [5.31e-07, 2.9459e-01],
            [5.32e-07, 2.8745e-01],
            [5.33e-07, 2.8914e-01],
            [5.34e-07, 2.8516e-01],
            [5.35e-07, 2.8132e-01],
            [5.36e-07, 2.8396e-01],
            [5.37e-07, 2.8710e-01],
            [5.38e-07, 2.8555e-01],
            [5.39e-07, 2.7691e-01],
            [5.40e-07, 2.7109e-01],
            [5.41e-07, 2.8156e-01],
            [5.42e-07, 2.8216e-01],
            [5.43e-07, 2.7978e-01],
            [5.44e-07, 2.7164e-01],
            [5.45e-07, 2.7663e-01],
            [5.46e-07, 2.7127e-01],
            [5.47e-07, 2.7519e-01],
            [5.48e-07, 2.7014e-01],
            [5.49e-07, 2.7481e-01],
            [5.50e-07, 2.6838e-01],
            [5.51e-07, 2.7720e-01],
            [5.52e-07, 2.6951e-01],
            [5.53e-07, 2.6849e-01],
            [5.54e-07, 2.5729e-01],
            [5.55e-07, 2.7241e-01],
            [5.56e-07, 2.5711e-01],
            [5.57e-07, 2.6681e-01],
            [5.58e-07, 2.6383e-01],
            [5.59e-07, 2.5731e-01],
            [5.60e-07, 2.6161e-01],
            [5.61e-07, 2.6008e-01],
            [5.62e-07, 2.5013e-01],
            [5.63e-07, 2.5611e-01],
            [5.64e-07, 2.6165e-01],
            [5.65e-07, 2.5259e-01],
            [5.66e-07, 2.5572e-01],
            [5.67e-07, 2.5091e-01],
            [5.68e-07, 2.4999e-01],
            [5.69e-07, 2.5034e-01],
            [5.70e-07, 2.5738e-01],
            [5.71e-07, 2.5091e-01],
            [5.72e-07, 2.4854e-01],
            [5.73e-07, 2.5210e-01],
            [5.74e-07, 2.4631e-01],
            [5.75e-07, 2.4731e-01],
            [5.76e-07, 2.5169e-01],
            [5.77e-07, 2.3965e-01],
            [5.78e-07, 2.4674e-01],
            [5.79e-07, 2.4167e-01],
            [5.80e-07, 2.4438e-01],
            [5.81e-07, 2.4992e-01],
            [5.82e-07, 2.3491e-01],
            [5.83e-07, 2.3900e-01],
            [5.84e-07, 2.4150e-01],
            [5.85e-07, 2.4002e-01],
            [5.86e-07, 2.4030e-01],
            [5.87e-07, 2.3881e-01],
            [5.88e-07, 2.2602e-01],
            [5.89e-07, 2.3387e-01],
            [5.90e-07, 2.3510e-01],
            [5.91e-07, 2.3363e-01],
            [5.92e-07, 2.3318e-01],
            [5.93e-07, 2.3095e-01],
            [5.94e-07, 2.3285e-01],
            [5.95e-07, 2.3149e-01],
            [5.96e-07, 2.3081e-01],
            [5.97e-07, 2.3014e-01],
            [5.98e-07, 2.2511e-01],
            [5.99e-07, 2.2918e-01],
            [6.00e-07, 2.2457e-01],
            [6.01e-07, 2.2770e-01],
            [6.02e-07, 2.2119e-01],
            [6.03e-07, 2.2137e-01],
            [6.04e-07, 2.1966e-01],
            [6.05e-07, 2.1825e-01],
            [6.06e-07, 2.2485e-01],
            [6.07e-07, 2.2080e-01],
            [6.08e-07, 2.1833e-01],
            [6.09e-07, 2.2014e-01],
            [6.10e-07, 2.2495e-01],
            [6.11e-07, 2.2511e-01],
            [6.12e-07, 2.1296e-01],
            [6.13e-07, 2.1741e-01],
            [6.14e-07, 2.2021e-01],
            [6.15e-07, 2.2493e-01],
            [6.16e-07, 2.1776e-01],
            [6.17e-07, 2.1389e-01],
            [6.18e-07, 2.1659e-01],
            [6.19e-07, 2.1833e-01],
            [6.20e-07, 2.1593e-01],
            [6.21e-07, 2.1040e-01],
            [6.22e-07, 2.1672e-01],
            [6.23e-07, 2.0300e-01],
            [6.24e-07, 2.1150e-01],
            [6.25e-07, 2.0970e-01],
            [6.26e-07, 2.1224e-01],
            [6.27e-07, 2.1737e-01],
            [6.28e-07, 2.0815e-01],
            [6.29e-07, 2.0525e-01],
            [6.30e-07, 2.0233e-01],
            [6.31e-07, 1.9884e-01],
            [6.32e-07, 2.0204e-01],
            [6.33e-07, 2.0522e-01],
            [6.34e-07, 2.0327e-01],
            [6.35e-07, 2.0265e-01],
            [6.36e-07, 2.0709e-01],
            [6.37e-07, 2.0553e-01],
            [6.38e-07, 1.9528e-01],
            [6.39e-07, 1.9930e-01],
            [6.40e-07, 1.9435e-01],
            [6.41e-07, 1.9827e-01],
            [6.42e-07, 1.9712e-01],
            [6.43e-07, 1.9904e-01],
            [6.44e-07, 1.9574e-01],
            [6.45e-07, 2.0105e-01],
            [6.46e-07, 1.9474e-01],
            [6.47e-07, 1.9877e-01],
            [6.48e-07, 1.9287e-01],
            [6.49e-07, 1.9555e-01],
            [6.50e-07, 1.9289e-01],
            [6.51e-07, 1.9019e-01],
            [6.52e-07, 1.9188e-01],
            [6.53e-07, 1.9343e-01],
            [6.54e-07, 1.9083e-01],
            [6.55e-07, 1.9587e-01],
            [6.56e-07, 1.8730e-01],
            [6.57e-07, 1.8752e-01],
            [6.58e-07, 1.8678e-01],
            [6.59e-07, 1.8459e-01],
            [6.60e-07, 1.9183e-01],
            [6.61e-07, 1.9074e-01],
            [6.62e-07, 1.8885e-01],
            [6.63e-07, 1.8332e-01],
            [6.64e-07, 1.8706e-01],
            [6.65e-07, 1.8194e-01],
            [6.66e-07, 1.7969e-01],
            [6.67e-07, 1.8880e-01],
            [6.68e-07, 1.8222e-01],
            [6.69e-07, 1.8813e-01],
            [6.70e-07, 1.8261e-01],
            [6.71e-07, 1.8192e-01],
            [6.72e-07, 1.8004e-01],
            [6.73e-07, 1.7930e-01],
            [6.74e-07, 1.8861e-01],
            [6.75e-07, 1.7986e-01],
            [6.76e-07, 1.7807e-01],
            [6.77e-07, 1.7779e-01],
            [6.78e-07, 1.7966e-01],
            [6.79e-07, 1.8107e-01],
            [6.80e-07, 1.7487e-01],
            [6.81e-07, 1.7990e-01],
            [6.82e-07, 1.7690e-01],
            [6.83e-07, 1.7195e-01],
            [6.84e-07, 1.7443e-01],
            [6.85e-07, 1.8335e-01],
            [6.86e-07, 1.7180e-01],
            [6.87e-07, 1.7222e-01],
            [6.88e-07, 1.6997e-01],
            [6.89e-07, 1.6884e-01],
            [6.90e-07, 1.7994e-01],
            [6.91e-07, 1.7345e-01],
            [6.92e-07, 1.7670e-01],
            [6.93e-07, 1.7267e-01],
            [6.94e-07, 1.7098e-01],
            [6.95e-07, 1.6919e-01],
            [6.96e-07, 1.7061e-01],
            [6.97e-07, 1.6859e-01],
            [6.98e-07, 1.6932e-01],
            [6.99e-07, 1.2294e-01],
        ]
    )

    _cer[70] = np.array(
        [
            [2.50e-07, 6.678e-04],
            [2.51e-07, 0.000e00],
            [2.52e-07, 0.000e00],
            [2.53e-07, 0.000e00],
            [2.54e-07, 0.000e00],
            [2.55e-07, 0.000e00],
            [2.56e-07, 0.000e00],
            [2.57e-07, 0.000e00],
            [2.58e-07, 0.000e00],
            [2.59e-07, 0.000e00],
            [2.60e-07, 0.000e00],
            [2.61e-07, 6.676e-04],
            [2.62e-07, 0.000e00],
            [2.63e-07, 0.000e00],
            [2.64e-07, 0.000e00],
            [2.65e-07, 1.335e-03],
            [2.66e-07, 1.334e-03],
            [2.67e-07, 3.333e-03],
            [2.68e-07, 3.335e-03],
            [2.69e-07, 2.002e-03],
            [2.70e-07, 3.333e-03],
            [2.71e-07, 3.333e-03],
            [2.72e-07, 6.006e-03],
            [2.73e-07, 3.997e-03],
            [2.74e-07, 5.998e-03],
            [2.75e-07, 1.468e-02],
            [2.76e-07, 1.268e-02],
            [2.77e-07, 8.659e-03],
            [2.78e-07, 1.133e-02],
            [2.79e-07, 2.399e-02],
            [2.80e-07, 2.467e-02],
            [2.81e-07, 3.861e-02],
            [2.82e-07, 4.332e-02],
            [2.83e-07, 4.795e-02],
            [2.84e-07, 3.992e-02],
            [2.85e-07, 4.661e-02],
            [2.86e-07, 6.459e-02],
            [2.87e-07, 6.803e-02],
            [2.88e-07, 9.454e-02],
            [2.89e-07, 1.133e-01],
            [2.90e-07, 1.212e-01],
            [2.91e-07, 1.258e-01],
            [2.92e-07, 1.178e-01],
            [2.93e-07, 1.388e-01],
            [2.94e-07, 1.532e-01],
            [2.95e-07, 1.485e-01],
            [2.96e-07, 1.612e-01],
            [2.97e-07, 1.598e-01],
            [2.98e-07, 1.925e-01],
            [2.99e-07, 1.799e-01],
            [3.00e-07, 2.044e-01],
            [3.01e-07, 2.135e-01],
            [3.02e-07, 2.252e-01],
            [3.03e-07, 2.400e-01],
            [3.04e-07, 2.600e-01],
            [3.05e-07, 2.617e-01],
            [3.06e-07, 2.845e-01],
            [3.07e-07, 2.989e-01],
            [3.08e-07, 3.150e-01],
            [3.09e-07, 3.659e-01],
            [3.10e-07, 3.856e-01],
            [3.11e-07, 3.764e-01],
            [3.12e-07, 3.605e-01],
            [3.13e-07, 4.135e-01],
            [3.14e-07, 4.118e-01],
            [3.15e-07, 4.156e-01],
            [3.16e-07, 4.170e-01],
            [3.17e-07, 4.361e-01],
            [3.18e-07, 4.443e-01],
            [3.19e-07, 4.343e-01],
            [3.20e-07, 4.565e-01],
            [3.21e-07, 4.353e-01],
            [3.22e-07, 4.596e-01],
            [3.23e-07, 5.075e-01],
            [3.24e-07, 5.049e-01],
            [3.25e-07, 4.998e-01],
            [3.26e-07, 4.963e-01],
            [3.27e-07, 5.729e-01],
            [3.28e-07, 5.158e-01],
            [3.29e-07, 5.258e-01],
            [3.30e-07, 5.336e-01],
            [3.31e-07, 5.521e-01],
            [3.32e-07, 5.686e-01],
            [3.33e-07, 6.082e-01],
            [3.34e-07, 5.892e-01],
            [3.35e-07, 5.612e-01],
            [3.36e-07, 5.939e-01],
            [3.37e-07, 6.303e-01],
            [3.38e-07, 6.080e-01],
            [3.39e-07, 6.262e-01],
            [3.40e-07, 6.244e-01],
            [3.41e-07, 6.126e-01],
            [3.42e-07, 6.376e-01],
            [3.43e-07, 6.324e-01],
            [3.44e-07, 6.343e-01],
            [3.45e-07, 6.582e-01],
            [3.46e-07, 6.586e-01],
            [3.47e-07, 6.715e-01],
            [3.48e-07, 6.775e-01],
            [3.49e-07, 6.993e-01],
            [3.50e-07, 6.682e-01],
            [3.51e-07, 7.162e-01],
            [3.52e-07, 7.228e-01],
            [3.53e-07, 7.080e-01],
            [3.54e-07, 7.283e-01],
            [3.55e-07, 6.980e-01],
            [3.56e-07, 7.427e-01],
            [3.57e-07, 7.271e-01],
            [3.58e-07, 7.066e-01],
            [3.59e-07, 7.193e-01],
            [3.60e-07, 7.714e-01],
            [3.61e-07, 7.200e-01],
            [3.62e-07, 7.561e-01],
            [3.63e-07, 7.216e-01],
            [3.64e-07, 7.621e-01],
            [3.65e-07, 7.518e-01],
            [3.66e-07, 7.764e-01],
            [3.67e-07, 7.670e-01],
            [3.68e-07, 7.824e-01],
            [3.69e-07, 8.040e-01],
            [3.70e-07, 7.930e-01],
            [3.71e-07, 8.036e-01],
            [3.72e-07, 7.695e-01],
            [3.73e-07, 7.803e-01],
            [3.74e-07, 8.131e-01],
            [3.75e-07, 7.900e-01],
            [3.76e-07, 8.427e-01],
            [3.77e-07, 7.772e-01],
            [3.78e-07, 8.107e-01],
            [3.79e-07, 8.506e-01],
            [3.80e-07, 8.279e-01],
            [3.81e-07, 8.368e-01],
            [3.82e-07, 8.898e-01],
            [3.83e-07, 8.420e-01],
            [3.84e-07, 8.291e-01],
            [3.85e-07, 8.519e-01],
            [3.86e-07, 8.275e-01],
            [3.87e-07, 8.880e-01],
            [3.88e-07, 8.609e-01],
            [3.89e-07, 8.339e-01],
            [3.90e-07, 8.560e-01],
            [3.91e-07, 8.562e-01],
            [3.92e-07, 8.911e-01],
            [3.93e-07, 8.668e-01],
            [3.94e-07, 8.846e-01],
            [3.95e-07, 8.849e-01],
            [3.96e-07, 9.105e-01],
            [3.97e-07, 8.728e-01],
            [3.98e-07, 8.701e-01],
            [3.99e-07, 8.894e-01],
            [4.00e-07, 9.411e-01],
            [4.01e-07, 8.873e-01],
            [4.02e-07, 9.138e-01],
            [4.03e-07, 9.084e-01],
            [4.04e-07, 9.553e-01],
            [4.05e-07, 9.076e-01],
            [4.06e-07, 9.667e-01],
            [4.07e-07, 8.981e-01],
            [4.08e-07, 9.301e-01],
            [4.09e-07, 9.369e-01],
            [4.10e-07, 9.338e-01],
            [4.11e-07, 9.037e-01],
            [4.12e-07, 9.094e-01],
            [4.13e-07, 9.154e-01],
            [4.14e-07, 9.254e-01],
            [4.15e-07, 9.540e-01],
            [4.16e-07, 9.155e-01],
            [4.17e-07, 9.569e-01],
            [4.18e-07, 9.272e-01],
            [4.19e-07, 9.209e-01],
            [4.20e-07, 8.999e-01],
            [4.21e-07, 9.150e-01],
            [4.22e-07, 9.252e-01],
            [4.23e-07, 9.073e-01],
            [4.24e-07, 8.807e-01],
            [4.25e-07, 8.707e-01],
            [4.26e-07, 9.313e-01],
            [4.27e-07, 9.621e-01],
            [4.28e-07, 9.331e-01],
            [4.29e-07, 9.334e-01],
            [4.30e-07, 9.336e-01],
            [4.31e-07, 9.507e-01],
            [4.32e-07, 9.610e-01],
            [4.33e-07, 9.722e-01],
            [4.34e-07, 9.590e-01],
            [4.35e-07, 9.170e-01],
            [4.36e-07, 9.897e-01],
            [4.37e-07, 9.472e-01],
            [4.38e-07, 9.443e-01],
            [4.39e-07, 9.866e-01],
            [4.40e-07, 9.438e-01],
            [4.41e-07, 9.093e-01],
            [4.42e-07, 9.132e-01],
            [4.43e-07, 9.581e-01],
            [4.44e-07, 9.610e-01],
            [4.45e-07, 1.000e00],
            [4.46e-07, 9.351e-01],
            [4.47e-07, 9.366e-01],
            [4.48e-07, 9.496e-01],
            [4.49e-07, 9.142e-01],
            [4.50e-07, 9.786e-01],
            [4.51e-07, 9.205e-01],
            [4.52e-07, 9.267e-01],
            [4.53e-07, 9.476e-01],
            [4.54e-07, 9.000e-01],
            [4.55e-07, 9.687e-01],
            [4.56e-07, 8.967e-01],
            [4.57e-07, 9.214e-01],
            [4.58e-07, 9.234e-01],
            [4.59e-07, 9.699e-01],
            [4.60e-07, 9.351e-01],
            [4.61e-07, 9.237e-01],
            [4.62e-07, 9.543e-01],
            [4.63e-07, 8.981e-01],
            [4.64e-07, 9.335e-01],
            [4.65e-07, 9.059e-01],
            [4.66e-07, 8.830e-01],
            [4.67e-07, 9.329e-01],
            [4.68e-07, 9.278e-01],
            [4.69e-07, 9.581e-01],
            [4.70e-07, 9.583e-01],
            [4.71e-07, 8.792e-01],
            [4.72e-07, 9.098e-01],
            [4.73e-07, 9.213e-01],
            [4.74e-07, 9.129e-01],
            [4.75e-07, 9.299e-01],
            [4.76e-07, 9.025e-01],
            [4.77e-07, 9.158e-01],
            [4.78e-07, 9.220e-01],
            [4.79e-07, 9.713e-01],
            [4.80e-07, 9.387e-01],
            [4.81e-07, 8.840e-01],
            [4.82e-07, 9.331e-01],
            [4.83e-07, 9.368e-01],
            [4.84e-07, 8.892e-01],
            [4.85e-07, 8.926e-01],
            [4.86e-07, 9.058e-01],
            [4.87e-07, 9.330e-01],
            [4.88e-07, 9.246e-01],
            [4.89e-07, 9.104e-01],
            [4.90e-07, 9.622e-01],
            [4.91e-07, 8.455e-01],
            [4.92e-07, 9.020e-01],
            [4.93e-07, 8.890e-01],
            [4.94e-07, 9.234e-01],
            [4.95e-07, 9.293e-01],
            [4.96e-07, 8.985e-01],
            [4.97e-07, 8.948e-01],
            [4.98e-07, 8.929e-01],
            [4.99e-07, 8.872e-01],
            [5.00e-07, 8.832e-01],
            [5.01e-07, 8.731e-01],
            [5.02e-07, 9.002e-01],
            [5.03e-07, 8.823e-01],
            [5.04e-07, 9.021e-01],
            [5.05e-07, 8.619e-01],
            [5.06e-07, 8.948e-01],
            [5.07e-07, 8.950e-01],
            [5.08e-07, 8.972e-01],
            [5.09e-07, 8.369e-01],
            [5.10e-07, 8.422e-01],
            [5.11e-07, 8.895e-01],
            [5.12e-07, 8.882e-01],
            [5.13e-07, 8.613e-01],
            [5.14e-07, 8.603e-01],
            [5.15e-07, 8.615e-01],
            [5.16e-07, 8.740e-01],
            [5.17e-07, 8.617e-01],
            [5.18e-07, 8.493e-01],
            [5.19e-07, 8.757e-01],
            [5.20e-07, 8.501e-01],
            [5.21e-07, 8.556e-01],
            [5.22e-07, 8.638e-01],
            [5.23e-07, 8.464e-01],
            [5.24e-07, 8.808e-01],
            [5.25e-07, 8.621e-01],
            [5.26e-07, 8.614e-01],
            [5.27e-07, 9.045e-01],
            [5.28e-07, 8.740e-01],
            [5.29e-07, 8.241e-01],
            [5.30e-07, 8.513e-01],
            [5.31e-07, 8.850e-01],
            [5.32e-07, 8.411e-01],
            [5.33e-07, 8.869e-01],
            [5.34e-07, 8.530e-01],
            [5.35e-07, 8.638e-01],
            [5.36e-07, 8.432e-01],
            [5.37e-07, 8.678e-01],
            [5.38e-07, 8.388e-01],
            [5.39e-07, 8.386e-01],
            [5.40e-07, 8.493e-01],
            [5.41e-07, 8.831e-01],
            [5.42e-07, 8.377e-01],
            [5.43e-07, 8.577e-01],
            [5.44e-07, 8.534e-01],
            [5.45e-07, 7.952e-01],
            [5.46e-07, 8.055e-01],
            [5.47e-07, 8.118e-01],
            [5.48e-07, 8.170e-01],
            [5.49e-07, 8.323e-01],
            [5.50e-07, 8.742e-01],
            [5.51e-07, 7.828e-01],
            [5.52e-07, 8.004e-01],
            [5.53e-07, 8.560e-01],
            [5.54e-07, 7.824e-01],
            [5.55e-07, 8.171e-01],
            [5.56e-07, 8.094e-01],
            [5.57e-07, 8.240e-01],
            [5.58e-07, 7.926e-01],
            [5.59e-07, 7.837e-01],
            [5.60e-07, 7.852e-01],
            [5.61e-07, 8.014e-01],
            [5.62e-07, 8.067e-01],
            [5.63e-07, 8.001e-01],
            [5.64e-07, 7.770e-01],
            [5.65e-07, 7.779e-01],
            [5.66e-07, 8.130e-01],
            [5.67e-07, 8.373e-01],
            [5.68e-07, 7.972e-01],
            [5.69e-07, 7.803e-01],
            [5.70e-07, 7.491e-01],
            [5.71e-07, 7.952e-01],
            [5.72e-07, 7.981e-01],
            [5.73e-07, 7.573e-01],
            [5.74e-07, 7.607e-01],
            [5.75e-07, 7.260e-01],
            [5.76e-07, 8.025e-01],
            [5.77e-07, 8.007e-01],
            [5.78e-07, 7.791e-01],
            [5.79e-07, 7.703e-01],
            [5.80e-07, 7.843e-01],
            [5.81e-07, 7.696e-01],
            [5.82e-07, 7.575e-01],
            [5.83e-07, 7.667e-01],
            [5.84e-07, 7.714e-01],
            [5.85e-07, 7.981e-01],
            [5.86e-07, 8.054e-01],
            [5.87e-07, 7.615e-01],
            [5.88e-07, 7.959e-01],
            [5.89e-07, 7.499e-01],
            [5.90e-07, 7.455e-01],
            [5.91e-07, 7.184e-01],
            [5.92e-07, 6.950e-01],
            [5.93e-07, 7.220e-01],
            [5.94e-07, 7.234e-01],
            [5.95e-07, 7.216e-01],
            [5.96e-07, 7.133e-01],
            [5.97e-07, 7.491e-01],
            [5.98e-07, 7.207e-01],
            [5.99e-07, 7.827e-01],
            [6.00e-07, 7.307e-01],
            [6.01e-07, 7.296e-01],
            [6.02e-07, 7.272e-01],
            [6.03e-07, 7.281e-01],
            [6.04e-07, 7.073e-01],
            [6.05e-07, 7.152e-01],
            [6.06e-07, 7.451e-01],
            [6.07e-07, 7.114e-01],
            [6.08e-07, 7.389e-01],
            [6.09e-07, 6.850e-01],
            [6.10e-07, 7.079e-01],
            [6.11e-07, 6.982e-01],
            [6.12e-07, 7.309e-01],
            [6.13e-07, 7.036e-01],
            [6.14e-07, 7.231e-01],
            [6.15e-07, 7.220e-01],
            [6.16e-07, 6.412e-01],
            [6.17e-07, 6.743e-01],
            [6.18e-07, 7.345e-01],
            [6.19e-07, 6.633e-01],
            [6.20e-07, 6.784e-01],
            [6.21e-07, 7.289e-01],
            [6.22e-07, 7.177e-01],
            [6.23e-07, 7.014e-01],
            [6.24e-07, 6.880e-01],
            [6.25e-07, 6.961e-01],
            [6.26e-07, 6.852e-01],
            [6.27e-07, 6.569e-01],
            [6.28e-07, 6.980e-01],
            [6.29e-07, 6.809e-01],
            [6.30e-07, 7.000e-01],
            [6.31e-07, 6.955e-01],
            [6.32e-07, 6.853e-01],
            [6.33e-07, 6.933e-01],
            [6.34e-07, 6.649e-01],
            [6.35e-07, 6.556e-01],
            [6.36e-07, 6.751e-01],
            [6.37e-07, 6.828e-01],
            [6.38e-07, 6.566e-01],
            [6.39e-07, 6.656e-01],
            [6.40e-07, 6.464e-01],
            [6.41e-07, 6.685e-01],
            [6.42e-07, 6.526e-01],
            [6.43e-07, 6.607e-01],
            [6.44e-07, 6.633e-01],
            [6.45e-07, 6.535e-01],
            [6.46e-07, 6.948e-01],
            [6.47e-07, 6.537e-01],
            [6.48e-07, 6.894e-01],
            [6.49e-07, 6.674e-01],
            [6.50e-07, 6.524e-01],
            [6.51e-07, 6.388e-01],
            [6.52e-07, 6.709e-01],
            [6.53e-07, 6.555e-01],
            [6.54e-07, 6.396e-01],
            [6.55e-07, 6.035e-01],
            [6.56e-07, 6.260e-01],
            [6.57e-07, 6.569e-01],
            [6.58e-07, 6.016e-01],
            [6.59e-07, 6.385e-01],
            [6.60e-07, 6.399e-01],
            [6.61e-07, 6.363e-01],
            [6.62e-07, 6.243e-01],
            [6.63e-07, 6.383e-01],
            [6.64e-07, 6.604e-01],
            [6.65e-07, 6.454e-01],
            [6.66e-07, 6.437e-01],
            [6.67e-07, 6.310e-01],
            [6.68e-07, 6.871e-01],
            [6.69e-07, 6.174e-01],
            [6.70e-07, 6.384e-01],
            [6.71e-07, 6.185e-01],
            [6.72e-07, 6.460e-01],
            [6.73e-07, 6.379e-01],
            [6.74e-07, 6.102e-01],
            [6.75e-07, 6.429e-01],
            [6.76e-07, 6.157e-01],
            [6.77e-07, 6.009e-01],
            [6.78e-07, 6.051e-01],
            [6.79e-07, 6.006e-01],
            [6.80e-07, 6.213e-01],
            [6.81e-07, 6.107e-01],
            [6.82e-07, 6.070e-01],
            [6.83e-07, 6.290e-01],
            [6.84e-07, 5.875e-01],
            [6.85e-07, 5.975e-01],
            [6.86e-07, 5.950e-01],
            [6.87e-07, 6.104e-01],
            [6.88e-07, 6.321e-01],
            [6.89e-07, 5.803e-01],
            [6.90e-07, 6.116e-01],
            [6.91e-07, 5.943e-01],
            [6.92e-07, 5.995e-01],
            [6.93e-07, 5.985e-01],
            [6.94e-07, 5.862e-01],
            [6.95e-07, 5.989e-01],
            [6.96e-07, 5.882e-01],
            [6.97e-07, 6.204e-01],
            [6.98e-07, 6.037e-01],
            [6.99e-07, 5.172e-01],
        ]
    )

    key = zenith_distance_deg

    assert utils.is_strictly_monotonic_increasing(_cer[key][:, 0])

    return {
        "wavelength": _cer[key][:, 0],
        "value": _cer[key][:, 1],
        "units": ["m", "1"],
        "reference": (
            "{zenith_"
            + str(key)
            + "deg}"
            + _corsika2018cherenkov.format(thetap=float(key))
        ),
    }


def _read_corsika_photons(path):
    corsoka_photons = np.fromfile(path, dtype=np.float32)
    n = corsoka_photons.shape[0]
    return corsoka_photons.reshape(n // 8, 8)


def _cherenkov_spectrum_from_corsika_photon_block(
    path, bins=10, use_weights=True
):
    prng = np.random.default_rng()

    photon_weight_idx = 6
    wavelength_idx = 7

    corsoka_photons = _read_corsika_photons(path)
    wavelength = np.abs(corsoka_photons[:, wavelength_idx])
    wavelength = (
        wavelength
        + prng.uniform(size=wavelength.shape[0])
        - 0.5 * np.ones(wavelength.shape[0])
    )

    wavelength *= 1e-9  # to meters
    if use_weights:
        weights = corsoka_photons[:, photon_weight_idx]
        return np.histogram(a=wavelength, bins=bins, weights=weights)
    else:
        return np.histogram(a=wavelength, bins=bins)
