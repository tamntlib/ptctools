# PortainerSSLSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_path** | **str** |  | [optional] 
**http_enabled** | **bool** |  | [optional] 
**key_path** | **str** |  | [optional] 
**self_signed** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_ssl_settings import PortainerSSLSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerSSLSettings from a JSON string
portainer_ssl_settings_instance = PortainerSSLSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerSSLSettings.to_json())

# convert the object into a dict
portainer_ssl_settings_dict = portainer_ssl_settings_instance.to_dict()
# create an instance of PortainerSSLSettings from a dict
portainer_ssl_settings_from_dict = PortainerSSLSettings.from_dict(portainer_ssl_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


