# PortainerUserThemeSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | **str** | Color represents the color theme of the UI | [optional] 

## Example

```python
from openapi_client.models.portainer_user_theme_settings import PortainerUserThemeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerUserThemeSettings from a JSON string
portainer_user_theme_settings_instance = PortainerUserThemeSettings.from_json(json)
# print the JSON string representation of the object
print(PortainerUserThemeSettings.to_json())

# convert the object into a dict
portainer_user_theme_settings_dict = portainer_user_theme_settings_instance.to_dict()
# create an instance of PortainerUserThemeSettings from a dict
portainer_user_theme_settings_from_dict = PortainerUserThemeSettings.from_dict(portainer_user_theme_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


