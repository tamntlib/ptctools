# KubernetesK8sIngressTLS


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | **List[str]** |  | [optional] 
**secret_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_ingress_tls import KubernetesK8sIngressTLS

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sIngressTLS from a JSON string
kubernetes_k8s_ingress_tls_instance = KubernetesK8sIngressTLS.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sIngressTLS.to_json())

# convert the object into a dict
kubernetes_k8s_ingress_tls_dict = kubernetes_k8s_ingress_tls_instance.to_dict()
# create an instance of KubernetesK8sIngressTLS from a dict
kubernetes_k8s_ingress_tls_from_dict = KubernetesK8sIngressTLS.from_dict(kubernetes_k8s_ingress_tls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


