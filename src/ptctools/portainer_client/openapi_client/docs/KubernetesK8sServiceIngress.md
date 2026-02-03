# KubernetesK8sServiceIngress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_service_ingress import KubernetesK8sServiceIngress

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sServiceIngress from a JSON string
kubernetes_k8s_service_ingress_instance = KubernetesK8sServiceIngress.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sServiceIngress.to_json())

# convert the object into a dict
kubernetes_k8s_service_ingress_dict = kubernetes_k8s_service_ingress_instance.to_dict()
# create an instance of KubernetesK8sServiceIngress from a dict
kubernetes_k8s_service_ingress_from_dict = KubernetesK8sServiceIngress.from_dict(kubernetes_k8s_service_ingress_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


