# PortainerKubernetesConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_none_ingress_class** | **bool** |  | [optional] 
**enable_resource_over_commit** | **bool** |  | [optional] 
**ingress_availability_per_namespace** | **bool** |  | [optional] 
**ingress_classes** | [**List[PortainerKubernetesIngressClassConfig]**](PortainerKubernetesIngressClassConfig.md) |  | [optional] 
**resource_over_commit_percentage** | **int** |  | [optional] 
**restrict_default_namespace** | **bool** |  | [optional] 
**storage_classes** | [**List[PortainerKubernetesStorageClassConfig]**](PortainerKubernetesStorageClassConfig.md) |  | [optional] 
**use_load_balancer** | **bool** |  | [optional] 
**use_server_metrics** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.portainer_kubernetes_configuration import PortainerKubernetesConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PortainerKubernetesConfiguration from a JSON string
portainer_kubernetes_configuration_instance = PortainerKubernetesConfiguration.from_json(json)
# print the JSON string representation of the object
print(PortainerKubernetesConfiguration.to_json())

# convert the object into a dict
portainer_kubernetes_configuration_dict = portainer_kubernetes_configuration_instance.to_dict()
# create an instance of PortainerKubernetesConfiguration from a dict
portainer_kubernetes_configuration_from_dict = PortainerKubernetesConfiguration.from_dict(portainer_kubernetes_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


