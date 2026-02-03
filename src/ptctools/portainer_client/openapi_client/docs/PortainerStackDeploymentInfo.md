# PortainerStackDeploymentInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_hash** | **str** | ConfigHash is the commit hash of the git repository used for deploying the stack | [optional] 
**file_version** | **int** | FileVersion is the version of the stack file, used to detect changes | [optional] 
**version** | **int** | Version is the version of the stack and also is the deployed version in edge agent | [optional] 

## Example

```python
from openapi_client.models.portainer_stack_deployment_info import PortainerStackDeploymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerStackDeploymentInfo from a JSON string
portainer_stack_deployment_info_instance = PortainerStackDeploymentInfo.from_json(json)
# print the JSON string representation of the object
print(PortainerStackDeploymentInfo.to_json())

# convert the object into a dict
portainer_stack_deployment_info_dict = portainer_stack_deployment_info_instance.to_dict()
# create an instance of PortainerStackDeploymentInfo from a dict
portainer_stack_deployment_info_from_dict = PortainerStackDeploymentInfo.from_dict(portainer_stack_deployment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


