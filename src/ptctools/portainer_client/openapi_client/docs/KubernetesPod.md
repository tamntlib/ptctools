# KubernetesPod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**container_name** | **str** |  | [optional] 
**creation_date** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**image_pull_policy** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**node_name** | **str** |  | [optional] 
**pod_ip** | **str** |  | [optional] 
**resource** | [**KubernetesK8sApplicationResource**](KubernetesK8sApplicationResource.md) |  | [optional] 
**status** | **str** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_pod import KubernetesPod

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesPod from a JSON string
kubernetes_pod_instance = KubernetesPod.from_json(json)
# print the JSON string representation of the object
print(KubernetesPod.to_json())

# convert the object into a dict
kubernetes_pod_dict = kubernetes_pod_instance.to_dict()
# create an instance of KubernetesPod from a dict
kubernetes_pod_from_dict = KubernetesPod.from_dict(kubernetes_pod_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


