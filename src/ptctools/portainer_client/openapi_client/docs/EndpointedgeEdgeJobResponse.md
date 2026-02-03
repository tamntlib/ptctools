# EndpointedgeEdgeJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collect_logs** | **bool** | Whether to collect logs | [optional] 
**cron_expression** | **str** | A cron expression to schedule this job | [optional] 
**id** | **int** | EdgeJob Identifier | [optional] 
**script** | **str** | Script to run | [optional] 
**version** | **int** | Version of this EdgeJob | [optional] 

## Example

```python
from openapi_client.models.endpointedge_edge_job_response import EndpointedgeEdgeJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EndpointedgeEdgeJobResponse from a JSON string
endpointedge_edge_job_response_instance = EndpointedgeEdgeJobResponse.from_json(json)
# print the JSON string representation of the object
print(EndpointedgeEdgeJobResponse.to_json())

# convert the object into a dict
endpointedge_edge_job_response_dict = endpointedge_edge_job_response_instance.to_dict()
# create an instance of EndpointedgeEdgeJobResponse from a dict
endpointedge_edge_job_response_from_dict = EndpointedgeEdgeJobResponse.from_dict(endpointedge_edge_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


