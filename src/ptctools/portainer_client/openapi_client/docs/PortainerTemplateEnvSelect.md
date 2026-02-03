# PortainerTemplateEnvSelect


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **bool** | Will set this choice as the default choice | [optional] 
**text** | **str** | Some text that will displayed as a choice | [optional] 
**value** | **str** | A value that will be associated to the choice | [optional] 

## Example

```python
from openapi_client.models.portainer_template_env_select import PortainerTemplateEnvSelect

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTemplateEnvSelect from a JSON string
portainer_template_env_select_instance = PortainerTemplateEnvSelect.from_json(json)
# print the JSON string representation of the object
print(PortainerTemplateEnvSelect.to_json())

# convert the object into a dict
portainer_template_env_select_dict = portainer_template_env_select_instance.to_dict()
# create an instance of PortainerTemplateEnvSelect from a dict
portainer_template_env_select_from_dict = PortainerTemplateEnvSelect.from_dict(portainer_template_env_select_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


