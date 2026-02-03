# EndpointsEndpointUpdateRelationsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relations** | [**Dict[str, EndpointsEndpointUpdateRelationsPayloadRelationsValue]**](EndpointsEndpointUpdateRelationsPayloadRelationsValue.md) |  | [optional] 

## Example

```python
from openapi_client.models.endpoints_endpoint_update_relations_payload import EndpointsEndpointUpdateRelationsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsEndpointUpdateRelationsPayload from a JSON string
endpoints_endpoint_update_relations_payload_instance = EndpointsEndpointUpdateRelationsPayload.from_json(json)
# print the JSON string representation of the object
print(EndpointsEndpointUpdateRelationsPayload.to_json())

# convert the object into a dict
endpoints_endpoint_update_relations_payload_dict = endpoints_endpoint_update_relations_payload_instance.to_dict()
# create an instance of EndpointsEndpointUpdateRelationsPayload from a dict
endpoints_endpoint_update_relations_payload_from_dict = EndpointsEndpointUpdateRelationsPayload.from_dict(endpoints_endpoint_update_relations_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


