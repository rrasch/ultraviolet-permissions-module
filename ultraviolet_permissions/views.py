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
# from .policies import UVCommunitiesPermissionPolicy
# from flask_menu import current_menu
# from flask_babelex import lazy_gettext as _
# import time
# import threading

blueprint = Blueprint(
    'ultraviolet_permissions',
    __name__,
    static_folder='static',
)


# @blueprint.record_once
# def override_communities_permissions(state):
#     """Override permission policy class for communities."""
#     # Does not impact community creation in any way but allows for customizing other communities permission policies
#     app = state.app
#     communities = app.extensions.get("invenio-communities", None)
#     assert communities is not None
#
#     # override the permission policy class for all communities services
#     svc = communities.service
#     svc.config.permission_policy_cls = UVCommunitiesPermissionPolicy
#     svc.files.config.permission_policy_cls = UVCommunitiesPermissionPolicy
#     svc.members.config.permission_policy_cls = UVCommunitiesPermissionPolicy
#
#     app.logger.debug("Updated Communities Permissions to Ultraviolet-Specific policies")

# @blueprint.record_once
# def override_menu(state):
#     current_menu = state.app.extensions.get("menu", None)
#     def run_job():
#         while not state.app.got_first_request:
#             time.sleep(1)
#         current_menu.submenu("actions.deposit").register(
#             "invenio_app_rdm_users.uploads", _("My Deposits"), order=1
#         )
#         state.app.logger.debug("Updated Dashboard to 'My Deposits'")
#
#     thread = threading.Thread(target=run_job, daemon=True)
#     thread.start()