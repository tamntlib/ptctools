# SystemVersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latest_version** | **str** | The latest version available | [optional] 
**server_edition** | **str** |  | [optional] 
**update_available** | **bool** | Whether portainer has an update available | [optional] 
**version_support** | **str** |  | [optional] 
**build** | [**BuildBuildInfo**](BuildBuildInfo.md) |  | [optional] 
**database_version** | **str** |  | [optional] 
**dependencies** | [**BuildDependenciesInfo**](BuildDependenciesInfo.md) |  | [optional] 
**runtime** | [**BuildRuntimeInfo**](BuildRuntimeInfo.md) |  | [optional] 
**server_version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.system_version_response import SystemVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemVersionResponse from a JSON string
system_version_response_instance = SystemVersionResponse.from_json(json)
# print the JSON string representation of the object
print(SystemVersionResponse.to_json())

# convert the object into a dict
system_version_response_dict = system_version_response_instance.to_dict()
# create an instance of SystemVersionResponse from a dict
system_version_response_from_dict = SystemVersionResponse.from_dict(system_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


