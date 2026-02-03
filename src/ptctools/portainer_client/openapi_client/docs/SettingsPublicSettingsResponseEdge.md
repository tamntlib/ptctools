# SettingsPublicSettingsResponseEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command_interval** | **int** | The command list interval for edge agent - used in edge async mode [seconds] | [optional] 
**ping_interval** | **int** | The ping interval for edge agent - used in edge async mode [seconds] | [optional] 
**snapshot_interval** | **int** | The snapshot interval for edge agent - used in edge async mode [seconds] | [optional] 
**checkin_interval** | **int** | The check in interval for edge agent (in seconds) - used in non async mode [seconds] | [optional] 

## Example

```python
from openapi_client.models.settings_public_settings_response_edge import SettingsPublicSettingsResponseEdge

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsPublicSettingsResponseEdge from a JSON string
settings_public_settings_response_edge_instance = SettingsPublicSettingsResponseEdge.from_json(json)
# print the JSON string representation of the object
print(SettingsPublicSettingsResponseEdge.to_json())

# convert the object into a dict
settings_public_settings_response_edge_dict = settings_public_settings_response_edge_instance.to_dict()
# create an instance of SettingsPublicSettingsResponseEdge from a dict
settings_public_settings_response_edge_from_dict = SettingsPublicSettingsResponseEdge.from_dict(settings_public_settings_response_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


