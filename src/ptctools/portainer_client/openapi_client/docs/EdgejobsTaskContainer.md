# EdgejobsTaskContainer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint_id** | **int** |  | [optional] 
**endpoint_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**logs_status** | [**PortainerEdgeJobLogsStatus**](PortainerEdgeJobLogsStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.edgejobs_task_container import EdgejobsTaskContainer

# TODO update the JSON string below
json = "{}"
# create an instance of EdgejobsTaskContainer from a JSON string
edgejobs_task_container_instance = EdgejobsTaskContainer.from_json(json)
# print the JSON string representation of the object
print(EdgejobsTaskContainer.to_json())

# convert the object into a dict
edgejobs_task_container_dict = edgejobs_task_container_instance.to_dict()
# create an instance of EdgejobsTaskContainer from a dict
edgejobs_task_container_from_dict = EdgejobsTaskContainer.from_dict(edgejobs_task_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


