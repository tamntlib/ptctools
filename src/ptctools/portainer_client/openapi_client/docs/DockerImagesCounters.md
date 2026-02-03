# DockerImagesCounters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.docker_images_counters import DockerImagesCounters

# TODO update the JSON string below
json = "{}"
# create an instance of DockerImagesCounters from a JSON string
docker_images_counters_instance = DockerImagesCounters.from_json(json)
# print the JSON string representation of the object
print(DockerImagesCounters.to_json())

# convert the object into a dict
docker_images_counters_dict = docker_images_counters_instance.to_dict()
# create an instance of DockerImagesCounters from a dict
docker_images_counters_from_dict = DockerImagesCounters.from_dict(docker_images_counters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


