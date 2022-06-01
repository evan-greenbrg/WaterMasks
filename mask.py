import argparse
import glob
import os
import platform
from multiprocessing import set_start_method

from natsort import natsorted
import ee
from matplotlib import pyplot as plt
import numpy as np
from puller_fun import pull_image_watermasks
from puller_fun import pull_esa


ee.Initialize()


if __name__ == '__main__':
    if platform.system() == "Darwin":
            set_start_method('spawn')

    parser = argparse.ArgumentParser(description='Pull Water Masks')
    parser.add_argument('--poly', metavar='poly', type=str,
                        help='In path for the geopackage path')

    parser.add_argument('--mask_method', metavar='mask_method', type=str,
                        choices=['Jones', 'esa', 'Zou'],
                        help='Do you want to calculate mobility')

    parser.add_argument('--network_method', metavar='network_method', type=str,
                        choices=['grwl', 'merit', 'largest', 'all'],
                        default='grwl',
                        help='what method do you want to use to extract the network')

    parser.add_argument('--network_path', metavar='network_path', type=str,
                        default=None,
                        help='Path to network dataset')

    parser.add_argument('--period', metavar='images', type=str,
                        choices=[
                            'annual', 
                            'quarterly', 
                            'bankfull', 
                            'max', 
                            'min'
                        ],
                        help='Do you want to export images')

    parser.add_argument('--out', metavar='out', type=str,
                        help='output root directory')

    args = parser.parse_args()

    export_images = True 
#    if args.images == 'true':
#        export_images = True
    if (args.mask_method == 'Jones') or (args.mask_method == 'Zou'):
        paths = pull_image_watermasks(
            args.poly, 
            args.out, 
            export_images, 
            args.mask_method, 
            args.network_method, 
            args.network_path,
            args.period
        )
    elif args.method == 'esa':
        paths = pull_esa(args.poly, args.out)


poly="/home/greenberg/ExtraSpace/PhD/Projects/Mobility/053122/Indus/Indus.gpkg"
mask_method="Jones"     # Jones, Zou,
network_method="grwl"   # grwl, merit, largest
network_path="/Users/greenberg/Documents/PHD/Projects/Mobility/river_networks/channel_networks_full.shp"
period="annual"
out="/home/greenberg/ExtraSpace/PhD/Projects/Mobility/053122/Indus/"
