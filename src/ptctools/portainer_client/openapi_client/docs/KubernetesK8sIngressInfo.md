# KubernetesK8sIngressInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**class_name** | **str** |  | [optional] 
**creation_date** | **str** |  | [optional] 
**hosts** | **List[str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**paths** | [**List[KubernetesK8sIngressPath]**](KubernetesK8sIngressPath.md) |  | [optional] 
**tls** | [**List[KubernetesK8sIngressTLS]**](KubernetesK8sIngressTLS.md) |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_ingress_info import KubernetesK8sIngressInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sIngressInfo from a JSON string
kubernetes_k8s_ingress_info_instance = KubernetesK8sIngressInfo.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sIngressInfo.to_json())

# convert the object into a dict
kubernetes_k8s_ingress_info_dict = kubernetes_k8s_ingress_info_instance.to_dict()
# create an instance of KubernetesK8sIngressInfo from a dict
kubernetes_k8s_ingress_info_from_dict = KubernetesK8sIngressInfo.from_dict(kubernetes_k8s_ingress_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


