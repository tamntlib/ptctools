# PortainerRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizations** | **Dict[str, bool]** | Authorizations associated to a role | [optional] 
**description** | **str** | Role description | [optional] 
**id** | **int** | Role Identifier | [optional] 
**name** | **str** | Role name | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_role import PortainerRole

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerRole from a JSON string
portainer_role_instance = PortainerRole.from_json(json)
# print the JSON string representation of the object
print(PortainerRole.to_json())

# convert the object into a dict
portainer_role_dict = portainer_role_instance.to_dict()
# create an instance of PortainerRole from a dict
portainer_role_from_dict = PortainerRole.from_dict(portainer_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


