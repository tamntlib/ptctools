# StacksStackGitUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_update** | [**PortainerAutoUpdateSettings**](PortainerAutoUpdateSettings.md) |  | [optional] 
**env** | [**List[PortainerPair]**](PortainerPair.md) |  | [optional] 
**prune** | **bool** |  | [optional] 
**repository_authentication** | **bool** |  | [optional] 
**repository_authorization_type** | [**GittypesGitCredentialAuthType**](GittypesGitCredentialAuthType.md) |  | [optional] 
**repository_password** | **str** |  | [optional] 
**repository_reference_name** | **str** |  | [optional] 
**repository_username** | **str** |  | [optional] 
**tlsskip_verify** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.stacks_stack_git_update_payload import StacksStackGitUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksStackGitUpdatePayload from a JSON string
stacks_stack_git_update_payload_instance = StacksStackGitUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(StacksStackGitUpdatePayload.to_json())

# convert the object into a dict
stacks_stack_git_update_payload_dict = stacks_stack_git_update_payload_instance.to_dict()
# create an instance of StacksStackGitUpdatePayload from a dict
stacks_stack_git_update_payload_from_dict = StacksStackGitUpdatePayload.from_dict(stacks_stack_git_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


