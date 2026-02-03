# EndpointsDockerhubStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | Daily limit | [optional] 
**remaining** | **int** | Remaiming images to pull | [optional] 

## Example

```python
from openapi_client.models.endpoints_dockerhub_status_response import EndpointsDockerhubStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsDockerhubStatusResponse from a JSON string
endpoints_dockerhub_status_response_instance = EndpointsDockerhubStatusResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointsDockerhubStatusResponse.to_json())

# convert the object into a dict
endpoints_dockerhub_status_response_dict = endpoints_dockerhub_status_response_instance.to_dict()
# create an instance of EndpointsDockerhubStatusResponse from a dict
endpoints_dockerhub_status_response_from_dict = EndpointsDockerhubStatusResponse.from_dict(endpoints_dockerhub_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


