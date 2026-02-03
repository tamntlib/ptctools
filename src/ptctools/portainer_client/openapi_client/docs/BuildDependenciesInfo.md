# BuildDependenciesInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compose_version** | **str** |  | [optional] 
**docker_version** | **str** |  | [optional] 
**helm_version** | **str** |  | [optional] 
**kubectl_version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.build_dependencies_info import BuildDependenciesInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BuildDependenciesInfo from a JSON string
build_dependencies_info_instance = BuildDependenciesInfo.from_json(json)
# print the JSON string representation of the object
print(BuildDependenciesInfo.to_json())

# convert the object into a dict
build_dependencies_info_dict = build_dependencies_info_instance.to_dict()
# create an instance of BuildDependenciesInfo from a dict
build_dependencies_info_from_dict = BuildDependenciesInfo.from_dict(build_dependencies_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


