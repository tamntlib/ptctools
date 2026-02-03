# PortainerUserResourceAccess


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_level** | [**PortainerResourceAccessLevel**](PortainerResourceAccessLevel.md) |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_user_resource_access import PortainerUserResourceAccess

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerUserResourceAccess from a JSON string
portainer_user_resource_access_instance = PortainerUserResourceAccess.from_json(json)
# print the JSON string representation of the object
print(PortainerUserResourceAccess.to_json())

# convert the object into a dict
portainer_user_resource_access_dict = portainer_user_resource_access_instance.to_dict()
# create an instance of PortainerUserResourceAccess from a dict
portainer_user_resource_access_from_dict = PortainerUserResourceAccess.from_dict(portainer_user_resource_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


