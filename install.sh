#!/bin/bash
## Author: Ben Knisley
## Created: 27 January, 2022
## Installs or reinstall the Nautilus Banner Extension locally, and showcases it.

## Remove old extension file, if exists
rm -f /home/ben/.local/share/nautilus-python/extensions/NautilusBannerExtension.py

## Copy current extension file to extensions directory
cp ./NautilusBannerExtension.py /home/ben/.local/share/nautilus-python/extensions/NautilusBannerExtension.py

## Kill running nautilus instances
nautilus -q

## Restart nautilus, and open example_dir to display banner
nautilus ./example_dir > /dev/null 2>&1 & 