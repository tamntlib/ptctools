# GittypesGitAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorization_type** | [**GittypesGitCredentialAuthType**](GittypesGitCredentialAuthType.md) |  | [optional] 
**git_credential_id** | **int** | Git credentials identifier when the value is not 0 When the value is 0, Username, Password, and Authtype are set without using saved credential This is introduced since 2.15.0 | [optional] 
**password** | **str** |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gittypes_git_authentication import GittypesGitAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of GittypesGitAuthentication from a JSON string
gittypes_git_authentication_instance = GittypesGitAuthentication.from_json(json)
# print the JSON string representation of the object
print(GittypesGitAuthentication.to_json())

# convert the object into a dict
gittypes_git_authentication_dict = gittypes_git_authentication_instance.to_dict()
# create an instance of GittypesGitAuthentication from a dict
gittypes_git_authentication_from_dict = GittypesGitAuthentication.from_dict(gittypes_git_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


