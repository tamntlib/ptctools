# KubernetesK8sServicePort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**node_port** | **int** |  | [optional] 
**port** | **int** |  | [optional] 
**protocol** | **str** |  | [optional] 
**target_port** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_service_port import KubernetesK8sServicePort

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sServicePort from a JSON string
kubernetes_k8s_service_port_instance = KubernetesK8sServicePort.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sServicePort.to_json())

# convert the object into a dict
kubernetes_k8s_service_port_dict = kubernetes_k8s_service_port_instance.to_dict()
# create an instance of KubernetesK8sServicePort from a dict
kubernetes_k8s_service_port_from_dict = KubernetesK8sServicePort.from_dict(kubernetes_k8s_service_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


