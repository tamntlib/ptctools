# PortainerInternalAuthSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_password_length** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_internal_auth_settings import PortainerInternalAuthSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerInternalAuthSettings from a JSON string
portainer_internal_auth_settings_instance = PortainerInternalAuthSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerInternalAuthSettings.to_json())

# convert the object into a dict
portainer_internal_auth_settings_dict = portainer_internal_auth_settings_instance.to_dict()
# create an instance of PortainerInternalAuthSettings from a dict
portainer_internal_auth_settings_from_dict = PortainerInternalAuthSettings.from_dict(portainer_internal_auth_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


