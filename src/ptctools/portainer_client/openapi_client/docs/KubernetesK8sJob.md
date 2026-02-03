# KubernetesK8sJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backoff_limit** | **int** |  | [optional] 
**command** | **str** |  | [optional] 
**completions** | **int** |  | [optional] 
**container** | [**V1Container**](V1Container.md) |  | [optional] 
**duration** | **str** |  | [optional] 
**failed_reason** | **str** |  | [optional] 
**finish_time** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**pod_name** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_job import KubernetesK8sJob

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sJob from a JSON string
kubernetes_k8s_job_instance = KubernetesK8sJob.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sJob.to_json())

# convert the object into a dict
kubernetes_k8s_job_dict = kubernetes_k8s_job_instance.to_dict()
# create an instance of KubernetesK8sJob from a dict
kubernetes_k8s_job_from_dict = KubernetesK8sJob.from_dict(kubernetes_k8s_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


