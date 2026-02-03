# KubernetesK8sPersistentVolumeClaim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_modes** | [**List[V1PersistentVolumeAccessMode]**](V1PersistentVolumeAccessMode.md) |  | [optional] 
**creation_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**owning_applications** | [**List[KubernetesK8sApplication]**](KubernetesK8sApplication.md) |  | [optional] 
**phase** | [**V1PersistentVolumeClaimPhase**](V1PersistentVolumeClaimPhase.md) |  | [optional] 
**resources_requests** | [**Dict[str, ResourceQuantity]**](ResourceQuantity.md) |  | [optional] 
**storage** | **int** |  | [optional] 
**storage_class** | **str** |  | [optional] 
**volume_mode** | [**V1PersistentVolumeMode**](V1PersistentVolumeMode.md) |  | [optional] 
**volume_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_persistent_volume_claim import KubernetesK8sPersistentVolumeClaim

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sPersistentVolumeClaim from a JSON string
kubernetes_k8s_persistent_volume_claim_instance = KubernetesK8sPersistentVolumeClaim.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sPersistentVolumeClaim.to_json())

# convert the object into a dict
kubernetes_k8s_persistent_volume_claim_dict = kubernetes_k8s_persistent_volume_claim_instance.to_dict()
# create an instance of KubernetesK8sPersistentVolumeClaim from a dict
kubernetes_k8s_persistent_volume_claim_from_dict = KubernetesK8sPersistentVolumeClaim.from_dict(kubernetes_k8s_persistent_volume_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


