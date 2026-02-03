# EndpointsRegistryAccessPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespaces** | **List[str]** |  | [optional] 
**team_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 
**user_access_policies** | [**Dict[str, PortainerAccessPolicy]**](PortainerAccessPolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.endpoints_registry_access_payload import EndpointsRegistryAccessPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsRegistryAccessPayload from a JSON string
endpoints_registry_access_payload_instance = EndpointsRegistryAccessPayload.from_json(json)
# print the JSON string representation of the object
print(EndpointsRegistryAccessPayload.to_json())

# convert the object into a dict
endpoints_registry_access_payload_dict = endpoints_registry_access_payload_instance.to_dict()
# create an instance of EndpointsRegistryAccessPayload from a dict
endpoints_registry_access_payload_from_dict = EndpointsRegistryAccessPayload.from_dict(endpoints_registry_access_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


