# PortainerTemplateRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stackfile** | **str** | Path to the stack file inside the git repository | [optional] 
**url** | **str** | URL of a git repository used to deploy a stack template. Mandatory for a Swarm/Compose stack template | [optional] 

## Example

```python
from openapi_client.models.portainer_template_repository import PortainerTemplateRepository

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerTemplateRepository from a JSON string
portainer_template_repository_instance = PortainerTemplateRepository.from_json(json)
# print the JSON string representation of the object
print(PortainerTemplateRepository.to_json())

# convert the object into a dict
portainer_template_repository_dict = portainer_template_repository_instance.to_dict()
# create an instance of PortainerTemplateRepository from a dict
portainer_template_repository_from_dict = PortainerTemplateRepository.from_dict(portainer_template_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


