# EdgeRegistryCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** |  | [optional] 
**server_url** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.edge_registry_credentials import EdgeRegistryCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeRegistryCredentials from a JSON string
edge_registry_credentials_instance = EdgeRegistryCredentials.from_json(json)
# print the JSON string representation of the object
print(EdgeRegistryCredentials.to_json())

# convert the object into a dict
edge_registry_credentials_dict = edge_registry_credentials_instance.to_dict()
# create an instance of EdgeRegistryCredentials from a dict
edge_registry_credentials_from_dict = EdgeRegistryCredentials.from_dict(edge_registry_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


