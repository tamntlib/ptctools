# PortainerEdgeJobEndpointMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collect_logs** | **bool** |  | [optional] 
**logs_status** | [**PortainerEdgeJobLogsStatus**](PortainerEdgeJobLogsStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.portainer_edge_job_endpoint_meta import PortainerEdgeJobEndpointMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdgeJobEndpointMeta from a JSON string
portainer_edge_job_endpoint_meta_instance = PortainerEdgeJobEndpointMeta.from_json(json)
# print the JSON string representation of the object
print(PortainerEdgeJobEndpointMeta.to_json())

# convert the object into a dict
portainer_edge_job_endpoint_meta_dict = portainer_edge_job_endpoint_meta_instance.to_dict()
# create an instance of PortainerEdgeJobEndpointMeta from a dict
portainer_edge_job_endpoint_meta_from_dict = PortainerEdgeJobEndpointMeta.from_dict(portainer_edge_job_endpoint_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


