# PortainerKubernetesIngressClassConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blocked** | **bool** |  | [optional] 
**blocked_namespaces** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_kubernetes_ingress_class_config import PortainerKubernetesIngressClassConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerKubernetesIngressClassConfig from a JSON string
portainer_kubernetes_ingress_class_config_instance = PortainerKubernetesIngressClassConfig.from_json(json)
# print the JSON string representation of the object
print(PortainerKubernetesIngressClassConfig.to_json())

# convert the object into a dict
portainer_kubernetes_ingress_class_config_dict = portainer_kubernetes_ingress_class_config_instance.to_dict()
# create an instance of PortainerKubernetesIngressClassConfig from a dict
portainer_kubernetes_ingress_class_config_from_dict = PortainerKubernetesIngressClassConfig.from_dict(portainer_kubernetes_ingress_class_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


