# KubernetesK8sServiceAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_date** | **str** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_service_account import KubernetesK8sServiceAccount

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sServiceAccount from a JSON string
kubernetes_k8s_service_account_instance = KubernetesK8sServiceAccount.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sServiceAccount.to_json())

# convert the object into a dict
kubernetes_k8s_service_account_dict = kubernetes_k8s_service_account_instance.to_dict()
# create an instance of KubernetesK8sServiceAccount from a dict
kubernetes_k8s_service_account_from_dict = KubernetesK8sServiceAccount.from_dict(kubernetes_k8s_service_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


