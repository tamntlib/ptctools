# EndpointsForceUpdateServicePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pull_image** | **bool** | PullImage if true will pull the image | [optional] 
**service_id** | **str** | ServiceId to update | [optional] 

## Example

```python
from openapi_client.models.endpoints_force_update_service_payload import EndpointsForceUpdateServicePayload

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointsForceUpdateServicePayload from a JSON string
endpoints_force_update_service_payload_instance = EndpointsForceUpdateServicePayload.from_json(json)
# print the JSON string representation of the object
print(EndpointsForceUpdateServicePayload.to_json())

# convert the object into a dict
endpoints_force_update_service_payload_dict = endpoints_force_update_service_payload_instance.to_dict()
# create an instance of EndpointsForceUpdateServicePayload from a dict
endpoints_force_update_service_payload_from_dict = EndpointsForceUpdateServicePayload.from_dict(endpoints_force_update_service_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


