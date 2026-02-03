# EndpointgroupsEndpointGroupCreatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_endpoints** | **List[int]** | List of environment(endpoint) identifiers that will be part of this group | [optional] 
**description** | **str** | Environment(Endpoint) group description | [optional] 
**name** | **str** | Environment(Endpoint) group name | 
**tag_ids** | **List[int]** | List of tag identifiers to which this environment(endpoint) group is associated | [optional] 

## Example

```python
from openapi_client.models.endpointgroups_endpoint_group_create_payload import EndpointgroupsEndpointGroupCreatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointgroupsEndpointGroupCreatePayload from a JSON string
endpointgroups_endpoint_group_create_payload_instance = EndpointgroupsEndpointGroupCreatePayload.from_json(json)
# print the JSON string representation of the object
print(EndpointgroupsEndpointGroupCreatePayload.to_json())

# convert the object into a dict
endpointgroups_endpoint_group_create_payload_dict = endpointgroups_endpoint_group_create_payload_instance.to_dict()
# create an instance of EndpointgroupsEndpointGroupCreatePayload from a dict
endpointgroups_endpoint_group_create_payload_from_dict = EndpointgroupsEndpointGroupCreatePayload.from_dict(endpointgroups_endpoint_group_create_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


