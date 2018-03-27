import equal_sampling as es


plt.figure()
lbenn, = plt.plot(
    es.wavelength,
    es.nsb_diff_la_palma_benn,
    label='night-sky-background, La Palma, Benn')
lhoff, = plt.plot(
    es.wavelength,
    es.nsb_diff_la_palma_2002_hoffmann,
    label='night-sky-background, La Palma, Hoffmann')
plt.semilogy()
plt.ylabel('differential flux/(m^-2 sr^-1 m^-1)')
plt.xlabel('wavelength/m')
plt.legend(handles=[lbenn, lhoff])
plt.savefig('./readme/nsb.png')

plt.figure()
lsipm, = plt.plot(es.wavelength, es.hamamatsu_s10362_33_050c, label='FACT SiPM')
lpmt, = plt.plot(es.wavelength, es.hamamatsu_r11920_100_05, label='CTA LST PMT')
plt.ylabel('photon-detection-efficiency/1')
plt.xlabel('wavelength/m')
plt.legend(handles=[lsipm, lpmt])
plt.savefig('./readme/pde.png')

plt.figure()
lcer, = plt.plot(
    es.wavelength,
    es.cherenkov_histogram_on_ground,
	label='3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 0deg')
lcer70, = plt.plot(
    es.wavelength,
    es.cherenkov_la_palma_zd_70deg,
	label='3TeV gamma, Cherenkov La Palma, 2200m asl, Zd: 70deg')
plt.ylabel('relative/1')
plt.xlabel('wavelength/m')
plt.legend(handles=[lcer, lcer70])
plt.savefig('./readme/cherenkov.png')

plt.figure()
lfilter, = plt.plot(
    es.wavelength,
    es.veritas_nsb_filter_2015,
    label='VERITAS night-sky-background filter')
plt.ylabel('transmission/1')
plt.xlabel('wavelength/m')
plt.legend(handles=[lfilter])
plt.savefig('./readme/transmission.png')
plt.close('all')



plt.figure(figsize=(16,9))
l0, = plt.plot(
    es.wavelength,
    es.mst_dielectric,
    label='CTA MST dielectric')
l1, = plt.plot(
    es.wavelength,
    es.mst_Al_SiO2_HfO2_SiO2_before,
    label='CTA MST Al SiO2 HfO2 before')
l2, = plt.plot(
    es.wavelength,
    es.mst_Al_SiO2_before,
    label='CTA MST Al SiO2 before')
l3, = plt.plot(
    es.wavelength,
    es.astri_SiO2_mixed_multilayer_yellow,
    label='CTA ASTRI SiO2 mixed multi. yellow')
l4, = plt.plot(
    es.wavelength,
    es.astri_SiO2_TiO2_mulitlayer,
    label='CTA ASTRI SiO2 TiO2 multi.')
l5, = plt.plot(
    es.wavelength,
    es.astri_SiO2_mixed_multilayer_orange,
    label='CTA ASTRI SiO2 mixed multi. orange')
l6, = plt.plot(
    es.wavelength,
    es.astri_Al_SiO2,
    label='CTA ASTRI Al SiO2')
plt.ylabel('reflectivity/1')
plt.xlabel('wavelength/m')
plt.legend(handles=[l0, l1, l2, l3, l4, l5, l6])
plt.savefig('./readme/cta_mirrors.png')