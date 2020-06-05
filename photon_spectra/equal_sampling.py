import cherenkov_la_palma
import cherenkov_cta_chile
import hamamatsu_r11920_100_05 as _hamamatsu_r11920_100_05
import hamamatsu_s10362_33_050c
import nsb_la_palma_2002_hofmann
import nsb_la_palma_2013_benn
import veritas_nsb_filter_2015
import cta_mirrors
import cta_windows
import hess_mirrors
import silica_glass_suprasil_311_312_313
import numpy as np

wavelength = np.linspace(200e-9, 700e-9, 501)

cherenkov_histogram_on_ground = np.interp(
    x=wavelength,
    xp=cherenkov_la_palma.cherenkov_histogram_on_ground[:, 0],
    fp=cherenkov_la_palma.cherenkov_histogram_on_ground[:, 1],)

cherenkov_la_palma_zd_70deg = np.interp(
    x=wavelength,
    xp=cherenkov_la_palma.cherenkov_histogram_on_ground_zenith_distance_70deg[
        :, 0],
    fp=cherenkov_la_palma.cherenkov_histogram_on_ground_zenith_distance_70deg[
        :, 1],)

cherenkov_gamma_below_5gev_5000m_asl = np.interp(
    x=wavelength,
    xp=cherenkov_cta_chile.cherenkov_gamma_below_5gev_5000m_asl[:, 0],
    fp=cherenkov_cta_chile.cherenkov_gamma_below_5gev_5000m_asl[:, 1],)

hamamatsu_s10362_33_050c = np.interp(
    x=wavelength,
    xp=hamamatsu_s10362_33_050c.hamamatsu_s10362_33_050c[:, 0],
    fp=hamamatsu_s10362_33_050c.hamamatsu_s10362_33_050c[:, 1],)

hamamatsu_r11920_100_05_sample = np.interp(
    x=wavelength,
    xp=_hamamatsu_r11920_100_05.hamamatsu_r11920_100_05_sample[:, 0],
    fp=_hamamatsu_r11920_100_05.hamamatsu_r11920_100_05_sample[:, 1],)

hamamatsu_r11920_100_05 = np.interp(
    x=wavelength,
    xp=_hamamatsu_r11920_100_05.hamamatsu_r11920_100_05[:, 0],
    fp=_hamamatsu_r11920_100_05.hamamatsu_r11920_100_05[:, 1],)

nsb_diff_la_palma_2002_hofmann = np.interp(
    x=wavelength,
    xp=nsb_la_palma_2002_hofmann.la_palma_2002_hofmann[:, 0],
    fp=nsb_la_palma_2002_hofmann.la_palma_2002_hofmann[:, 1],)
nsb_diff_la_palma_2002_hofmann[wavelength < 362e-9] = np.nan
nsb_diff_la_palma_2002_hofmann[wavelength > 550e-9] = np.nan

nsb_diff_la_palma_benn = np.interp(
    x=wavelength,
    xp=nsb_la_palma_2013_benn.la_palma_2013_benn[:, 0],
    fp=nsb_la_palma_2013_benn.la_palma_2013_benn[:, 1],)

veritas_nsb_filter_2015 = np.interp(
    x=wavelength,
    xp=veritas_nsb_filter_2015.veritas_nsb_filter_2015[:, 0],
    fp=veritas_nsb_filter_2015.veritas_nsb_filter_2015[:, 1],)

mst_dielectric_before = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_dielectric_before[:, 0],
    fp=cta_mirrors.mst_dielectric_before[:, 1],)

mst_dielectric_after = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_dielectric_after[:, 0],
    fp=cta_mirrors.mst_dielectric_after[:, 1],)

mst_Al_SiO2_before = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_Al_SiO2_before[:, 0],
    fp=cta_mirrors.mst_Al_SiO2_before[:, 1],)

mst_Al_SiO2_after = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_Al_SiO2_after[:, 0],
    fp=cta_mirrors.mst_Al_SiO2_after[:, 1],)

mst_Al_SiO2_HfO2_SiO2_before = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_Al_SiO2_HfO2_SiO2_before[:, 0],
    fp=cta_mirrors.mst_Al_SiO2_HfO2_SiO2_before[:, 1],)

mst_Al_SiO2_HfO2_SiO2_after = np.interp(
    x=wavelength,
    xp=cta_mirrors.mst_Al_SiO2_HfO2_SiO2_after[:, 0],
    fp=cta_mirrors.mst_Al_SiO2_HfO2_SiO2_after[:, 1],)

astri_SiO2_mixed_multilayer_yellow = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_SiO2_mixed_multilayer_yellow[:, 0],
    fp=cta_mirrors.astri_SiO2_mixed_multilayer_yellow[:, 1],)

astri_SiO2_TiO2_mulitlayer = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_SiO2_TiO2_mulitlayer[:, 0],
    fp=cta_mirrors.astri_SiO2_TiO2_mulitlayer[:, 1],)

astri_SiO2_mixed_multilayer_orange = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_SiO2_mixed_multilayer_orange[:, 0],
    fp=cta_mirrors.astri_SiO2_mixed_multilayer_orange[:, 1],)

astri_Al_SiO2 = np.interp(
    x=wavelength,
    xp=cta_mirrors.astri_Al_SiO2[:, 0],
    fp=cta_mirrors.astri_Al_SiO2[:, 1],)

cta_mst_flash_cam_window_transmission = np.interp(
    x=wavelength,
    xp=cta_windows.cta_flash_cam_window_transmisson[:, 0],
    fp=cta_windows.cta_flash_cam_window_transmisson[:, 1],)

hess_ct5_mirror_degraded = np.interp(
    x=wavelength,
    xp=hess_mirrors.hess_ct5_mirror_degraded[:, 0],
    fp=hess_mirrors.hess_ct5_mirror_degraded[:, 1],)

suprasil_311_312_313_refraction = np.interp(
    x=wavelength,
    xp=silica_glass_suprasil_311_312_313.suprasil_refractive_index[:, 0],
    fp=silica_glass_suprasil_311_312_313.suprasil_refractive_index[:, 1],)

suprasil_311_312_313_transmission_incl_Fresnel = np.interp(
    x=wavelength,
    xp=silica_glass_suprasil_311_312_313.heraeus_silica_glass_suprasil_311_312_313_transmission[:, 0],
    fp=silica_glass_suprasil_311_312_313.heraeus_silica_glass_suprasil_311_312_313_transmission[:, 1],)

suprasil_311_312_313_transmission_only_Fresnel = np.interp(
    x=wavelength,
    xp=silica_glass_suprasil_311_312_313.fresnell_reflection_losses[:, 0],
    fp=silica_glass_suprasil_311_312_313.fresnell_reflection_losses[:, 1],)
