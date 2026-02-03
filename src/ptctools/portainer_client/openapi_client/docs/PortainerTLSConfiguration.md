# PortainerTLSConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tls** | **bool** | Use TLS | [optional] 
**tlsca_cert** | **str** | Path to the TLS CA certificate file | [optional] 
**tls_cert** | **str** | Path to the TLS client certificate file | [optional] 
**tls_key** | **str** | Path to the TLS client key file | [optional] 
**tls_skip_verify** | **bool** | Skip the verification of the server TLS certificate | [optional] 

## Example

```python
from openapi_client.models.portainer_tls_configuration import PortainerTLSConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTLSConfiguration from a JSON string
portainer_tls_configuration_instance = PortainerTLSConfiguration.from_json(json)
# print the JSON string representation of the object
print(PortainerTLSConfiguration.to_json())

# convert the object into a dict
portainer_tls_configuration_dict = portainer_tls_configuration_instance.to_dict()
# create an instance of PortainerTLSConfiguration from a dict
portainer_tls_configuration_from_dict = PortainerTLSConfiguration.from_dict(portainer_tls_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


