# EdgestacksEdgeStackFromGitRepositoryPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_type** | [**PortainerEdgeStackDeploymentType**](PortainerEdgeStackDeploymentType.md) | Deployment type to deploy this stack Valid values are: 0 - &#39;compose&#39;, 1 - &#39;kubernetes&#39; compose is enabled only for docker environments kubernetes is enabled only for kubernetes environments | [optional] 
**edge_groups** | **List[int]** | List of identifiers of EdgeGroups | 
**file_path_in_repository** | **str** | Path to the Stack file inside the Git repository | [optional] [default to 'docker-compose.yml']
**name** | **str** | Name of the stack Max length: 255 Name must only contains lowercase characters, numbers, hyphens, or underscores Name must start with a lowercase character or number Example: stack-name or stack_123 or stackName | 
**registries** | **List[int]** | List of Registries to use for this stack | [optional] 
**repository_authentication** | **bool** | Use basic authentication to clone the Git repository | [optional] 
**repository_authorization_type** | [**GittypesGitCredentialAuthType**](GittypesGitCredentialAuthType.md) | RepositoryAuthorizationType is the authorization type to use | [optional] 
**repository_password** | **str** | Password used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**repository_reference_name** | **str** | Reference name of a Git repository hosting the Stack file | [optional] 
**repository_url** | **str** | URL of a Git repository hosting the Stack file | 
**repository_username** | **str** | Username used in basic authentication. Required when RepositoryAuthentication is true. | [optional] 
**tlsskip_verify** | **bool** | TLSSkipVerify skips SSL verification when cloning the Git repository | [optional] 
**use_manifest_namespaces** | **bool** | Uses the manifest&#39;s namespaces instead of the default one | [optional] 

## Example

```python
from openapi_client.models.edgestacks_edge_stack_from_git_repository_payload import EdgestacksEdgeStackFromGitRepositoryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgestacksEdgeStackFromGitRepositoryPayload from a JSON string
edgestacks_edge_stack_from_git_repository_payload_instance = EdgestacksEdgeStackFromGitRepositoryPayload.from_json(json)
# print the JSON string representation of the object
print(EdgestacksEdgeStackFromGitRepositoryPayload.to_json())

# convert the object into a dict
edgestacks_edge_stack_from_git_repository_payload_dict = edgestacks_edge_stack_from_git_repository_payload_instance.to_dict()
# create an instance of EdgestacksEdgeStackFromGitRepositoryPayload from a dict
edgestacks_edge_stack_from_git_repository_payload_from_dict = EdgestacksEdgeStackFromGitRepositoryPayload.from_dict(edgestacks_edge_stack_from_git_repository_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


