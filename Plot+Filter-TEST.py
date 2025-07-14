import numpy as np
import matplotlib.pyplot as plt
import healpy as hp
import astropy.io.fits as fits


def plot_map(input_map, title='Filtered Map'):
    """
    Plots the input map using Healpy.
    
    Parameters:
    input_map (numpy.ndarray): The map to plot.
    title (str): The title of the plot.

    REQUIRES plt.show() AFTER CALLING THIS FUNCTION
    """
    fig = plt.figure(figsize=(8, 6))

    hp.mollview(input_map, title=title, fig=fig)
    

def fits_file_iterate(base_path, index_list_primary, index_list_secondary=[""], secondary_path = ""): 
    
    sky_maps = []

    for i in index_list_primary:
        try:
            file = base_path + f"{index_list_primary[i]}" + secondary_path + f"{index_list_secondary[i]}"
            sky = hp.read_map(file)
            sky_maps.append(sky)
        except IndexError:
            file = base_path + f"{index_list_primary[i]}"
            sky = hp.read_map(file)
            sky_maps.append(sky)
    return sky_maps

def fits_info(file_path):   
    """
    Prints the information of a FITS file.
    
    Parameters:
    file_path (str): The path to the FITS file.
    """
    fits.info(file_path)


def main():
    # Example input map (Healpix format)
    nside = 64  # Healpix resolution parameter
    npix = hp.nside2npix(nside)
    input_map_path = '/home/nathand/Documents/AstroCode/SkyMaps/GCxCIB/maps/cib_857micron_signal_nside1024.fits'

    input_map = hp.read_map(input_map_path)
    # Define a threshold
    threshold = 50

    # Filter the map
    filtered_map = filter_map(input_map_path, threshold)

    # Plot the original and filtered maps
    plot_map(input_map, title='Original Map')
    plot_map(filtered_map, title='Filtered Map')

if __name__ == "__main__":
    pass
    #main()
    #fits_info('/home/nathand/Documents/AstroCode/SkyMaps/GCxCIB/maps/cib_857micron_signal_nside1024.fits')


ffff = fits_file_iterate(base_path='/home/nathand/Documents/AstroCode/SkyMaps/GCxCIB/maps/hsc_zbin', secondary_path='_nside1024.fits', index_list_primary=[0, 1, 2, 3], index_list_secondary=['', '', '', ''])

fig = plt.figure(figsize=(8, 6))
hp.mollview(ffff[3], title='HSC zbin 0', fig=fig)
plt.show()
