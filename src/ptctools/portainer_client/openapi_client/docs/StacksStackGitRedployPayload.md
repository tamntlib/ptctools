# StacksStackGitRedployPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env** | [**List[PortainerPair]**](PortainerPair.md) |  | [optional] 
**prune** | **bool** |  | [optional] 
**pull_image** | **bool** | Force a pulling to current image with the original tag though the image is already the latest | [optional] 
**repository_authentication** | **bool** |  | [optional] 
**repository_authorization_type** | [**GittypesGitCredentialAuthType**](GittypesGitCredentialAuthType.md) |  | [optional] 
**repository_password** | **str** |  | [optional] 
**repository_reference_name** | **str** |  | [optional] 
**repository_username** | **str** |  | [optional] 
**stack_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.stacks_stack_git_redploy_payload import StacksStackGitRedployPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksStackGitRedployPayload from a JSON string
stacks_stack_git_redploy_payload_instance = StacksStackGitRedployPayload.from_json(json)
# print the JSON string representation of the object
print(StacksStackGitRedployPayload.to_json())

# convert the object into a dict
stacks_stack_git_redploy_payload_dict = stacks_stack_git_redploy_payload_instance.to_dict()
# create an instance of StacksStackGitRedployPayload from a dict
stacks_stack_git_redploy_payload_from_dict = StacksStackGitRedployPayload.from_dict(stacks_stack_git_redploy_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


