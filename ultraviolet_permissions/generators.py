# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
# Copyright (C) 2021 CERN.
# Copyright (C) 2021 TU Wien.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.
#
#

"""UltraViolet Permissions Generators."""
from elasticsearch_dsl import Q
from invenio_access.permissions import authenticated_user
from invenio_access.models import  RoleNeed
from invenio_records_permissions.generators import Generator



class ProprietaryRecordPermissions(Generator):
    """ProprietaryRecordPermissions

    Allows users who were granted  a specific role to view additional records
    Main use case are records which should be only available to NYU community
    Another use case are records that only can be accessed by users who met special conditions.
    In second case record curators check the condition outside Ultraviolet and then assign the
    user to a special role.
    InvenioRDM data model does not allow to add role to the access section of the record ( See https://inveniordm.docs.cern.ch/reference/metadata/)
    As a proof of concept solution we use additional_descriptions field where value will be equal to "role" and type will be equal
    to "Technical Info". Hopefully InvenioRDM will modify their data model and we won't have to use this model in production
    We expect that even users who do not have access to the records will be able to see them in the search so query filter is set to any_user
    """

    def needs(self, record=None, **kwargs):
        """Enabling Needs."""
        if record is None:
            # 'record is None' means that this must be a 'create'
            # this should be allowed for any authenticated user
            return [authenticated_user]

        additional_descriptions = record.get("metadata").get("additional_descriptions", [])
        for index, description in enumerate(additional_descriptions, start = 0):
            if description.get("type") == "technical-info":
                role = description.get("description")
                for char in role:
                    if char in "</>p":
                        role.replace(char, '')
                return [RoleNeed(role.name)]
        return []

    def query_filter(self, **kwargs):
        """Match all in search."""
        return Q('can_all')
