# EndpointedgeStackStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | EdgeStack Identifier | [optional] 
**version** | **int** | Version of this stack | [optional] 

## Example

```python
from openapi_client.models.endpointedge_stack_status_response import EndpointedgeStackStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointedgeStackStatusResponse from a JSON string
endpointedge_stack_status_response_instance = EndpointedgeStackStatusResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointedgeStackStatusResponse.to_json())

# convert the object into a dict
endpointedge_stack_status_response_dict = endpointedge_stack_status_response_instance.to_dict()
# create an instance of EndpointedgeStackStatusResponse from a dict
endpointedge_stack_status_response_from_dict = EndpointedgeStackStatusResponse.from_dict(endpointedge_stack_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


