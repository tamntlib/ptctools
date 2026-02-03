# BuildBuildInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_number** | **str** |  | [optional] 
**git_commit** | **str** |  | [optional] 
**go_version** | **str** |  | [optional] 
**image_tag** | **str** |  | [optional] 
**nodejs_version** | **str** |  | [optional] 
**webpack_version** | **str** |  | [optional] 
**yarn_version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.build_build_info import BuildBuildInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BuildBuildInfo from a JSON string
build_build_info_instance = BuildBuildInfo.from_json(json)
# print the JSON string representation of the object
print(BuildBuildInfo.to_json())

# convert the object into a dict
build_build_info_dict = build_build_info_instance.to_dict()
# create an instance of BuildBuildInfo from a dict
build_build_info_from_dict = BuildBuildInfo.from_dict(build_build_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


