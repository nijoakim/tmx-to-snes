#!/usr/bin/env python3

# Copyright 2019 Joakim Nilsson
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

from distutils.core import setup

setup(
	name         = 'tmx-to-snes',
	version      = '0.1.0',
	author       = 'Joakim Nilsson',
	author_email = 'nijoakim@gmail.com',
	packages     = [],
	scripts      = ['tmx-to-snes'],
	license      = 'GPLv3',
	description  = 'Convert Tiled tilemaps to SNES tilemaps.',
)
