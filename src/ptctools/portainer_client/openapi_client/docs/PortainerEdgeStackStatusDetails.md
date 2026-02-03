# PortainerEdgeStackStatusDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledged** | **bool** |  | [optional] 
**error** | **bool** |  | [optional] 
**images_pulled** | **bool** |  | [optional] 
**ok** | **bool** |  | [optional] 
**pending** | **bool** |  | [optional] 
**remote_update_success** | **bool** |  | [optional] 
**remove** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_edge_stack_status_details import PortainerEdgeStackStatusDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerEdgeStackStatusDetails from a JSON string
portainer_edge_stack_status_details_instance = PortainerEdgeStackStatusDetails.from_json(json)
# print the JSON string representation of the object
print(PortainerEdgeStackStatusDetails.to_json())

# convert the object into a dict
portainer_edge_stack_status_details_dict = portainer_edge_stack_status_details_instance.to_dict()
# create an instance of PortainerEdgeStackStatusDetails from a dict
portainer_edge_stack_status_details_from_dict = PortainerEdgeStackStatusDetails.from_dict(portainer_edge_stack_status_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


