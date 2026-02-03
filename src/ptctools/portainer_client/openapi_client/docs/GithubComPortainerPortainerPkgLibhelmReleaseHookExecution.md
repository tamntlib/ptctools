# GithubComPortainerPortainerPkgLibhelmReleaseHookExecution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completed_at** | **str** | CompletedAt indicates the date/time this hook was completed. | [optional] 
**phase** | **str** | Phase indicates whether the hook completed successfully | [optional] 
**started_at** | **str** | StartedAt indicates the date/time this hook was started | [optional] 

## Example

```python
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_hook_execution import GithubComPortainerPortainerPkgLibhelmReleaseHookExecution

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseHookExecution from a JSON string
github_com_portainer_portainer_pkg_libhelm_release_hook_execution_instance = GithubComPortainerPortainerPkgLibhelmReleaseHookExecution.from_json(json)
# print the JSON string representation of the object
print(GithubComPortainerPortainerPkgLibhelmReleaseHookExecution.to_json())

# convert the object into a dict
github_com_portainer_portainer_pkg_libhelm_release_hook_execution_dict = github_com_portainer_portainer_pkg_libhelm_release_hook_execution_instance.to_dict()
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseHookExecution from a dict
github_com_portainer_portainer_pkg_libhelm_release_hook_execution_from_dict = GithubComPortainerPortainerPkgLibhelmReleaseHookExecution.from_dict(github_com_portainer_portainer_pkg_libhelm_release_hook_execution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


