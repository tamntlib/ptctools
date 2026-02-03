# DockerContainerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthy** | **int** |  | [optional] 
**running** | **int** |  | [optional] 
**stopped** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**unhealthy** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.docker_container_stats import DockerContainerStats

# TODO update the JSON string below
json = "{}"
# create an instance of DockerContainerStats from a JSON string
docker_container_stats_instance = DockerContainerStats.from_json(json)
# print the JSON string representation of the object
print(DockerContainerStats.to_json())

# convert the object into a dict
docker_container_stats_dict = docker_container_stats_instance.to_dict()
# create an instance of DockerContainerStats from a dict
docker_container_stats_from_dict = DockerContainerStats.from_dict(docker_container_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


