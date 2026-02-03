# KubernetesK8sDashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications_count** | **int** |  | [optional] 
**config_maps_count** | **int** |  | [optional] 
**ingresses_count** | **int** |  | [optional] 
**namespaces_count** | **int** |  | [optional] 
**secrets_count** | **int** |  | [optional] 
**services_count** | **int** |  | [optional] 
**volumes_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.kubernetes_k8s_dashboard import KubernetesK8sDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of KubernetesK8sDashboard from a JSON string
kubernetes_k8s_dashboard_instance = KubernetesK8sDashboard.from_json(json)
# print the JSON string representation of the object
print(KubernetesK8sDashboard.to_json())

# convert the object into a dict
kubernetes_k8s_dashboard_dict = kubernetes_k8s_dashboard_instance.to_dict()
# create an instance of KubernetesK8sDashboard from a dict
kubernetes_k8s_dashboard_from_dict = KubernetesK8sDashboard.from_dict(kubernetes_k8s_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


