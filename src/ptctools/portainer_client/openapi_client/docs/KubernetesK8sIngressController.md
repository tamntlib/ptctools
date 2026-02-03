# KubernetesK8sIngressController


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | **bool** |  | [optional] 
**class_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**new** | **bool** |  | [optional] 
**type** | **str** |  | [optional] 
**used** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_ingress_controller import KubernetesK8sIngressController

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sIngressController from a JSON string
kubernetes_k8s_ingress_controller_instance = KubernetesK8sIngressController.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sIngressController.to_json())

# convert the object into a dict
kubernetes_k8s_ingress_controller_dict = kubernetes_k8s_ingress_controller_instance.to_dict()
# create an instance of KubernetesK8sIngressController from a dict
kubernetes_k8s_ingress_controller_from_dict = KubernetesK8sIngressController.from_dict(kubernetes_k8s_ingress_controller_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


