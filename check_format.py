#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  check_format.py
#
#  Copyright 2014 Dominique Hunziker <dominique.hunziker@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os
import json


def main():
    for dir_name in ['demo', 'tests']:
        for file_name in os.listdir(dir_name):
            uri = os.path.join(dir_name, file_name)

            try:
                with open(uri, 'r') as f:
                    content = f.read()
            except IOError:
                continue

            try:
                json.loads(content)
            except Exception as e:
                print('{0}: FAILED [{1}]'.format(uri, e))
            else:
                print('{0}: OK'.format(uri))

    return 0


if __name__ == '__main__':
    main()
