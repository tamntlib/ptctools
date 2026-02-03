# StacksKubernetesGitDeploymentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_files** | **List[str]** |  | [optional] 
**auto_update** | [**PortainerAutoUpdateSettings**](PortainerAutoUpdateSettings.md) |  | [optional] 
**compose_format** | **bool** |  | [optional] 
**manifest_file** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**repository_authentication** | **bool** |  | [optional] 
**repository_password** | **str** |  | [optional] 
**repository_reference_name** | **str** |  | [optional] 
**repository_url** | **str** |  | [optional] 
**repository_username** | **str** |  | [optional] 
**stack_name** | **str** |  | [optional] 
**tlsskip_verify** | **bool** | TLSSkipVerify skips SSL verification when cloning the Git repository | [optional] 

## Example

```python
from openapi_client.models.stacks_kubernetes_git_deployment_payload import StacksKubernetesGitDeploymentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksKubernetesGitDeploymentPayload from a JSON string
stacks_kubernetes_git_deployment_payload_instance = StacksKubernetesGitDeploymentPayload.from_json(json)
# print the JSON string representation of the object
print(StacksKubernetesGitDeploymentPayload.to_json())

# convert the object into a dict
stacks_kubernetes_git_deployment_payload_dict = stacks_kubernetes_git_deployment_payload_instance.to_dict()
# create an instance of StacksKubernetesGitDeploymentPayload from a dict
stacks_kubernetes_git_deployment_payload_from_dict = StacksKubernetesGitDeploymentPayload.from_dict(stacks_kubernetes_git_deployment_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


