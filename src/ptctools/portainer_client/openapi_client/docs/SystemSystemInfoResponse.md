# SystemSystemInfoResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agents** | **int** |  | [optional] 
**edge_agents** | **int** |  | [optional] 
**platform** | [**PlatformContainerPlatform**](PlatformContainerPlatform.md) |  | [optional] 

## Example

```python
from openapi_client.models.system_system_info_response import SystemSystemInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSystemInfoResponse from a JSON string
system_system_info_response_instance = SystemSystemInfoResponse.from_json(json)
# print the JSON string representation of the object
print(SystemSystemInfoResponse.to_json())

# convert the object into a dict
system_system_info_response_dict = system_system_info_response_instance.to_dict()
# create an instance of SystemSystemInfoResponse from a dict
system_system_info_response_from_dict = SystemSystemInfoResponse.from_dict(system_system_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


