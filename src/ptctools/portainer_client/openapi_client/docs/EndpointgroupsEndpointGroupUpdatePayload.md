# EndpointgroupsEndpointGroupUpdatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Environment(Endpoint) group description | [optional] 
**name** | **str** | Environment(Endpoint) group name | [optional] 
**tag_ids** | **List[int]** | List of tag identifiers associated to the environment(endpoint) group | [optional] 
**team_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 
**user_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.endpointgroups_endpoint_group_update_payload import EndpointgroupsEndpointGroupUpdatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointgroupsEndpointGroupUpdatePayload from a JSON string
endpointgroups_endpoint_group_update_payload_instance = EndpointgroupsEndpointGroupUpdatePayload.from_json(json)
# print the JSON string representation of the object
print(EndpointgroupsEndpointGroupUpdatePayload.to_json())

# convert the object into a dict
endpointgroups_endpoint_group_update_payload_dict = endpointgroups_endpoint_group_update_payload_instance.to_dict()
# create an instance of EndpointgroupsEndpointGroupUpdatePayload from a dict
endpointgroups_endpoint_group_update_payload_from_dict = EndpointgroupsEndpointGroupUpdatePayload.from_dict(endpointgroups_endpoint_group_update_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


