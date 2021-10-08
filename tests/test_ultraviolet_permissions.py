# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 NYU.
#
# Ultraviolet Permssions is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Module tests."""

from flask import Flask

from ultraviolet_permissions import UltravioletPermssions


def test_version():
    """Test version import."""
    from ultraviolet_permissions import __version__
    assert __version__


def test_init():
    """Test extension initialization."""
    app = Flask('testapp')
    ext = UltravioletPermssions(app)
    assert 'ultraviolet-permissions' in app.extensions

    app = Flask('testapp')
    ext = UltravioletPermssions()
    assert 'ultraviolet-permissions' not in app.extensions
    ext.init_app(app)
    assert 'ultraviolet-permissions' in app.extensions


def test_view(base_client):
    """Test view."""
    res = base_client.get("/")
    assert res.status_code == 200
    assert 'Welcome to Ultraviolet Permssions' in str(res.data)
