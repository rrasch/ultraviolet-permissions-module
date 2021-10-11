# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 NYU.
#
# Ultraviolet Permssions is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio module that is used to define user permissions for NYUltraviolet ( NYU InvenioRDM instance)"""

# TODO: This is an example file. Remove it if you do not need it, including
# the templates and static folders as well as the test case.

from flask import Blueprint

blueprint = Blueprint(
    'ultraviolet_permissions',
    __name__,
    static_folder='static',
)
