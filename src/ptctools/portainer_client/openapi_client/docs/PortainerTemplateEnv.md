# PortainerTemplateEnv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** | Default value that will be set for the variable | [optional] 
**description** | **str** | Content of the tooltip that will be generated in the UI | [optional] 
**label** | **str** | Text for the label that will be generated in the UI | [optional] 
**name** | **str** | name of the environment(endpoint) variable | [optional] 
**preset** | **bool** | If set to true, will not generate any input for this variable in the UI | [optional] 
**select** | [**List[PortainerTemplateEnvSelect]**](PortainerTemplateEnvSelect.md) | A list of name/value that will be used to generate a dropdown in the UI | [optional] 

## Example

```python
from openapi_client.models.portainer_template_env import PortainerTemplateEnv

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTemplateEnv from a JSON string
portainer_template_env_instance = PortainerTemplateEnv.from_json(json)
# print the JSON string representation of the object
print(PortainerTemplateEnv.to_json())

# convert the object into a dict
portainer_template_env_dict = portainer_template_env_instance.to_dict()
# create an instance of PortainerTemplateEnv from a dict
portainer_template_env_from_dict = PortainerTemplateEnv.from_dict(portainer_template_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


