# PortainerRegistryAccessPolicies


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespaces** | **List[str]** |  | [optional] 
**team_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 
**user_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_registry_access_policies import PortainerRegistryAccessPolicies

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerRegistryAccessPolicies from a JSON string
portainer_registry_access_policies_instance = PortainerRegistryAccessPolicies.from_json(json)
# print the JSON string representation of the object
print(PortainerRegistryAccessPolicies.to_json())

# convert the object into a dict
portainer_registry_access_policies_dict = portainer_registry_access_policies_instance.to_dict()
# create an instance of PortainerRegistryAccessPolicies from a dict
portainer_registry_access_policies_from_dict = PortainerRegistryAccessPolicies.from_dict(portainer_registry_access_policies_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


