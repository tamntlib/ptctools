# EndpointsEndpointDeleteBatchPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoints** | [**List[EndpointsEndpointDeleteRequest]**](EndpointsEndpointDeleteRequest.md) |  | [optional] 

## Example

```python
from openapi_client.models.endpoints_endpoint_delete_batch_payload import EndpointsEndpointDeleteBatchPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsEndpointDeleteBatchPayload from a JSON string
endpoints_endpoint_delete_batch_payload_instance = EndpointsEndpointDeleteBatchPayload.from_json(json)
# print the JSON string representation of the object
print(EndpointsEndpointDeleteBatchPayload.to_json())

# convert the object into a dict
endpoints_endpoint_delete_batch_payload_dict = endpoints_endpoint_delete_batch_payload_instance.to_dict()
# create an instance of EndpointsEndpointDeleteBatchPayload from a dict
endpoints_endpoint_delete_batch_payload_from_dict = EndpointsEndpointDeleteBatchPayload.from_dict(endpoints_endpoint_delete_batch_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


