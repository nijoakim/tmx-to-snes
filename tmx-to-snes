#!/usr/bin/env python3

# Copyright 2019 Joakim Nilsson
#
# This file is part of tmx-to-snes.
#
# tmx-to-snes is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# tmx-to-snes is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with tmx-to-snes.  If not, see <http://www.gnu.org/licenses/>.

#========
# Import
#========

import argparse as ap
import os
import xml.etree.ElementTree as et

#=================
# Parse arguments
#=================

# Make parser
parser = ap.ArgumentParser(description='Converts tiled Tiled tilemaps to SNES tilemaps.')
parser.add_argument('filename', help='.tmx file to convert.')
parser.add_argument(
	'-s',
	'--size',
	type     = int,
	choices  = [8, 16],
	required = True,
	help = 'The side length of a tile in pixels.',
)

# Parse
args = parser.parse_args()

#==============
# Convert file
#==============

# Parse .tmx file as XML data
root = et.parse(args.filename).getroot()

# Use xml data to generate files
for layer_xml in root.iter('layer'):
	for data_xml in layer_xml.iter('data'):
		# Helper function
		def map_funct(x):
			x = int(x)-1        # tmx tiles are 1-indexed
			x *= args.size // 8 # Index step size = tile size / 8
			x = max(0, x)       # No tile results in tile 0

			# Each tile starts at a new 16-byte row
			if args.size == 16:
				hi_nibble = x & 0xf0
				lo_nibble = x & 0x0f
				x = (hi_nibble*2) | lo_nibble

			return x

		# Convert data
		data_bin = bytes(map(map_funct, data_xml.text.replace('\n', '').split(',')))

		# Write to output file
		filename_out = os.path.splitext(args.filename)[0] +'.'+ layer_xml.attrib['name'] +'.map'
		with open(filename_out, 'wb') as file:
			file.write(data_bin)
			
