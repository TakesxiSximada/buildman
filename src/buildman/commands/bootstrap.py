#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import argparse
import subprocess
import requests

# compat
import six
if six.PY3:
    import configparser
else:
    import ConfigParser as configparser  # noqa


BOOTSTRAP_URL = 'https://raw.githubusercontent.com/buildout/buildout/master/bootstrap/bootstrap.py'
CACHE_BOOTSTRAP = 'buildmain.zc.buildout.bootstrap.py'


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--python', default='python')
    parser.add_argument('--bootstrap', default=BOOTSTRAP_URL)
    parser.add_argument('--cache', default=CACHE_BOOTSTRAP)
    args = parser.parse_args(argv)

    bootstrap_url = args.bootstrap
    bootstrap_file = args.cache
    buildout_cfg = 'buildout.cfg'

    if not os.path.exists(buildout_cfg):
        config = configparser.SafeConfigParser()
        config.add_section('buildout')
        config.set('buildout', 'parts', '')
        with open(buildout_cfg, 'w+t') as fp:
            config.write(fp)

    if not os.path.exists(bootstrap_file):
        res = requests.get(bootstrap_url)
        with open(bootstrap_file, 'wb') as fp:
            for chunk in res.iter_content(chunk_size=512 * 1024):
                fp.write(chunk)
    child = subprocess.Popen([args.python, bootstrap_file])
    res = child.wait()
    print(res)

if __name__ == '__main__':
    sys.exit(main())
