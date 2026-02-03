# PortainerTemplate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**administrator_only** | **bool** | Whether the template should be available to administrators only | [optional] 
**categories** | **List[str]** | A list of categories associated to the template | [optional] 
**command** | **str** | The command that will be executed in a container template | [optional] 
**description** | **str** | Description of the template | [optional] 
**env** | [**List[PortainerTemplateEnv]**](PortainerTemplateEnv.md) | A list of environment(endpoint) variables used during the template deployment | [optional] 
**hostname** | **str** | Container hostname | [optional] 
**id** | **int** | Mandatory container/stack fields Template Identifier | [optional] 
**image** | **str** | Mandatory container fields Image associated to a container template. Mandatory for a container template | [optional] 
**interactive** | **bool** | Whether the container should be started in interactive mode (-i -t equivalent on the CLI) | [optional] 
**labels** | [**List[PortainerPair]**](PortainerPair.md) | Container labels | [optional] 
**logo** | **str** | URL of the template&#39;s logo | [optional] 
**name** | **str** | Optional stack/container fields Default name for the stack/container to be used on deployment | [optional] 
**network** | **str** | Name of a network that will be used on container deployment if it exists inside the environment(endpoint) | [optional] 
**note** | **str** | A note that will be displayed in the UI. Supports HTML content | [optional] 
**platform** | **str** | Platform associated to the template. Valid values are: &#39;linux&#39;, &#39;windows&#39; or leave empty for multi-platform | [optional] 
**ports** | **List[str]** | A list of ports exposed by the container | [optional] 
**privileged** | **bool** | Whether the container should be started in privileged mode | [optional] 
**registry** | **str** | Optional container fields The URL of a registry associated to the image for a container template | [optional] 
**repository** | [**PortainerTemplateRepository**](PortainerTemplateRepository.md) | Mandatory stack fields | [optional] 
**restart_policy** | **str** | Container restart policy | [optional] 
**stack_file** | **str** | Mandatory Edge stack fields Stack file used for this template | [optional] 
**title** | **str** | Title of the template | [optional] 
**type** | [**PortainerTemplateType**](PortainerTemplateType.md) | Template type. Valid values are: 1 (container), 2 (Swarm stack), 3 (Compose stack), 4 (Compose edge stack) | [optional] 
**volumes** | [**List[PortainerTemplateVolume]**](PortainerTemplateVolume.md) | A list of volumes used during the container template deployment | [optional] 

## Example

```python
from openapi_client.models.portainer_template import PortainerTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTemplate from a JSON string
portainer_template_instance = PortainerTemplate.from_json(json)
# print the JSON string representation of the object
print(PortainerTemplate.to_json())

# convert the object into a dict
portainer_template_dict = portainer_template_instance.to_dict()
# create an instance of PortainerTemplate from a dict
portainer_template_from_dict = PortainerTemplate.from_dict(portainer_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


