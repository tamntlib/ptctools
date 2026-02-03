# PortainerUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User Identifier | [optional] 
**role** | [**PortainerUserRole**](PortainerUserRole.md) | User role (1 for administrator account and 2 for regular account) | [optional] 
**theme_settings** | [**PortainerUserThemeSettings**](PortainerUserThemeSettings.md) |  | [optional] 
**token_issue_at** | **int** |  | [optional] 
**use_cache** | **bool** |  | [optional] 
**user_theme** | **str** | Deprecated | [optional] 
**username** | **str** |  | [optional] 
**endpoint_authorizations** | **Dict[str, Dict[str, bool]]** | Deprecated in DBVersion &#x3D;&#x3D; 25 | [optional] 
**portainer_authorizations** | **Dict[str, bool]** | Deprecated in DBVersion &#x3D;&#x3D; 25 | [optional] 

## Example

```python
from openapi_client.models.portainer_user import PortainerUser

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerUser from a JSON string
portainer_user_instance = PortainerUser.from_json(json)
# print the JSON string representation of the object
print(PortainerUser.to_json())

# convert the object into a dict
portainer_user_dict = portainer_user_instance.to_dict()
# create an instance of PortainerUser from a dict
portainer_user_from_dict = PortainerUser.from_dict(portainer_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


