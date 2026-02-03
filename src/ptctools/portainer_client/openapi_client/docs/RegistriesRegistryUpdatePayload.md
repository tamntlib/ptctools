# RegistriesRegistryUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Is authentication against this registry enabled | 
**base_url** | **str** | BaseURL is used for quay registry | [optional] 
**ecr** | [**PortainerEcrData**](PortainerEcrData.md) | ECR data | [optional] 
**name** | **str** | Name that will be used to identify this registry | 
**password** | **str** | Password used to authenticate against this registry. required when Authentication is true | [optional] 
**quay** | [**PortainerQuayRegistryData**](PortainerQuayRegistryData.md) | Quay data | [optional] 
**registry_accesses** | [**Dict[str, PortainerRegistryAccessPolicies]**](PortainerRegistryAccessPolicies.md) | Registry access control | [optional] 
**url** | **str** | URL or IP address of the Docker registry | 
**username** | **str** | Username used to authenticate against this registry. Required when Authentication is true | [optional] 

## Example

```python
from openapi_client.models.registries_registry_update_payload import RegistriesRegistryUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of RegistriesRegistryUpdatePayload from a JSON string
registries_registry_update_payload_instance = RegistriesRegistryUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(RegistriesRegistryUpdatePayload.to_json())

# convert the object into a dict
registries_registry_update_payload_dict = registries_registry_update_payload_instance.to_dict()
# create an instance of RegistriesRegistryUpdatePayload from a dict
registries_registry_update_payload_from_dict = RegistriesRegistryUpdatePayload.from_dict(registries_registry_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


