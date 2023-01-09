# ultraviolet-permissions-module
Custom permission policies for NYU Ultraviolet Users

To install and enable custom permissions policy, use the following command::
```
pipenv run pip install git+https://github.com/nyudlts/ultraviolet-permissions-module.git@nyu-records-restrictions
```
And then, add the following to invenio.cfg::
```
from ultraviolet_permissions.policies import UltraVioletPermissionPolicy
RDM_PERMISSION_POLICY = UltraVioletPermissionPolicy
```