# RegistriesRegistryCreatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Is authentication against this registry enabled | 
**base_url** | **str** | BaseURL required for ProGet registry | [optional] 
**ecr** | [**PortainerEcrData**](PortainerEcrData.md) | ECR specific details, required when type &#x3D; 7 | [optional] 
**gitlab** | [**PortainerGitlabRegistryData**](PortainerGitlabRegistryData.md) | Gitlab specific details, required when type &#x3D; 4 | [optional] 
**name** | **str** | Name that will be used to identify this registry | 
**password** | **str** | Password used to authenticate against this registry. required when Authentication is true | [optional] 
**quay** | [**PortainerQuayRegistryData**](PortainerQuayRegistryData.md) | Quay specific details, required when type &#x3D; 1 | [optional] 
**type** | [**PortainerRegistryType**](PortainerRegistryType.md) | Registry Type. Valid values are:  1 (Quay.io),  2 (Azure container registry),  3 (custom registry),  4 (Gitlab registry),  5 (ProGet registry),  6 (DockerHub)  7 (ECR) | 
**url** | **str** | URL or IP address of the Docker registry | 
**username** | **str** | Username used to authenticate against this registry. Required when Authentication is true | [optional] 

## Example

```python
from openapi_client.models.registries_registry_create_payload import RegistriesRegistryCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of RegistriesRegistryCreatePayload from a JSON string
registries_registry_create_payload_instance = RegistriesRegistryCreatePayload.from_json(json)
# print the JSON string representation of the object
print(RegistriesRegistryCreatePayload.to_json())

# convert the object into a dict
registries_registry_create_payload_dict = registries_registry_create_payload_instance.to_dict()
# create an instance of RegistriesRegistryCreatePayload from a dict
registries_registry_create_payload_from_dict = RegistriesRegistryCreatePayload.from_dict(registries_registry_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


