#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 lizongzhe 
#
# Distributed under terms of the MIT license.

import os, sys
import yaml
with open('config', "r") as config_file:
    conf = yaml.load(config_file.read())

for key, value in conf['env'].items():
    os.environ[key] = value % {"env": os.environ, "hostname": hostname}

for key, info in [(k, i) for k, i in conf.items() if v.get('config', False)]:
    config = info['config'].format(env=os.environ)
    with open(info['path']) as conf_file:
        conf_file.write(config)

    os.popen(config.get('setup', ""))

