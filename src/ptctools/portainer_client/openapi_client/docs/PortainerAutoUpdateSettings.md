# PortainerAutoUpdateSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force_pull_image** | **bool** | Pull latest image | [optional] 
**force_update** | **bool** | Force update ignores repo changes | [optional] 
**interval** | **str** | Auto update interval | [optional] 
**job_id** | **str** | Autoupdate job id | [optional] 
**webhook** | **str** | A UUID generated from client | [optional] 

## Example

```python
from openapi_client.models.portainer_auto_update_settings import PortainerAutoUpdateSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerAutoUpdateSettings from a JSON string
portainer_auto_update_settings_instance = PortainerAutoUpdateSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerAutoUpdateSettings.to_json())

# convert the object into a dict
portainer_auto_update_settings_dict = portainer_auto_update_settings_instance.to_dict()
# create an instance of PortainerAutoUpdateSettings from a dict
portainer_auto_update_settings_from_dict = PortainerAutoUpdateSettings.from_dict(portainer_auto_update_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


