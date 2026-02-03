# GitopsRepositoryFilePreviewPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_type** | [**GittypesGitCredentialAuthType**](GittypesGitCredentialAuthType.md) |  | [optional] 
**password** | **str** |  | [optional] 
**reference** | **str** |  | [optional] 
**repository** | **str** |  | 
**target_file** | **str** | Path to file whose content will be read | [optional] 
**tlsskip_verify** | **bool** | TLSSkipVerify skips SSL verification when cloning the Git repository | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gitops_repository_file_preview_payload import GitopsRepositoryFilePreviewPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GitopsRepositoryFilePreviewPayload from a JSON string
gitops_repository_file_preview_payload_instance = GitopsRepositoryFilePreviewPayload.from_json(json)
# print the JSON string representation of the object
print(GitopsRepositoryFilePreviewPayload.to_json())

# convert the object into a dict
gitops_repository_file_preview_payload_dict = gitops_repository_file_preview_payload_instance.to_dict()
# create an instance of GitopsRepositoryFilePreviewPayload from a dict
gitops_repository_file_preview_payload_from_dict = GitopsRepositoryFilePreviewPayload.from_dict(gitops_repository_file_preview_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


