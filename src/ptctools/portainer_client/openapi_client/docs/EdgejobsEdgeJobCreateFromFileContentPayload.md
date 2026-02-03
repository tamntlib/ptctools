# EdgejobsEdgeJobCreateFromFileContentPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cron_expression** | **str** |  | [optional] 
**edge_groups** | **List[int]** |  | [optional] 
**endpoints** | **List[int]** |  | [optional] 
**file_content** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**recurring** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.edgejobs_edge_job_create_from_file_content_payload import EdgejobsEdgeJobCreateFromFileContentPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EdgejobsEdgeJobCreateFromFileContentPayload from a JSON string
edgejobs_edge_job_create_from_file_content_payload_instance = EdgejobsEdgeJobCreateFromFileContentPayload.from_json(json)
# print the JSON string representation of the object
print(EdgejobsEdgeJobCreateFromFileContentPayload.to_json())

# convert the object into a dict
edgejobs_edge_job_create_from_file_content_payload_dict = edgejobs_edge_job_create_from_file_content_payload_instance.to_dict()
# create an instance of EdgejobsEdgeJobCreateFromFileContentPayload from a dict
edgejobs_edge_job_create_from_file_content_payload_from_dict = EdgejobsEdgeJobCreateFromFileContentPayload.from_dict(edgejobs_edge_job_create_from_file_content_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


