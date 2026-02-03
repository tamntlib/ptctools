# PortainerCustomTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by_user_id** | **int** | User identifier who created this template | [optional] 
**description** | **str** | Description of the template | [optional] 
**entry_point** | **str** | Path to the Stack file | [optional] 
**git_config** | [**GittypesRepoConfig**](GittypesRepoConfig.md) |  | [optional] 
**id** | **int** | CustomTemplate Identifier | [optional] 
**logo** | **str** | URL of the template&#39;s logo | [optional] 
**note** | **str** | A note that will be displayed in the UI. Supports HTML content | [optional] 
**platform** | [**PortainerCustomTemplatePlatform**](PortainerCustomTemplatePlatform.md) | Platform associated to the template. Valid values are: 1 - &#39;linux&#39;, 2 - &#39;windows&#39; | [optional] 
**project_path** | **str** | Path on disk to the repository hosting the Stack file | [optional] 
**resource_control** | [**PortainerResourceControl**](PortainerResourceControl.md) |  | [optional] 
**title** | **str** | Title of the template | [optional] 
**type** | [**PortainerStackType**](PortainerStackType.md) | Type of created stack: * 1 - swarm * 2 - compose * 3 - kubernetes | [optional] 
**edge_template** | **bool** | EdgeTemplate indicates if this template purpose for Edge Stack | [optional] 
**is_compose_format** | **bool** | IsComposeFormat indicates if the Kubernetes template is created from a Docker Compose file | [optional] 
**variables** | [**List[PortainerCustomTemplateVariableDefinition]**](PortainerCustomTemplateVariableDefinition.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_custom_template import PortainerCustomTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerCustomTemplate from a JSON string
portainer_custom_template_instance = PortainerCustomTemplate.from_json(json)
# print the JSON string representation of the object
print(PortainerCustomTemplate.to_json())

# convert the object into a dict
portainer_custom_template_dict = portainer_custom_template_instance.to_dict()
# create an instance of PortainerCustomTemplate from a dict
portainer_custom_template_from_dict = PortainerCustomTemplate.from_dict(portainer_custom_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


