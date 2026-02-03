# GittypesRepoConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**GittypesGitAuthentication**](GittypesGitAuthentication.md) | Git credentials | [optional] 
**config_file_path** | **str** | Path to where the config file is in this url/refName | [optional] 
**config_hash** | **str** | Repository hash | [optional] 
**reference_name** | **str** | The reference name | [optional] 
**tlsskip_verify** | **bool** | TLSSkipVerify skips SSL verification when cloning the Git repository | [optional] 
**url** | **str** | The repo url | [optional] 

## Example

```python
from openapi_client.models.gittypes_repo_config import GittypesRepoConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GittypesRepoConfig from a JSON string
gittypes_repo_config_instance = GittypesRepoConfig.from_json(json)
# print the JSON string representation of the object
print(GittypesRepoConfig.to_json())

# convert the object into a dict
gittypes_repo_config_dict = gittypes_repo_config_instance.to_dict()
# create an instance of GittypesRepoConfig from a dict
gittypes_repo_config_from_dict = GittypesRepoConfig.from_dict(gittypes_repo_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


