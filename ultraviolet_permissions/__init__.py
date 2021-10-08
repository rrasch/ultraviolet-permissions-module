# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 NYU.
#
# Ultraviolet Permssions is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that is used to define user permissions for NYUltraviolet ( NYU InvenioRDM instance)"""

from .ext import UltravioletPermssions
from .version import __version__

__all__ = ('__version__', 'UltravioletPermssions')
