# KubernetesK8sIngressPath


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_service** | **bool** |  | [optional] 
**host** | **str** |  | [optional] 
**ingress_name** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**path_type** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**service_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_ingress_path import KubernetesK8sIngressPath

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sIngressPath from a JSON string
kubernetes_k8s_ingress_path_instance = KubernetesK8sIngressPath.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sIngressPath.to_json())

# convert the object into a dict
kubernetes_k8s_ingress_path_dict = kubernetes_k8s_ingress_path_instance.to_dict()
# create an instance of KubernetesK8sIngressPath from a dict
kubernetes_k8s_ingress_path_from_dict = KubernetesK8sIngressPath.from_dict(kubernetes_k8s_ingress_path_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


