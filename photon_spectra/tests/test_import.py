import photon_spectra


def test_version():
    vstr = photon_spectra.__version__
    assert vstr
    assert len(str.split(vstr, ".")) == 3
