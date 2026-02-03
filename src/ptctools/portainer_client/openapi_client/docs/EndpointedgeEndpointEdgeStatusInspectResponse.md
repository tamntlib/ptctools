# EndpointedgeEndpointEdgeStatusInspectResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkin** | **int** | The current value of CheckinInterval | [optional] 
**credentials** | **str** |  | [optional] 
**port** | **int** | The tunnel port | [optional] 
**schedules** | [**List[EndpointedgeEdgeJobResponse]**](EndpointedgeEdgeJobResponse.md) | List of requests for jobs to run on the environment(endpoint) | [optional] 
**stacks** | [**List[EndpointedgeStackStatusResponse]**](EndpointedgeStackStatusResponse.md) | List of stacks to be deployed on the environments(endpoints) | [optional] 
**status** | **str** | Status represents the environment(endpoint) status | [optional] 

## Example

```python
from openapi_client.models.endpointedge_endpoint_edge_status_inspect_response import EndpointedgeEndpointEdgeStatusInspectResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointedgeEndpointEdgeStatusInspectResponse from a JSON string
endpointedge_endpoint_edge_status_inspect_response_instance = EndpointedgeEndpointEdgeStatusInspectResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointedgeEndpointEdgeStatusInspectResponse.to_json())

# convert the object into a dict
endpointedge_endpoint_edge_status_inspect_response_dict = endpointedge_endpoint_edge_status_inspect_response_instance.to_dict()
# create an instance of EndpointedgeEndpointEdgeStatusInspectResponse from a dict
endpointedge_endpoint_edge_status_inspect_response_from_dict = EndpointedgeEndpointEdgeStatusInspectResponse.from_dict(endpointedge_endpoint_edge_status_inspect_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


