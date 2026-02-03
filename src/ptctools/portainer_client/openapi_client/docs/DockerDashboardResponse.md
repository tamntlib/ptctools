# DockerDashboardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containers** | [**DockerContainerStats**](DockerContainerStats.md) |  | [optional] 
**images** | [**DockerImagesCounters**](DockerImagesCounters.md) |  | [optional] 
**networks** | **int** |  | [optional] 
**services** | **int** |  | [optional] 
**stacks** | **int** |  | [optional] 
**volumes** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.docker_dashboard_response import DockerDashboardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DockerDashboardResponse from a JSON string
docker_dashboard_response_instance = DockerDashboardResponse.from_json(json)
# print the JSON string representation of the object
print(DockerDashboardResponse.to_json())

# convert the object into a dict
docker_dashboard_response_dict = docker_dashboard_response_instance.to_dict()
# create an instance of DockerDashboardResponse from a dict
docker_dashboard_response_from_dict = DockerDashboardResponse.from_dict(docker_dashboard_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


