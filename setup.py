#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2015 lizongzhe 
#
# Distributed under terms of the MIT license.

import sys
import yaml
import os
conf_file = sys.argv[1]
hostname = os.popen('hostname').read()
conf = yaml.load(open(conf_file).read().format(env=os.environ, hostname=hostname))
env = conf['env']
export_env = "\n".join(["export {}={};".format(k, v) for k, v in env.items()])
del conf['env']
for key, info in conf.items():
    path = info['path']
    template = info['template']
    with open(path, 'w+') as out:
        out.write(template.format(env=env, export_env=export_env))
    print '{} write success'.format([atj)


