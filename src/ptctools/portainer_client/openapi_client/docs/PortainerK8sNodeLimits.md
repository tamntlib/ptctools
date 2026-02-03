# PortainerK8sNodeLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **int** |  | [optional] 
**memory** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_k8s_node_limits import PortainerK8sNodeLimits

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerK8sNodeLimits from a JSON string
portainer_k8s_node_limits_instance = PortainerK8sNodeLimits.from_json(json)
# print the JSON string representation of the object
print(PortainerK8sNodeLimits.to_json())

# convert the object into a dict
portainer_k8s_node_limits_dict = portainer_k8s_node_limits_instance.to_dict()
# create an instance of PortainerK8sNodeLimits from a dict
portainer_k8s_node_limits_from_dict = PortainerK8sNodeLimits.from_dict(portainer_k8s_node_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


