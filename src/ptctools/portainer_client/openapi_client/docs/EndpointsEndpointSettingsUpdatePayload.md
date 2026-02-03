# EndpointsEndpointSettingsUpdatePayload


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
**enable_gpu_management** | **bool** |  | [optional] 
**enable_host_management_features** | **bool** | Whether host management features are enabled | [optional] 
**gpus** | [**List[PortainerPair]**](PortainerPair.md) |  | [optional] 

## Example

```python
from openapi_client.models.endpoints_endpoint_settings_update_payload import EndpointsEndpointSettingsUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsEndpointSettingsUpdatePayload from a JSON string
endpoints_endpoint_settings_update_payload_instance = EndpointsEndpointSettingsUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(EndpointsEndpointSettingsUpdatePayload.to_json())

# convert the object into a dict
endpoints_endpoint_settings_update_payload_dict = endpoints_endpoint_settings_update_payload_instance.to_dict()
# create an instance of EndpointsEndpointSettingsUpdatePayload from a dict
endpoints_endpoint_settings_update_payload_from_dict = EndpointsEndpointSettingsUpdatePayload.from_dict(endpoints_endpoint_settings_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


