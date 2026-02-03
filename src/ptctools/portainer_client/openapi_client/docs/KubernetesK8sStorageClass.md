# KubernetesK8sStorageClass


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_volume_expansion** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**provisioner** | **str** |  | [optional] 
**reclaim_policy** | [**V1PersistentVolumeReclaimPolicy**](V1PersistentVolumeReclaimPolicy.md) |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_storage_class import KubernetesK8sStorageClass

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sStorageClass from a JSON string
kubernetes_k8s_storage_class_instance = KubernetesK8sStorageClass.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sStorageClass.to_json())

# convert the object into a dict
kubernetes_k8s_storage_class_dict = kubernetes_k8s_storage_class_instance.to_dict()
# create an instance of KubernetesK8sStorageClass from a dict
kubernetes_k8s_storage_class_from_dict = KubernetesK8sStorageClass.from_dict(kubernetes_k8s_storage_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


