import pytest
from invenio_access.models import RoleNeed
from invenio_access.permissions import authenticated_user, superuser_access, any_user

from conftest import propriatery_record, user_roles_propriatery_record

import sys
sys.path.append('/Users/kunal/dev/ultraviolet-permissions-module/ultraviolet_permissions')
from generators import AdminSuperUser, Depositor, Viewer, RestrictedDataUser, PublicViewer, Curator


def test_admin_superuser():
    generator = AdminSuperUser()

    assert generator.needs() == [superuser_access]

@pytest.mark.parametrize("user_role", ["depositor"], indirect=True)
def test_depositor(user_roles_propriatery_record, propriatery_record):
    generator = Depositor()
    record = user_roles_propriatery_record
    other_record = propriatery_record

    assert generator.needs(record=record) == [RoleNeed("depositor")]
    assert generator.needs(record=other_record) == []


@pytest.mark.parametrize("user_role", ["viewer"], indirect=True)
def test_viewer(user_roles_propriatery_record, propriatery_record):
    generator = Viewer()
    record = user_roles_propriatery_record
    other_record = propriatery_record

    assert generator.needs(record=record) == [RoleNeed("viewer")]
    assert generator.needs(record=other_record) == []


@pytest.mark.parametrize("user_role", ["restricted_data_user"], indirect=True)
def test_restricted_data_user(user_roles_propriatery_record, propriatery_record):
    generator = RestrictedDataUser()
    record = user_roles_propriatery_record
    other_record = propriatery_record

    assert generator.needs(record=record) == [RoleNeed("restricted_data_user")]
    assert generator.needs(record=other_record) == []


@pytest.mark.parametrize("user_role", ["public_viewer"], indirect=True)
def test_public_viewer(user_roles_propriatery_record, propriatery_record):
    generator = PublicViewer()
    record = user_roles_propriatery_record
    other_record = propriatery_record

    assert generator.needs(record=record) == [RoleNeed("public_viewer")]
    assert generator.needs(record=other_record) == []


@pytest.mark.parametrize("user_role", ["curator"], indirect=True)
def test_curator(user_roles_propriatery_record, propriatery_record):
    generator = Curator()
    record = user_roles_propriatery_record
    other_record = propriatery_record

    assert generator.needs(record=record) == [RoleNeed("curator")]
    assert generator.needs(record=other_record) == []