# StacksComposeStackFromGitRepositoryPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_files** | **List[str]** | Applicable when deploying with multiple stack files | [optional] 
**auto_update** | [**PortainerAutoUpdateSettings**](PortainerAutoUpdateSettings.md) | Optional GitOps update configuration | [optional] 
**compose_file** | **str** | Path to the Stack file inside the Git repository | [optional] [default to 'docker-compose.yml']
**env** | [**List[PortainerPair]**](PortainerPair.md) | A list of environment variables used during stack deployment | [optional] 
**from_app_template** | **bool** | Whether the stack is from a app template | [optional] 
**name** | **str** | Name of the stack | 
**repository_authentication** | **bool** | Use basic authentication to clone the Git repository | [optional] 
**repository_password** | **str** | Password used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**repository_reference_name** | **str** | Reference name of a Git repository hosting the Stack file | [optional] 
**repository_url** | **str** | URL of a Git repository hosting the Stack file | 
**repository_username** | **str** | Username used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**tlsskip_verify** | **bool** | TLSSkipVerify skips SSL verification when cloning the Git repository | [optional] 

## Example

```python
from openapi_client.models.stacks_compose_stack_from_git_repository_payload import StacksComposeStackFromGitRepositoryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of StacksComposeStackFromGitRepositoryPayload from a JSON string
stacks_compose_stack_from_git_repository_payload_instance = StacksComposeStackFromGitRepositoryPayload.from_json(json)
# print the JSON string representation of the object
print(StacksComposeStackFromGitRepositoryPayload.to_json())

# convert the object into a dict
stacks_compose_stack_from_git_repository_payload_dict = stacks_compose_stack_from_git_repository_payload_instance.to_dict()
# create an instance of StacksComposeStackFromGitRepositoryPayload from a dict
stacks_compose_stack_from_git_repository_payload_from_dict = StacksComposeStackFromGitRepositoryPayload.from_dict(stacks_compose_stack_from_git_repository_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


