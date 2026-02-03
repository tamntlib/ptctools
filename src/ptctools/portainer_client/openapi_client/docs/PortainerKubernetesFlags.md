# PortainerKubernetesFlags


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_server_ingress_class_detected** | **bool** |  | [optional] 
**is_server_metrics_detected** | **bool** |  | [optional] 
**is_server_storage_detected** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_kubernetes_flags import PortainerKubernetesFlags

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerKubernetesFlags from a JSON string
portainer_kubernetes_flags_instance = PortainerKubernetesFlags.from_json(json)
# print the JSON string representation of the object
print(PortainerKubernetesFlags.to_json())

# convert the object into a dict
portainer_kubernetes_flags_dict = portainer_kubernetes_flags_instance.to_dict()
# create an instance of PortainerKubernetesFlags from a dict
portainer_kubernetes_flags_from_dict = PortainerKubernetesFlags.from_dict(portainer_kubernetes_flags_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


