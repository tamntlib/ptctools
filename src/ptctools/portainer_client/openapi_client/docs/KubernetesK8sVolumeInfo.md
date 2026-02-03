# KubernetesK8sVolumeInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persistent_volume** | [**KubernetesK8sPersistentVolume**](KubernetesK8sPersistentVolume.md) |  | [optional] 
**persistent_volume_claim** | [**KubernetesK8sPersistentVolumeClaim**](KubernetesK8sPersistentVolumeClaim.md) |  | [optional] 
**storage_class** | [**KubernetesK8sStorageClass**](KubernetesK8sStorageClass.md) |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_volume_info import KubernetesK8sVolumeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sVolumeInfo from a JSON string
kubernetes_k8s_volume_info_instance = KubernetesK8sVolumeInfo.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sVolumeInfo.to_json())

# convert the object into a dict
kubernetes_k8s_volume_info_dict = kubernetes_k8s_volume_info_instance.to_dict()
# create an instance of KubernetesK8sVolumeInfo from a dict
kubernetes_k8s_volume_info_from_dict = KubernetesK8sVolumeInfo.from_dict(kubernetes_k8s_volume_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


