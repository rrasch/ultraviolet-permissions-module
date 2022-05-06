import pytest
from invenio_access.models import RoleNeed
from invenio_access.permissions import authenticated_user, superuser_access, any_user

from .conftest import propriatery_record, user_roles_propriatery_record
from ultraviolet_permissions.generators import AdminSuperUser, Depositor, Viewer, RestrictedDataUser, PublicViewer, Curator


def test_admin_superuser():
    generator = AdminSuperUser()

    assert generator.needs() == [superuser_access]


def test_depositor():
    generator = Depositor()
    role = "depositor"
    record = user_roles_propriatery_record(role)
    other_record = propriatery_record()

    assert generator.needs(record=record) == [RoleNeed(role)]
    assert generator.needs(record=other_record) == []


def test_viewer():
    generator = Viewer()
    role = "viewer"
    record = user_roles_propriatery_record(role)
    other_record = propriatery_record()

    assert generator.needs(record=record) == [RoleNeed(role)]
    assert generator.needs(record=other_record) == []


def test_restricted_data_user():
    generator = RestrictedDataUser()
    role = "restricted_data_user"
    record = user_roles_propriatery_record(role)
    other_record = propriatery_record()

    assert generator.needs(record=record) == [RoleNeed(role)]
    assert generator.needs(record=other_record) == []


def test_public_viewer():
    generator = PublicViewer()
    role = "public_viewer"
    record = user_roles_propriatery_record(role)
    other_record = propriatery_record()

    assert generator.needs(record=record) == [RoleNeed(role)]
    assert generator.needs(record=other_record) == []


def test_curator():
    generator = Curator()
    role = "curator"
    record = user_roles_propriatery_record(role)
    other_record = propriatery_record()

    assert generator.needs(record=record) == [RoleNeed(role)]
    assert generator.needs(record=other_record) == []