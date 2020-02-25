#plota uma imagem fits usando suas informações para criar o tamanho dos eixos. 
from matplotlib import pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from astropy.utils.data import get_pkg_data_filename
from mpl_toolkits.axes_grid.anchored_artists import AnchoredText

filename = get_pkg_data_filename('teste.fits') #Imagem do astro
fits.info(filename)

hdu = fits.open(filename)[0]
wcs = WCS(hdu.header)

fig = plt.figure()
ax = fig.add_subplot(111, projection=wcs)
plt.imshow(hdu.data, origin='lower', cmap='gray')
plt.title('CTS1011') 
plt.xlabel('RA')
plt.ylabel('Dec')
at = AnchoredText('parsec',prop=dict(size=9), frameon=True,loc=3,)
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)
#plt.savefig("figura.eps") #Tirar o '#' se quiser salvar a imagem automaticamente
plt.show()
plt.close()
