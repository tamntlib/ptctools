# EndpointsEndpointDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_cluster** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.endpoints_endpoint_delete_request import EndpointsEndpointDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsEndpointDeleteRequest from a JSON string
endpoints_endpoint_delete_request_instance = EndpointsEndpointDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(EndpointsEndpointDeleteRequest.to_json())

# convert the object into a dict
endpoints_endpoint_delete_request_dict = endpoints_endpoint_delete_request_instance.to_dict()
# create an instance of EndpointsEndpointDeleteRequest from a dict
endpoints_endpoint_delete_request_from_dict = EndpointsEndpointDeleteRequest.from_dict(endpoints_endpoint_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


