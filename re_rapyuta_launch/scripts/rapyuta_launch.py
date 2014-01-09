#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#     rapyuta_launch.py
#
#     This file is part of the RoboEarth Cloud Engine framework.
#
#     This file was originally created for RoboEearth
#     http://www.roboearth.org/
#
#     The research leading to these results has received funding from
#     the European Union Seventh Framework Programme FP7/2007-2013 under
#     grant agreement no248942 RoboEarth.
#
#     Copyright 2012 RoboEarth
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#
#     \author/s: Dominique Hunziker
#
#     Note: Copy & Paste from "rce-client/scripts/rce-ros"!
#

# Python specific imports
import json

# ROS specific imports
import rospy

# Custom imports
from rce.client.ros import main


def _get_argparse():
    from argparse import ArgumentParser, FileType

    parser = ArgumentParser(prog='ROS Client',
                            description='Client for the RoboEarth Cloud Engine '
                                        'providing an Interface for ROS based '
                                        'communications.')

    parser.add_argument('config', help='rce-ros client configuration file.',
                        type=FileType('r'))

    return parser


if __name__ == '__main__':
    from twisted.internet import reactor

    args = _get_argparse().parse_args(rospy.myargv()[1:])
    fh = args.config

    try:
        config = json.load(fh)
    except ValueError:
        print('Configuration file is not in proper JSON format.')
        exit(1)
    finally:
        fh.close()

    main(config, reactor)
