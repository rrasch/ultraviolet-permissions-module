# ultraviolet-permissions-module
Custom permission policies for NYU Ultraviolet Users

To install and enable custom permissions policy, use the following command:
```
pipenv run pip install git+https://github.com/nyudlts/ultraviolet-permissions-module.git@nyu-records-restrictions
```
And then, add the following to invenio.cfg:
```
from ultraviolet_permissions.policies import UltraVioletPermissionPolicy
RDM_PERMISSION_POLICY = UltraVioletPermissionPolicy
```
To enable the admin panel, add the following to your invenio.cfg:
```
ADMIN_PERMISSION_FACTORY = "ultraviolet_permissions.policies.ultraviolet_admin_permission_factory"
```
Important: Make sure that the following configuration is set in your invenio.cfg as well:
```
ADMIN_ROLE = "admin"
```