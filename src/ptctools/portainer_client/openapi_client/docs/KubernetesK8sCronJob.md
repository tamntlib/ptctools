# KubernetesK8sCronJob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_system** | **bool** |  | [optional] 
**jobs** | [**List[KubernetesK8sJob]**](KubernetesK8sJob.md) |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**schedule** | **str** |  | [optional] 
**suspend** | **bool** |  | [optional] 
**timezone** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_cron_job import KubernetesK8sCronJob

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sCronJob from a JSON string
kubernetes_k8s_cron_job_instance = KubernetesK8sCronJob.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sCronJob.to_json())

# convert the object into a dict
kubernetes_k8s_cron_job_dict = kubernetes_k8s_cron_job_instance.to_dict()
# create an instance of KubernetesK8sCronJob from a dict
kubernetes_k8s_cron_job_from_dict = KubernetesK8sCronJob.from_dict(kubernetes_k8s_cron_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


