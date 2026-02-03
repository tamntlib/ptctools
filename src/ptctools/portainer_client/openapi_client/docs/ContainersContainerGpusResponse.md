# ContainersContainerGpusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gpus** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.containers_container_gpus_response import ContainersContainerGpusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainersContainerGpusResponse from a JSON string
containers_container_gpus_response_instance = ContainersContainerGpusResponse.from_json(json)
# print the JSON string representation of the object
print(ContainersContainerGpusResponse.to_json())

# convert the object into a dict
containers_container_gpus_response_dict = containers_container_gpus_response_instance.to_dict()
# create an instance of ContainersContainerGpusResponse from a dict
containers_container_gpus_response_from_dict = ContainersContainerGpusResponse.from_dict(containers_container_gpus_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


