# EdgeStackPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_clone_git_repo_for_relative_path** | **bool** | AlwaysCloneGitRepoForRelativePath is a flag indicating if the agent must always clone the git repository for relative path. This field is only valid when SupportRelativePath is true. Used only for EE | [optional] 
**deployer_options_payload** | [**EdgeDeployerOptionsPayload**](EdgeDeployerOptionsPayload.md) |  | [optional] 
**dir_entries** | [**List[FilesystemDirEntry]**](FilesystemDirEntry.md) | Content of stack folder | [optional] 
**edge_update_id** | **int** | EdgeUpdateID is the ID of the edge update related to this stack. Used only for EE | [optional] 
**entry_file_name** | **str** | Name of the stack entry file | [optional] 
**env_vars** | [**List[PortainerPair]**](PortainerPair.md) | Used only for EE EnvVars is a list of environment variables to inject into the stack | [optional] 
**filesystem_path** | **str** | Mount point for relative path | [optional] 
**id** | **int** | ID of the stack | [optional] 
**name** | **str** | Name of the stack | [optional] 
**namespace** | **str** | Namespace to use for kubernetes stack. Keep empty to use the manifest namespace. | [optional] 
**pre_pull_image** | **bool** | PrePullImage is a flag indicating if the agent must pull the image before deploying the stack. Used only for EE | [optional] 
**re_pull_image** | **bool** | RePullImage is a flag indicating if the agent must pull the image if it is already present on the node. Used only for EE | [optional] 
**ready_re_pull_image** | **bool** | Used only for EE async edge agent ReadyRePullImage is a flag to indicate whether the auto update is trigger to re-pull image | [optional] 
**registry_credentials** | [**List[EdgeRegistryCredentials]**](EdgeRegistryCredentials.md) | RegistryCredentials holds the credentials for a Docker registry. Used only for EE | [optional] 
**retry_deploy** | **bool** | RetryDeploy is a flag indicating if the agent must retry to deploy the stack if it fails. Used only for EE | [optional] 
**retry_period** | **int** | RetryPeriod specifies the duration, in seconds, for which the agent should continue attempting to deploy the stack after a failure Used only for EE | [optional] 
**rollback_to** | **int** | RollbackTo specifies the stack file version to rollback to (only support to rollback to the last version currently) | [optional] 
**stack_file_content** | **str** | Content of the stack file (for compatibility to agent version less than 2.19.0) | [optional] 
**support_relative_path** | **bool** | Is relative path supported | [optional] 
**version** | **int** | Version of the stack file | [optional] 

## Example

```python
from openapi_client.models.edge_stack_payload import EdgeStackPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeStackPayload from a JSON string
edge_stack_payload_instance = EdgeStackPayload.from_json(json)
# print the JSON string representation of the object
print(EdgeStackPayload.to_json())

# convert the object into a dict
edge_stack_payload_dict = edge_stack_payload_instance.to_dict()
# create an instance of EdgeStackPayload from a dict
edge_stack_payload_from_dict = EdgeStackPayload.from_dict(edge_stack_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


