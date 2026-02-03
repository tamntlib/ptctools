# KubernetesK8sPersistentVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | [**List[V1PersistentVolumeAccessMode]**](V1PersistentVolumeAccessMode.md) |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**capacity** | [**Dict[str, ResourceQuantity]**](ResourceQuantity.md) |  | [optional] 
**claim_ref** | [**V1ObjectReference**](V1ObjectReference.md) |  | [optional] 
**csi** | [**V1CSIPersistentVolumeSource**](V1CSIPersistentVolumeSource.md) |  | [optional] 
**name** | **str** |  | [optional] 
**persistent_volume_reclaim_policy** | [**V1PersistentVolumeReclaimPolicy**](V1PersistentVolumeReclaimPolicy.md) |  | [optional] 
**storage_class_name** | **str** |  | [optional] 
**volume_mode** | [**V1PersistentVolumeMode**](V1PersistentVolumeMode.md) |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_persistent_volume import KubernetesK8sPersistentVolume

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sPersistentVolume from a JSON string
kubernetes_k8s_persistent_volume_instance = KubernetesK8sPersistentVolume.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sPersistentVolume.to_json())

# convert the object into a dict
kubernetes_k8s_persistent_volume_dict = kubernetes_k8s_persistent_volume_instance.to_dict()
# create an instance of KubernetesK8sPersistentVolume from a dict
kubernetes_k8s_persistent_volume_from_dict = KubernetesK8sPersistentVolume.from_dict(kubernetes_k8s_persistent_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


