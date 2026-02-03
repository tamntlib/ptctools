# KubernetesK8sResourceQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**memory** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_resource_quota import KubernetesK8sResourceQuota

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sResourceQuota from a JSON string
kubernetes_k8s_resource_quota_instance = KubernetesK8sResourceQuota.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sResourceQuota.to_json())

# convert the object into a dict
kubernetes_k8s_resource_quota_dict = kubernetes_k8s_resource_quota_instance.to_dict()
# create an instance of KubernetesK8sResourceQuota from a dict
kubernetes_k8s_resource_quota_from_dict = KubernetesK8sResourceQuota.from_dict(kubernetes_k8s_resource_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


