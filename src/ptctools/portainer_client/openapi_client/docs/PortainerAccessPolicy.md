# PortainerAccessPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** | Role identifier. Reference the role that will be associated to this access policy | [optional] 

## Example

```python
from openapi_client.models.portainer_access_policy import PortainerAccessPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerAccessPolicy from a JSON string
portainer_access_policy_instance = PortainerAccessPolicy.from_json(json)
# print the JSON string representation of the object
print(PortainerAccessPolicy.to_json())

# convert the object into a dict
portainer_access_policy_dict = portainer_access_policy_instance.to_dict()
# create an instance of PortainerAccessPolicy from a dict
portainer_access_policy_from_dict = PortainerAccessPolicy.from_dict(portainer_access_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


