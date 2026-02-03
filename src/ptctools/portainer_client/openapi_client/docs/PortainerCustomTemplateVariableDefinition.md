# PortainerCustomTemplateVariableDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_value** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_custom_template_variable_definition import PortainerCustomTemplateVariableDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerCustomTemplateVariableDefinition from a JSON string
portainer_custom_template_variable_definition_instance = PortainerCustomTemplateVariableDefinition.from_json(json)
# print the JSON string representation of the object
print(PortainerCustomTemplateVariableDefinition.to_json())

# convert the object into a dict
portainer_custom_template_variable_definition_dict = portainer_custom_template_variable_definition_instance.to_dict()
# create an instance of PortainerCustomTemplateVariableDefinition from a dict
portainer_custom_template_variable_definition_from_dict = PortainerCustomTemplateVariableDefinition.from_dict(portainer_custom_template_variable_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


