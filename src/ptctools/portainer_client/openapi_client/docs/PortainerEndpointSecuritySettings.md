# PortainerEndpointSecuritySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_bind_mounts_for_regular_users** | **bool** | Whether non-administrator should be able to use bind mounts when creating containers | [optional] 
**allow_container_capabilities_for_regular_users** | **bool** | Whether non-administrator should be able to use container capabilities | [optional] 
**allow_device_mapping_for_regular_users** | **bool** | Whether non-administrator should be able to use device mapping | [optional] 
**allow_host_namespace_for_regular_users** | **bool** | Whether non-administrator should be able to use the host pid | [optional] 
**allow_privileged_mode_for_regular_users** | **bool** | Whether non-administrator should be able to use privileged mode when creating containers | [optional] 
**allow_stack_management_for_regular_users** | **bool** | Whether non-administrator should be able to manage stacks | [optional] 
**allow_sysctl_setting_for_regular_users** | **bool** | Whether non-administrator should be able to use sysctl settings | [optional] 
**allow_volume_browser_for_regular_users** | **bool** | Whether non-administrator should be able to browse volumes | [optional] 
**enable_host_management_features** | **bool** | Whether host management features are enabled | [optional] 

## Example

```python
from openapi_client.models.portainer_endpoint_security_settings import PortainerEndpointSecuritySettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEndpointSecuritySettings from a JSON string
portainer_endpoint_security_settings_instance = PortainerEndpointSecuritySettings.from_json(json)
# print the JSON string representation of the object
print(PortainerEndpointSecuritySettings.to_json())

# convert the object into a dict
portainer_endpoint_security_settings_dict = portainer_endpoint_security_settings_instance.to_dict()
# create an instance of PortainerEndpointSecuritySettings from a dict
portainer_endpoint_security_settings_from_dict = PortainerEndpointSecuritySettings.from_dict(portainer_endpoint_security_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


