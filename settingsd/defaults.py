# encoding: utf8
"""
Defaults for internal SETTINGSD_* keys
"""

from __future__ import absolute_import
from __future__ import print_function


SETTINGSD_NS_KEY = '__dict__'

SETTINGSD_BASES = ['settingsd.core:BaseSettings']

SETTINGSD_LOADERS = [
    'settingsd.loaders:from_name',
    'settingsd.loaders:from_mime',
    'settingsd.loaders:from_ext',
    ]

SETTINGSD_LOADER_FROM_EXT = dict()
SETTINGSD_LOADER_FROM_NAME = dict()
SETTINGSD_LOADER_FROM_MIME = {
    'text/x-python': 'settingsd.loaders:python',
    'application/json': 'settingsd.loaders:json',
    }