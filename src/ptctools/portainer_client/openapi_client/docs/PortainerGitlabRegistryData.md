# PortainerGitlabRegistryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_url** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 
**project_path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_gitlab_registry_data import PortainerGitlabRegistryData

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerGitlabRegistryData from a JSON string
portainer_gitlab_registry_data_instance = PortainerGitlabRegistryData.from_json(json)
# print the JSON string representation of the object
print(PortainerGitlabRegistryData.to_json())

# convert the object into a dict
portainer_gitlab_registry_data_dict = portainer_gitlab_registry_data_instance.to_dict()
# create an instance of PortainerGitlabRegistryData from a dict
portainer_gitlab_registry_data_from_dict = PortainerGitlabRegistryData.from_dict(portainer_gitlab_registry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


