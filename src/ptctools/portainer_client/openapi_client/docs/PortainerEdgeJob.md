# PortainerEdgeJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **int** |  | [optional] 
**cron_expression** | **str** |  | [optional] 
**edge_groups** | **List[int]** |  | [optional] 
**endpoints** | [**Dict[str, PortainerEdgeJobEndpointMeta]**](PortainerEdgeJobEndpointMeta.md) |  | [optional] 
**id** | **int** | EdgeJob Identifier | [optional] 
**name** | **str** |  | [optional] 
**recurring** | **bool** |  | [optional] 
**script_path** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**group_logs_collection** | [**Dict[str, PortainerEdgeJobEndpointMeta]**](PortainerEdgeJobEndpointMeta.md) | Field used for log collection of Endpoints belonging to EdgeGroups | [optional] 

## Example

```python
from openapi_client.models.portainer_edge_job import PortainerEdgeJob

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdgeJob from a JSON string
portainer_edge_job_instance = PortainerEdgeJob.from_json(json)
# print the JSON string representation of the object
print(PortainerEdgeJob.to_json())

# convert the object into a dict
portainer_edge_job_dict = portainer_edge_job_instance.to_dict()
# create an instance of PortainerEdgeJob from a dict
portainer_edge_job_from_dict = PortainerEdgeJob.from_dict(portainer_edge_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


