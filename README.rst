..
    Copyright (C) 2021 NYU.

    Ultraviolet Permssions is free software; you can redistribute it and/or
    modify it under the terms of the MIT License; see LICENSE file for more
    details.

========================
 Ultraviolet Permissions
========================

.. image:: https://github.com/nyudlts/ultraviolet-permissions-module/workflows/CI/badge.svg
        :target: https://github.com/nyudlts/ultraviolet-permissions-module/actions?query=workflow%3ACI

.. image:: https://img.shields.io/github/tag/nyudlts/ultraviolet-permissions-module.svg
        :target: https://github.com/nyudlts/ultraviolet-permissions-module/releases

.. image:: https://img.shields.io/pypi/dm/ultraviolet-permissions.svg
        :target: https://pypi.python.org/pypi/ultraviolet-permissions

.. image:: https://img.shields.io/github/license/nyudlts/ultraviolet-permissions-module.svg
        :target: https://github.com/nyudlts/ultraviolet-permissions-module/blob/master/LICENSE

Invenio module that is used to define user permissions for NYUltraviolet ( NYU InvenioRDM instance)

To install and enable custom permissions policy, use the following command::

pipenv run pip install git+https://github.com/nyudlts/ultraviolet-permissions-module.git@nyu-records-restrictions

And then, add the following to invenio.cfg::

from ultraviolet_permissions.policies import UltraVioletPermissionPolicy
RDM_PERMISSION_POLICY = UltraVioletPermissionPolicy

