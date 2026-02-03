# PortainerEndpointGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorized_teams** | **List[int]** |  | [optional] 
**authorized_users** | **List[int]** | Deprecated in DBVersion &#x3D;&#x3D; 18 | [optional] 
**description** | **str** | Description associated to the environment(endpoint) group | [optional] 
**id** | **int** | Environment(Endpoint) group Identifier | [optional] 
**labels** | [**List[PortainerPair]**](PortainerPair.md) | Deprecated fields | [optional] 
**name** | **str** | Environment(Endpoint) group name | [optional] 
**tag_ids** | **List[int]** | List of tags associated to this environment(endpoint) group | [optional] 
**tags** | **List[str]** | Deprecated in DBVersion &#x3D;&#x3D; 22 | [optional] 
**team_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 
**user_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_endpoint_group import PortainerEndpointGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEndpointGroup from a JSON string
portainer_endpoint_group_instance = PortainerEndpointGroup.from_json(json)
# print the JSON string representation of the object
print(PortainerEndpointGroup.to_json())

# convert the object into a dict
portainer_endpoint_group_dict = portainer_endpoint_group_instance.to_dict()
# create an instance of PortainerEndpointGroup from a dict
portainer_endpoint_group_from_dict = PortainerEndpointGroup.from_dict(portainer_endpoint_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


