# PortainerRegistryManagementConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**access_token_expiry** | **int** |  | [optional] 
**authentication** | **bool** |  | [optional] 
**ecr** | [**PortainerEcrData**](PortainerEcrData.md) |  | [optional] 
**password** | **str** |  | [optional] 
**tls_config** | [**PortainerTLSConfiguration**](PortainerTLSConfiguration.md) |  | [optional] 
**type** | [**PortainerRegistryType**](PortainerRegistryType.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_registry_management_configuration import PortainerRegistryManagementConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerRegistryManagementConfiguration from a JSON string
portainer_registry_management_configuration_instance = PortainerRegistryManagementConfiguration.from_json(json)
# print the JSON string representation of the object
print(PortainerRegistryManagementConfiguration.to_json())

# convert the object into a dict
portainer_registry_management_configuration_dict = portainer_registry_management_configuration_instance.to_dict()
# create an instance of PortainerRegistryManagementConfiguration from a dict
portainer_registry_management_configuration_from_dict = PortainerRegistryManagementConfiguration.from_dict(portainer_registry_management_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


