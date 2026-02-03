# KubernetesK8sApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **Dict[str, str]** |  | [optional] 
**application_owner** | **str** |  | [optional] 
**application_type** | **str** |  | [optional] 
**configurations** | [**List[KubernetesConfiguration]**](KubernetesConfiguration.md) |  | [optional] 
**containers** | **List[object]** |  | [optional] 
**creation_date** | **str** |  | [optional] 
**custom_resource_metadata** | [**KubernetesCustomResourceMetadata**](KubernetesCustomResourceMetadata.md) |  | [optional] 
**deployment_type** | **str** |  | [optional] 
**horizontal_pod_autoscaler** | [**V2HorizontalPodAutoscaler**](V2HorizontalPodAutoscaler.md) |  | [optional] 
**id** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**load_balancer_ip_address** | **str** |  | [optional] 
**match_labels** | **Dict[str, str]** |  | [optional] 
**metadata** | [**KubernetesMetadata**](KubernetesMetadata.md) |  | [optional] 
**name** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**pods** | [**List[KubernetesPod]**](KubernetesPod.md) |  | [optional] 
**published_ports** | [**List[KubernetesPublishedPort]**](KubernetesPublishedPort.md) |  | [optional] 
**resource** | [**KubernetesK8sApplicationResource**](KubernetesK8sApplicationResource.md) |  | [optional] 
**resource_pool** | **str** |  | [optional] 
**running_pods_count** | **int** |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**service_type** | **str** |  | [optional] 
**services** | [**List[V1Service]**](V1Service.md) |  | [optional] 
**stack_id** | **str** |  | [optional] 
**stack_name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**total_pods_count** | **int** |  | [optional] 
**uid** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_application import KubernetesK8sApplication

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sApplication from a JSON string
kubernetes_k8s_application_instance = KubernetesK8sApplication.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sApplication.to_json())

# convert the object into a dict
kubernetes_k8s_application_dict = kubernetes_k8s_application_instance.to_dict()
# create an instance of KubernetesK8sApplication from a dict
kubernetes_k8s_application_from_dict = KubernetesK8sApplication.from_dict(kubernetes_k8s_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


