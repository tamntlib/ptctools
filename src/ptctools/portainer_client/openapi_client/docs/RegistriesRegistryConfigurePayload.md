# RegistriesRegistryConfigurePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **bool** | Is authentication against this registry enabled | 
**password** | **str** | Password used to authenticate against this registry. required when Authentication is true | [optional] 
**region** | **str** | ECR region | [optional] 
**tls** | **bool** | Use TLS | [optional] 
**tlscacert_file** | **List[int]** | The TLS CA certificate file | [optional] 
**tlscert_file** | **List[int]** | The TLS client certificate file | [optional] 
**tlskey_file** | **List[int]** | The TLS client key file | [optional] 
**tlsskip_verify** | **bool** | Skip the verification of the server TLS certificate | [optional] 
**username** | **str** | Username used to authenticate against this registry. Required when Authentication is true | [optional] 

## Example

```python
from openapi_client.models.registries_registry_configure_payload import RegistriesRegistryConfigurePayload

# TODO update the JSON string below
json = "{}"
# create an instance of RegistriesRegistryConfigurePayload from a JSON string
registries_registry_configure_payload_instance = RegistriesRegistryConfigurePayload.from_json(json)
# print the JSON string representation of the object
print(RegistriesRegistryConfigurePayload.to_json())

# convert the object into a dict
registries_registry_configure_payload_dict = registries_registry_configure_payload_instance.to_dict()
# create an instance of RegistriesRegistryConfigurePayload from a dict
registries_registry_configure_payload_from_dict = RegistriesRegistryConfigurePayload.from_dict(registries_registry_configure_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


