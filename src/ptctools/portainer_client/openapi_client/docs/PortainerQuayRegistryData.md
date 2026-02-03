# PortainerQuayRegistryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organisation_name** | **str** |  | [optional] 
**use_organisation** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_quay_registry_data import PortainerQuayRegistryData

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerQuayRegistryData from a JSON string
portainer_quay_registry_data_instance = PortainerQuayRegistryData.from_json(json)
# print the JSON string representation of the object
print(PortainerQuayRegistryData.to_json())

# convert the object into a dict
portainer_quay_registry_data_dict = portainer_quay_registry_data_instance.to_dict()
# create an instance of PortainerQuayRegistryData from a dict
portainer_quay_registry_data_from_dict = PortainerQuayRegistryData.from_dict(portainer_quay_registry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


