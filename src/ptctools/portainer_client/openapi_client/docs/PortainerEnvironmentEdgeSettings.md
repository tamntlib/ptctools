# PortainerEnvironmentEdgeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_interval** | **int** | The command list interval for edge agent - used in edge async mode [seconds] | [optional] 
**ping_interval** | **int** | The ping interval for edge agent - used in edge async mode [seconds] | [optional] 
**snapshot_interval** | **int** | The snapshot interval for edge agent - used in edge async mode [seconds] | [optional] 
**async_mode** | **bool** | Whether the device has been started in edge async mode | [optional] 

## Example

```python
from openapi_client.models.portainer_environment_edge_settings import PortainerEnvironmentEdgeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEnvironmentEdgeSettings from a JSON string
portainer_environment_edge_settings_instance = PortainerEnvironmentEdgeSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerEnvironmentEdgeSettings.to_json())

# convert the object into a dict
portainer_environment_edge_settings_dict = portainer_environment_edge_settings_instance.to_dict()
# create an instance of PortainerEnvironmentEdgeSettings from a dict
portainer_environment_edge_settings_from_dict = PortainerEnvironmentEdgeSettings.from_dict(portainer_environment_edge_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


