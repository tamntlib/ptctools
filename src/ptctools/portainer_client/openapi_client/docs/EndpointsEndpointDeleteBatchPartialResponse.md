# EndpointsEndpointDeleteBatchPartialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted** | **List[int]** |  | [optional] 
**errors** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.endpoints_endpoint_delete_batch_partial_response import EndpointsEndpointDeleteBatchPartialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsEndpointDeleteBatchPartialResponse from a JSON string
endpoints_endpoint_delete_batch_partial_response_instance = EndpointsEndpointDeleteBatchPartialResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointsEndpointDeleteBatchPartialResponse.to_json())

# convert the object into a dict
endpoints_endpoint_delete_batch_partial_response_dict = endpoints_endpoint_delete_batch_partial_response_instance.to_dict()
# create an instance of EndpointsEndpointDeleteBatchPartialResponse from a dict
endpoints_endpoint_delete_batch_partial_response_from_dict = EndpointsEndpointDeleteBatchPartialResponse.from_dict(endpoints_endpoint_delete_batch_partial_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


