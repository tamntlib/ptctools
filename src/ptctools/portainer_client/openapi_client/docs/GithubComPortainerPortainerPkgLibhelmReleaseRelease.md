# GithubComPortainerPortainerPkgLibhelmReleaseRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_version** | **str** | AppVersion is the app version of the release. | [optional] 
**chart** | [**ReleaseChart**](ReleaseChart.md) | Chart is the chart that was released. | [optional] 
**chart_reference** | [**ReleaseChartReference**](ReleaseChartReference.md) | ChartReference are the labels that are used to identify the chart source. | [optional] 
**config** | **Dict[str, object]** | Config is the set of extra Values added to the chart. These values override the default values inside of the chart. | [optional] 
**hooks** | [**List[GithubComPortainerPortainerPkgLibhelmReleaseHook]**](GithubComPortainerPortainerPkgLibhelmReleaseHook.md) | Hooks are all of the hooks declared for this release. | [optional] 
**info** | [**GithubComPortainerPortainerPkgLibhelmReleaseInfo**](GithubComPortainerPortainerPkgLibhelmReleaseInfo.md) | Info provides information about a release | [optional] 
**manifest** | **str** | Manifest is the string representation of the rendered template. | [optional] 
**name** | **str** | Name is the name of the release | [optional] 
**namespace** | **str** | Namespace is the kubernetes namespace of the release. | [optional] 
**values** | [**ReleaseValues**](ReleaseValues.md) | Values are the values used to deploy the chart. | [optional] 
**version** | **int** | Version is an int which represents the revision of the release. | [optional] 

## Example

```python
from openapi_client.models.github_com_portainer_portainer_pkg_libhelm_release_release import GithubComPortainerPortainerPkgLibhelmReleaseRelease

# TODO update the JSON string below
json = "{}"
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseRelease from a JSON string
github_com_portainer_portainer_pkg_libhelm_release_release_instance = GithubComPortainerPortainerPkgLibhelmReleaseRelease.from_json(json)
# print the JSON string representation of the object
print(GithubComPortainerPortainerPkgLibhelmReleaseRelease.to_json())

# convert the object into a dict
github_com_portainer_portainer_pkg_libhelm_release_release_dict = github_com_portainer_portainer_pkg_libhelm_release_release_instance.to_dict()
# create an instance of GithubComPortainerPortainerPkgLibhelmReleaseRelease from a dict
github_com_portainer_portainer_pkg_libhelm_release_release_from_dict = GithubComPortainerPortainerPkgLibhelmReleaseRelease.from_dict(github_com_portainer_portainer_pkg_libhelm_release_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


