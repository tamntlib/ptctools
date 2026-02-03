# EdgestacksUpdateStatusPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **int** |  | [optional] 
**error** | **str** |  | [optional] 
**status** | [**PortainerEdgeStackStatusType**](PortainerEdgeStackStatusType.md) |  | [optional] 
**time** | **int** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.edgestacks_update_status_payload import EdgestacksUpdateStatusPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgestacksUpdateStatusPayload from a JSON string
edgestacks_update_status_payload_instance = EdgestacksUpdateStatusPayload.from_json(json)
# print the JSON string representation of the object
print(EdgestacksUpdateStatusPayload.to_json())

# convert the object into a dict
edgestacks_update_status_payload_dict = edgestacks_update_status_payload_instance.to_dict()
# create an instance of EdgestacksUpdateStatusPayload from a dict
edgestacks_update_status_payload_from_dict = EdgestacksUpdateStatusPayload.from_dict(edgestacks_update_status_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


