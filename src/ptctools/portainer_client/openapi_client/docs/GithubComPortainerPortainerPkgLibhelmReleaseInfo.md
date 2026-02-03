# GithubComPortainerPortainerPkgLibhelmReleaseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **str** | Deleted tracks when this object was deleted. | [optional] 
**description** | **str** | Description is human-friendly \&quot;log entry\&quot; about this release. | [optional] 
**first_deployed** | **str** | FirstDeployed is when the release was first deployed. | [optional] 
**last_deployed** | **str** | LastDeployed is when the release was last deployed. | [optional] 
**notes** | **str** | Contains the rendered templates/NOTES.txt if available | [optional] 
**resources** | [**List[UnstructuredUnstructured]**](UnstructuredUnstructured.md) | Resources is the list of resources that are part of the release | [optional] 
**status** | **str** | Status is the current state of the release | [optional] 

## Example

```python
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_info import GithubComPortainerPortainerPkgLibhelmReleaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseInfo from a JSON string
github_com_portainer_portainer_pkg_libhelm_release_info_instance = GithubComPortainerPortainerPkgLibhelmReleaseInfo.from_json(json)
# print the JSON string representation of the object
print(GithubComPortainerPortainerPkgLibhelmReleaseInfo.to_json())

# convert the object into a dict
github_com_portainer_portainer_pkg_libhelm_release_info_dict = github_com_portainer_portainer_pkg_libhelm_release_info_instance.to_dict()
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseInfo from a dict
github_com_portainer_portainer_pkg_libhelm_release_info_from_dict = GithubComPortainerPortainerPkgLibhelmReleaseInfo.from_dict(github_com_portainer_portainer_pkg_libhelm_release_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


