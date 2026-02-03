# GithubComPortainerPortainerPkgLibhelmReleaseHook


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_policies** | **List[str]** | DeletePolicies are the policies that indicate when to delete the hook | [optional] 
**events** | **List[str]** | Events are the events that this hook fires on. | [optional] 
**kind** | **str** | Kind is the Kubernetes kind. | [optional] 
**last_run** | [**GithubComPortainerPortainerPkgLibhelmReleaseHookExecution**](GithubComPortainerPortainerPkgLibhelmReleaseHookExecution.md) | LastRun indicates the date/time this was last run. | [optional] 
**manifest** | **str** | Manifest is the manifest contents. | [optional] 
**name** | **str** |  | [optional] 
**path** | **str** | Path is the chart-relative path to the template. | [optional] 
**weight** | **int** | Weight indicates the sort order for execution among similar Hook type | [optional] 

## Example

```python
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_hook import GithubComPortainerPortainerPkgLibhelmReleaseHook

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseHook from a JSON string
github_com_portainer_portainer_pkg_libhelm_release_hook_instance = GithubComPortainerPortainerPkgLibhelmReleaseHook.from_json(json)
# print the JSON string representation of the object
print(GithubComPortainerPortainerPkgLibhelmReleaseHook.to_json())

# convert the object into a dict
github_com_portainer_portainer_pkg_libhelm_release_hook_dict = github_com_portainer_portainer_pkg_libhelm_release_hook_instance.to_dict()
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseHook from a dict
github_com_portainer_portainer_pkg_libhelm_release_hook_from_dict = GithubComPortainerPortainerPkgLibhelmReleaseHook.from_dict(github_com_portainer_portainer_pkg_libhelm_release_hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


