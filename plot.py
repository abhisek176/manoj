import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as  np
import matplotlib as mpl
import astropy.table as tab
import matplotlib.pyplot as plt
import os

def make_plot(input_file,fig_name,cmap):

# setting the figure
    font = {'family': 'serif', 'weight': 'normal', 'size': 14}
    plt.rc('font', **font)
    mpl.rcParams['axes.linewidth'] = 1.5
    fig = plt.figure()
    fig.set_size_inches(20,5)
    ax = fig.add_subplot(121)
    df=pd.read_csv(input_file)
    f=df.T
    f.to_csv('final.csv', header=False, index=False)
    read=pd.read_csv('final.csv')
    read.index=['x=0.00','x=0.005','x=0.01','x=0.02','x=0.03','x=0.04','x=0.05','x=0.06','x=0.08','x=0.10']
    #asc=sns.color_palette("viridis", as_cmap=True)
    ax = sb.heatmap(read, xticklabels=500,cmap =cmap, cbar_kws={'label': 'Intensity Map'})#, linewidths = 0.02),RdYlGn # for more check https://www.python-graph-gallery.com/92-control-color-in-seaborn-heatmaps
    plt.xlabel(r"2${\theta}$ (deg)")
    plt.ylabel(r"Intensity")
    ax.tick_params(direction='out', which='major', length=5, width=1.50)
    fig.savefig(fig_name, bbox_inches='tight',dpi=600)
    return

"""
example:
mk('input_file','plot_name.pdf','cmap')

from plot import make_plot as mk
mk('XRD_profiles_2D.csv','output.pdf','YlOrRd')
mk('XRD_profiles_2D.csv','output1.pdf','rainbow')
mk('XRD_profiles_2D.csv','output2.pdf','rocket')

Cmap options are:
rainbow,
MRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'crest', 'crest_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'flare', 'flare_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako', 'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r'
"""


