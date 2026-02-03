# KubernetesK8sServiceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocate_load_balancer_node_ports** | **bool** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**applications** | [**List[KubernetesK8sApplication]**](KubernetesK8sApplication.md) | serviceList screen | [optional] 
**cluster_ips** | **List[str]** |  | [optional] 
**creation_date** | **str** |  | [optional] 
**external_ips** | **List[str]** |  | [optional] 
**external_name** | **str** |  | [optional] 
**ingress_status** | [**List[KubernetesK8sServiceIngress]**](KubernetesK8sServiceIngress.md) |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**ports** | [**List[KubernetesK8sServicePort]**](KubernetesK8sServicePort.md) |  | [optional] 
**selector** | **Dict[str, str]** |  | [optional] 
**type** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_service_info import KubernetesK8sServiceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sServiceInfo from a JSON string
kubernetes_k8s_service_info_instance = KubernetesK8sServiceInfo.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sServiceInfo.to_json())

# convert the object into a dict
kubernetes_k8s_service_info_dict = kubernetes_k8s_service_info_instance.to_dict()
# create an instance of KubernetesK8sServiceInfo from a dict
kubernetes_k8s_service_info_from_dict = KubernetesK8sServiceInfo.from_dict(kubernetes_k8s_service_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


