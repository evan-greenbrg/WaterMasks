#!/bin/bash
poly="/home/greenberg/ExtraSpace/PhD/Projects/Mobility/053122/Indus/Indus.gpkg"
mask_method="Jones"     # Jones, Zou,
network_method="grwl"   # grwl, merit, largest
network_path="/Users/greenberg/Documents/PHD/Projects/Mobility/river_networks/channel_networks_full.shp"
period="annual"
out="/home/greenberg/ExtraSpace/PhD/Projects/Mobility/053122/Indus/"

python mask.py --poly $poly --mask_method $mask_method --network_method $network_method --network_path $network_path --period $period --out $out
