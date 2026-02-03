# openapi_client.KubernetesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kubernetes_ingress**](KubernetesApi.md#create_kubernetes_ingress) | **POST** /kubernetes/{id}/namespaces/{namespace}/ingresses | Create an Ingress
[**create_kubernetes_namespace**](KubernetesApi.md#create_kubernetes_namespace) | **POST** /kubernetes/{id}/namespaces | Create a namespace
[**create_kubernetes_service**](KubernetesApi.md#create_kubernetes_service) | **POST** /kubernetes/{id}/namespaces/{namespace}/services | Create a service
[**delete_cluster_role_bindings**](KubernetesApi.md#delete_cluster_role_bindings) | **POST** /kubernetes/{id}/cluster_role_bindings/delete | Delete cluster role bindings
[**delete_cluster_roles**](KubernetesApi.md#delete_cluster_roles) | **POST** /kubernetes/{id}/cluster_roles/delete | Delete cluster roles
[**delete_cron_jobs**](KubernetesApi.md#delete_cron_jobs) | **POST** /kubernetes/{id}/cron_jobs/delete | Delete Cron Jobs
[**delete_jobs**](KubernetesApi.md#delete_jobs) | **POST** /kubernetes/{id}/jobs/delete | Delete Jobs
[**delete_kubernetes_ingresses**](KubernetesApi.md#delete_kubernetes_ingresses) | **POST** /kubernetes/{id}/ingresses/delete | Delete one or more Ingresses
[**delete_kubernetes_namespace**](KubernetesApi.md#delete_kubernetes_namespace) | **DELETE** /kubernetes/{id}/namespaces | Delete a kubernetes namespace
[**delete_kubernetes_services**](KubernetesApi.md#delete_kubernetes_services) | **POST** /kubernetes/{id}/services/delete | Delete services
[**delete_role_bindings**](KubernetesApi.md#delete_role_bindings) | **POST** /kubernetes/{id}/role_bindings/delete | Delete role bindings
[**delete_roles**](KubernetesApi.md#delete_roles) | **POST** /kubernetes/{id}/roles/delete | Delete roles
[**delete_service_accounts**](KubernetesApi.md#delete_service_accounts) | **POST** /kubernetes/{id}/service_accounts/delete | Delete service accounts
[**describe_resource**](KubernetesApi.md#describe_resource) | **GET** /kubernetes/{id}/describe | Get a description of a kubernetes resource
[**get_all_kubernetes_applications**](KubernetesApi.md#get_all_kubernetes_applications) | **GET** /kubernetes/{id}/applications | Get a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node.
[**get_all_kubernetes_applications_count**](KubernetesApi.md#get_all_kubernetes_applications_count) | **GET** /kubernetes/{id}/applications/count | Get Applications count
[**get_all_kubernetes_cluster_ingresses**](KubernetesApi.md#get_all_kubernetes_cluster_ingresses) | **GET** /kubernetes/{id}/ingresses | Get kubernetes ingresses at the cluster level
[**get_all_kubernetes_cluster_ingresses_count**](KubernetesApi.md#get_all_kubernetes_cluster_ingresses_count) | **GET** /kubernetes/{id}/ingresses/count | Get Ingresses count
[**get_all_kubernetes_cluster_role_bindings**](KubernetesApi.md#get_all_kubernetes_cluster_role_bindings) | **GET** /kubernetes/{id}/clusterrolebindings | Get a list of kubernetes cluster role bindings
[**get_all_kubernetes_cluster_roles**](KubernetesApi.md#get_all_kubernetes_cluster_roles) | **GET** /kubernetes/{id}/clusterroles | Get a list of kubernetes cluster roles
[**get_all_kubernetes_config_maps**](KubernetesApi.md#get_all_kubernetes_config_maps) | **GET** /kubernetes/{id}/configmaps | Get a list of ConfigMaps
[**get_all_kubernetes_config_maps_count**](KubernetesApi.md#get_all_kubernetes_config_maps_count) | **GET** /kubernetes/{id}/configmaps/count | Get ConfigMaps count
[**get_all_kubernetes_events**](KubernetesApi.md#get_all_kubernetes_events) | **GET** /kubernetes/{id}/events | Gets kubernetes events
[**get_all_kubernetes_ingress_controllers**](KubernetesApi.md#get_all_kubernetes_ingress_controllers) | **GET** /kubernetes/{id}/ingresscontrollers | Get a list of ingress controllers
[**get_all_kubernetes_ingresses**](KubernetesApi.md#get_all_kubernetes_ingresses) | **GET** /kubernetes/{id}/namespaces/{namespace}/ingresses | Get a list of Ingresses
[**get_all_kubernetes_services_count**](KubernetesApi.md#get_all_kubernetes_services_count) | **GET** /kubernetes/{id}/services/count | Get services count
[**get_all_kubernetes_volumes**](KubernetesApi.md#get_all_kubernetes_volumes) | **GET** /kubernetes/{id}/volumes | Get Kubernetes volumes within the given Portainer environment
[**get_all_kubernetes_volumes_count**](KubernetesApi.md#get_all_kubernetes_volumes_count) | **GET** /kubernetes/{id}/volumes/count | Get the total number of kubernetes volumes within the given Portainer environment.
[**get_applications_resources**](KubernetesApi.md#get_applications_resources) | **GET** /kubernetes/{id}/metrics/applications_resources | Get the total resource requests and limits of all applications
[**get_kubernetes_config**](KubernetesApi.md#get_kubernetes_config) | **GET** /kubernetes/config | Generate a kubeconfig file
[**get_kubernetes_config_map**](KubernetesApi.md#get_kubernetes_config_map) | **GET** /kubernetes/{id}/namespaces/{namespace}/configmaps/{configmap} | Get a ConfigMap
[**get_kubernetes_cron_jobs**](KubernetesApi.md#get_kubernetes_cron_jobs) | **GET** /kubernetes/{id}/cron_jobs | Get a list of kubernetes Cron Jobs
[**get_kubernetes_dashboard**](KubernetesApi.md#get_kubernetes_dashboard) | **GET** /kubernetes/{id}/dashboard | Get the dashboard summary data
[**get_kubernetes_events_for_namespace**](KubernetesApi.md#get_kubernetes_events_for_namespace) | **GET** /kubernetes/{id}/namespaces/{namespace}/events | Gets kubernetes events for namespace
[**get_kubernetes_ingress**](KubernetesApi.md#get_kubernetes_ingress) | **GET** /kubernetes/{id}/namespaces/{namespace}/ingresses/{ingress} | Get an Ingress by name
[**get_kubernetes_ingress_controllers_by_namespace**](KubernetesApi.md#get_kubernetes_ingress_controllers_by_namespace) | **GET** /kubernetes/{id}/namespaces/{namespace}/ingresscontrollers | Get a list ingress controllers by namespace
[**get_kubernetes_jobs**](KubernetesApi.md#get_kubernetes_jobs) | **GET** /kubernetes/{id}/jobs | Get a list of kubernetes Jobs
[**get_kubernetes_max_resource_limits**](KubernetesApi.md#get_kubernetes_max_resource_limits) | **GET** /kubernetes/{id}/max_resource_limits | Get max CPU and memory limits of all nodes within k8s cluster
[**get_kubernetes_metrics_for_all_nodes**](KubernetesApi.md#get_kubernetes_metrics_for_all_nodes) | **GET** /kubernetes/{id}/metrics/nodes | Get a list of nodes with their live metrics
[**get_kubernetes_metrics_for_all_pods**](KubernetesApi.md#get_kubernetes_metrics_for_all_pods) | **GET** /kubernetes/{id}/metrics/pods/{namespace} | Get a list of pods with their live metrics
[**get_kubernetes_metrics_for_node**](KubernetesApi.md#get_kubernetes_metrics_for_node) | **GET** /kubernetes/{id}/metrics/nodes/{name} | Get live metrics for a node
[**get_kubernetes_metrics_for_pod**](KubernetesApi.md#get_kubernetes_metrics_for_pod) | **GET** /kubernetes/{id}/metrics/pods/{namespace}/{name} | Get live metrics for a pod
[**get_kubernetes_namespace**](KubernetesApi.md#get_kubernetes_namespace) | **GET** /kubernetes/{id}/namespaces/{namespace} | Get namespace details
[**get_kubernetes_namespaces**](KubernetesApi.md#get_kubernetes_namespaces) | **GET** /kubernetes/{id}/namespaces | Get a list of namespaces
[**get_kubernetes_namespaces_count**](KubernetesApi.md#get_kubernetes_namespaces_count) | **GET** /kubernetes/{id}/namespaces/count | Get the total number of kubernetes namespaces within the given Portainer environment.
[**get_kubernetes_nodes_limits**](KubernetesApi.md#get_kubernetes_nodes_limits) | **GET** /kubernetes/{id}/nodes_limits | Get CPU and memory limits of all nodes within k8s cluster
[**get_kubernetes_rbac_status**](KubernetesApi.md#get_kubernetes_rbac_status) | **GET** /kubernetes/{id}/rbac_enabled | Check if RBAC is enabled
[**get_kubernetes_role_bindings**](KubernetesApi.md#get_kubernetes_role_bindings) | **GET** /kubernetes/{id}/rolebindings | Get a list of kubernetes role bindings
[**get_kubernetes_roles**](KubernetesApi.md#get_kubernetes_roles) | **GET** /kubernetes/{id}/roles | Get a list of kubernetes roles
[**get_kubernetes_secret**](KubernetesApi.md#get_kubernetes_secret) | **GET** /kubernetes/{id}/namespaces/{namespace}/secrets/{secret} | Get a Secret
[**get_kubernetes_secrets**](KubernetesApi.md#get_kubernetes_secrets) | **GET** /kubernetes/{id}/secrets | Get a list of Secrets
[**get_kubernetes_secrets_count**](KubernetesApi.md#get_kubernetes_secrets_count) | **GET** /kubernetes/{id}/secrets/count | Get Secrets count
[**get_kubernetes_service_accounts**](KubernetesApi.md#get_kubernetes_service_accounts) | **GET** /kubernetes/{id}/serviceaccounts | Get a list of kubernetes service accounts
[**get_kubernetes_services**](KubernetesApi.md#get_kubernetes_services) | **GET** /kubernetes/{id}/services | Get a list of services
[**get_kubernetes_services_by_namespace**](KubernetesApi.md#get_kubernetes_services_by_namespace) | **GET** /kubernetes/{id}/namespaces/{namespace}/services | Get a list of services for a given namespace
[**get_kubernetes_volume**](KubernetesApi.md#get_kubernetes_volume) | **GET** /kubernetes/{id}/volumes/{namespace}/{volume} | Get a Kubernetes volume within the given Portainer environment
[**get_kubernetes_volumes_in_namespace**](KubernetesApi.md#get_kubernetes_volumes_in_namespace) | **GET** /kubernetes/{id}/namespaces/{namespace}/volumes | Get Kubernetes volumes within a namespace in the given Portainer environment
[**kubernetes_namespaces_toggle_system**](KubernetesApi.md#kubernetes_namespaces_toggle_system) | **PUT** /kubernetes/{id}/namespaces/{namespace}/system | Toggle the system state for a namespace
[**update_kubernetes_ingress**](KubernetesApi.md#update_kubernetes_ingress) | **PUT** /kubernetes/{id}/namespaces/{namespace}/ingresses | Update an Ingress
[**update_kubernetes_ingress_controllers**](KubernetesApi.md#update_kubernetes_ingress_controllers) | **PUT** /kubernetes/{id}/ingresscontrollers | Update (block/unblock) ingress controllers
[**update_kubernetes_ingress_controllers_by_namespace**](KubernetesApi.md#update_kubernetes_ingress_controllers_by_namespace) | **PUT** /kubernetes/{id}/namespaces/{namespace}/ingresscontrollers | Update (block/unblock) ingress controllers by namespace
[**update_kubernetes_namespace**](KubernetesApi.md#update_kubernetes_namespace) | **PUT** /kubernetes/{id}/namespaces/{namespace} | Update a namespace
[**update_kubernetes_namespace_deprecated**](KubernetesApi.md#update_kubernetes_namespace_deprecated) | **PUT** /kubernetes/{id}/namespaces | Update a namespace
[**update_kubernetes_service**](KubernetesApi.md#update_kubernetes_service) | **PUT** /kubernetes/{id}/namespaces/{namespace}/services | Update a service


# **create_kubernetes_ingress**
> create_kubernetes_ingress(id, namespace, body)

Create an Ingress

Create an Ingress for the provided environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_info import KubernetesK8sIngressInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name
    body = openapi_client.KubernetesK8sIngressInfo() # KubernetesK8sIngressInfo | Ingress details

    try:
        # Create an Ingress
        api_instance.create_kubernetes_ingress(id, namespace, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->create_kubernetes_ingress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 
 **body** | [**KubernetesK8sIngressInfo**](KubernetesK8sIngressInfo.md)| Ingress details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**409** | Conflict - an ingress with the same name already exists in the specified namespace. |  -  |
**500** | Server error occurred while attempting to create an ingress. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kubernetes_namespace**
> PortainerK8sNamespaceInfo create_kubernetes_namespace(id, body)

Create a namespace

Create a namespace within the given environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_namespace_details import KubernetesK8sNamespaceDetails
from openapi_client.models.portainer_k8s_namespace_info import PortainerK8sNamespaceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    body = openapi_client.KubernetesK8sNamespaceDetails() # KubernetesK8sNamespaceDetails | Namespace configuration details

    try:
        # Create a namespace
        api_response = api_instance.create_kubernetes_namespace(id, body)
        print("The response of KubernetesApi->create_kubernetes_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->create_kubernetes_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **body** | [**KubernetesK8sNamespaceDetails**](KubernetesK8sNamespaceDetails.md)| Namespace configuration details | 

### Return type

[**PortainerK8sNamespaceInfo**](PortainerK8sNamespaceInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**409** | Conflict - the namespace already exists. |  -  |
**500** | Server error occurred while attempting to create the namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kubernetes_service**
> create_kubernetes_service(id, namespace, body)

Create a service

Create a service within a given namespace
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_service_info import KubernetesK8sServiceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name
    body = openapi_client.KubernetesK8sServiceInfo() # KubernetesK8sServiceInfo | Service definition

    try:
        # Create a service
        api_instance.create_kubernetes_service(id, namespace, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->create_kubernetes_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 
 **body** | [**KubernetesK8sServiceInfo**](KubernetesK8sServiceInfo.md)| Service definition | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to create a service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_role_bindings**
> delete_cluster_role_bindings(id, payload)

Delete cluster role bindings

Delete the provided list of cluster role bindings.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    payload = ['payload_example'] # List[str] | A list of cluster role bindings to delete

    try:
        # Delete cluster role bindings
        api_instance.delete_cluster_role_bindings(id, payload)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_cluster_role_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **payload** | [**List[str]**](str.md)| A list of cluster role bindings to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific cluster role binding. |  -  |
**500** | Server error occurred while attempting to delete cluster role bindings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_roles**
> delete_cluster_roles(id, payload)

Delete cluster roles

Delete the provided list of cluster roles.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    payload = ['payload_example'] # List[str] | A list of cluster roles to delete

    try:
        # Delete cluster roles
        api_instance.delete_cluster_roles(id, payload)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_cluster_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **payload** | [**List[str]**](str.md)| A list of cluster roles to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific cluster role. |  -  |
**500** | Server error occurred while attempting to delete cluster roles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cron_jobs**
> delete_cron_jobs(id, payload)

Delete Cron Jobs

Delete the provided list of Cron Jobs.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    payload = None # Dict[str, List[str]] | A map where the key is the namespace and the value is an array of Cron Jobs to delete

    try:
        # Delete Cron Jobs
        api_instance.delete_cron_jobs(id, payload)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_cron_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **payload** | [**Dict[str, List[str]]**](List.md)| A map where the key is the namespace and the value is an array of Cron Jobs to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific service account. |  -  |
**500** | Server error occurred while attempting to delete Cron Jobs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jobs**
> delete_jobs(id, payload)

Delete Jobs

Delete the provided list of Jobs.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    payload = None # Dict[str, List[str]] | A map where the key is the namespace and the value is an array of Jobs to delete

    try:
        # Delete Jobs
        api_instance.delete_jobs(id, payload)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **payload** | [**Dict[str, List[str]]**](List.md)| A map where the key is the namespace and the value is an array of Jobs to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific service account. |  -  |
**500** | Server error occurred while attempting to delete Jobs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kubernetes_ingresses**
> delete_kubernetes_ingresses(id, body)

Delete one or more Ingresses

Delete one or more Ingresses in the provided environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    body = None # Dict[str, List[str]] | Ingress details

    try:
        # Delete one or more Ingresses
        api_instance.delete_kubernetes_ingresses(id, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_ingresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **body** | [**Dict[str, List[str]]**](List.md)| Ingress details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific ingress. |  -  |
**500** | Server error occurred while attempting to delete specified ingresses. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kubernetes_namespace**
> str delete_kubernetes_namespace(id)

Delete a kubernetes namespace

Delete a kubernetes namespace within the given environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Delete a kubernetes namespace
        api_response = api_instance.delete_kubernetes_namespace(id)
        print("The response of KubernetesApi->delete_kubernetes_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**str**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**403** | Unauthorized access or operation not allowed. |  -  |
**500** | Server error occurred while attempting to delete the namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kubernetes_services**
> delete_kubernetes_services(id, body)

Delete services

Delete the provided list of services.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    body = None # Dict[str, List[str]] | A map where the key is the namespace and the value is an array of services to delete

    try:
        # Delete services
        api_instance.delete_kubernetes_services(id, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_kubernetes_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **body** | [**Dict[str, List[str]]**](List.md)| A map where the key is the namespace and the value is an array of services to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific service. |  -  |
**500** | Server error occurred while attempting to delete services. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_bindings**
> delete_role_bindings(id, payload)

Delete role bindings

Delete the provided list of role bindings.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    payload = None # Dict[str, List[str]] | A map where the key is the namespace and the value is an array of role bindings to delete

    try:
        # Delete role bindings
        api_instance.delete_role_bindings(id, payload)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_role_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **payload** | [**Dict[str, List[str]]**](List.md)| A map where the key is the namespace and the value is an array of role bindings to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific role binding. |  -  |
**500** | Server error occurred while attempting to delete role bindings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_roles**
> delete_roles(id, payload)

Delete roles

Delete the provided list of roles.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    payload = None # Dict[str, List[str]] | A map where the key is the namespace and the value is an array of roles to delete

    try:
        # Delete roles
        api_instance.delete_roles(id, payload)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **payload** | [**Dict[str, List[str]]**](List.md)| A map where the key is the namespace and the value is an array of roles to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific role. |  -  |
**500** | Server error occurred while attempting to delete roles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_accounts**
> delete_service_accounts(id, payload)

Delete service accounts

Delete the provided list of service accounts.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    payload = None # Dict[str, List[str]] | A map where the key is the namespace and the value is an array of service accounts to delete

    try:
        # Delete service accounts
        api_instance.delete_service_accounts(id, payload)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_service_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **payload** | [**Dict[str, List[str]]**](List.md)| A map where the key is the namespace and the value is an array of service accounts to delete | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific service account. |  -  |
**500** | Server error occurred while attempting to delete service accounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **describe_resource**
> KubernetesDescribeResourceResponse describe_resource(id, name, kind, namespace=namespace)

Get a description of a kubernetes resource

Get a description of a kubernetes resource.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_describe_resource_response import KubernetesDescribeResourceResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    name = 'name_example' # str | Resource name
    kind = 'kind_example' # str | Resource kind
    namespace = 'namespace_example' # str | Namespace (optional)

    try:
        # Get a description of a kubernetes resource
        api_response = api_instance.describe_resource(id, name, kind, namespace=namespace)
        print("The response of KubernetesApi->describe_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->describe_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **name** | **str**| Resource name | 
 **kind** | **str**| Resource kind | 
 **namespace** | **str**| Namespace | [optional] 

### Return type

[**KubernetesDescribeResourceResponse**](KubernetesDescribeResourceResponse.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve resource description |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_applications**
> List[KubernetesK8sApplication] get_all_kubernetes_applications(id, namespace, node_name)

Get a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node.

Get a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_application import KubernetesK8sApplication
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    namespace = 'namespace_example' # str | Namespace name
    node_name = 'node_name_example' # str | Node name

    try:
        # Get a list of applications across all namespaces in the cluster. If the nodeName is provided, it will return the applications running on that node.
        api_response = api_instance.get_all_kubernetes_applications(id, namespace, node_name)
        print("The response of KubernetesApi->get_all_kubernetes_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **namespace** | **str**| Namespace name | 
 **node_name** | **str**| Node name | 

### Return type

[**List[KubernetesK8sApplication]**](KubernetesK8sApplication.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of applications from the cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_applications_count**
> int get_all_kubernetes_applications_count(id)

Get Applications count

Get the count of Applications across all namespaces in the cluster. If the nodeName is provided, it will return the count of applications running on that node.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get Applications count
        api_response = api_instance.get_all_kubernetes_applications_count(id)
        print("The response of KubernetesApi->get_all_kubernetes_applications_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_applications_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**int**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the count of all applications from the cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_cluster_ingresses**
> List[KubernetesK8sIngressInfo] get_all_kubernetes_cluster_ingresses(id, with_services=with_services)

Get kubernetes ingresses at the cluster level

Get kubernetes ingresses at the cluster level for the provided environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_info import KubernetesK8sIngressInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    with_services = True # bool | Lookup services associated with each ingress (optional)

    try:
        # Get kubernetes ingresses at the cluster level
        api_response = api_instance.get_all_kubernetes_cluster_ingresses(id, with_services=with_services)
        print("The response of KubernetesApi->get_all_kubernetes_cluster_ingresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_cluster_ingresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **with_services** | **bool**| Lookup services associated with each ingress | [optional] 

### Return type

[**List[KubernetesK8sIngressInfo]**](KubernetesK8sIngressInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve ingresses. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_cluster_ingresses_count**
> int get_all_kubernetes_cluster_ingresses_count(id)

Get Ingresses count

Get the number of kubernetes ingresses within the given environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get Ingresses count
        api_response = api_instance.get_all_kubernetes_cluster_ingresses_count(id)
        print("The response of KubernetesApi->get_all_kubernetes_cluster_ingresses_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_cluster_ingresses_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**int**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve ingresses count. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_cluster_role_bindings**
> List[KubernetesK8sClusterRoleBinding] get_all_kubernetes_cluster_role_bindings(id)

Get a list of kubernetes cluster role bindings

Get a list of kubernetes cluster role bindings within the given environment at the cluster level.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_cluster_role_binding import KubernetesK8sClusterRoleBinding
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get a list of kubernetes cluster role bindings
        api_response = api_instance.get_all_kubernetes_cluster_role_bindings(id)
        print("The response of KubernetesApi->get_all_kubernetes_cluster_role_bindings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_cluster_role_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

[**List[KubernetesK8sClusterRoleBinding]**](KubernetesK8sClusterRoleBinding.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of cluster role bindings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_cluster_roles**
> List[KubernetesK8sClusterRole] get_all_kubernetes_cluster_roles(id)

Get a list of kubernetes cluster roles

Get a list of kubernetes cluster roles within the given environment at the cluster level.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_cluster_role import KubernetesK8sClusterRole
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get a list of kubernetes cluster roles
        api_response = api_instance.get_all_kubernetes_cluster_roles(id)
        print("The response of KubernetesApi->get_all_kubernetes_cluster_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_cluster_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

[**List[KubernetesK8sClusterRole]**](KubernetesK8sClusterRole.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of cluster roles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_config_maps**
> List[KubernetesK8sConfigMap] get_all_kubernetes_config_maps(id, is_used)

Get a list of ConfigMaps

Get a list of ConfigMaps across all namespaces in the cluster. For non-admin users, it will only return ConfigMaps based on the namespaces that they have access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_config_map import KubernetesK8sConfigMap
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    is_used = True # bool | Set to true to include information about applications that use the ConfigMaps in the response

    try:
        # Get a list of ConfigMaps
        api_response = api_instance.get_all_kubernetes_config_maps(id, is_used)
        print("The response of KubernetesApi->get_all_kubernetes_config_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_config_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **is_used** | **bool**| Set to true to include information about applications that use the ConfigMaps in the response | 

### Return type

[**List[KubernetesK8sConfigMap]**](KubernetesK8sConfigMap.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve all configmaps from the cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_config_maps_count**
> int get_all_kubernetes_config_maps_count(id)

Get ConfigMaps count

Get the count of ConfigMaps across all namespaces in the cluster. For non-admin users, it will only return the count of ConfigMaps based on the namespaces that they have access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get ConfigMaps count
        api_response = api_instance.get_all_kubernetes_config_maps_count(id)
        print("The response of KubernetesApi->get_all_kubernetes_config_maps_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_config_maps_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**int**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the count of all configmaps from the cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_events**
> List[KubernetesK8sEvent] get_all_kubernetes_events(id, resource_id=resource_id)

Gets kubernetes events

Get events by query param resourceId
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_event import KubernetesK8sEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    resource_id = 'resource_id_example' # str | The resource id of the involved kubernetes object (optional)

    try:
        # Gets kubernetes events
        api_response = api_instance.get_all_kubernetes_events(id, resource_id=resource_id)
        print("The response of KubernetesApi->get_all_kubernetes_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **resource_id** | **str**| The resource id of the involved kubernetes object | [optional] 

### Return type

[**List[KubernetesK8sEvent]**](KubernetesK8sEvent.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**500** | Server error occurred while attempting to retrieve the events. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_ingress_controllers**
> List[KubernetesK8sIngressController] get_all_kubernetes_ingress_controllers(id, allowed_only=allowed_only)

Get a list of ingress controllers

Get a list of ingress controllers for the given environment. If the allowedOnly query parameter is set, only ingress controllers that are allowed by the environment's ingress configuration will be returned.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_controller import KubernetesK8sIngressController
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    allowed_only = True # bool | Only return allowed ingress controllers (optional)

    try:
        # Get a list of ingress controllers
        api_response = api_instance.get_all_kubernetes_ingress_controllers(id, allowed_only=allowed_only)
        print("The response of KubernetesApi->get_all_kubernetes_ingress_controllers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_ingress_controllers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **allowed_only** | **bool**| Only return allowed ingress controllers | [optional] 

### Return type

[**List[KubernetesK8sIngressController]**](KubernetesK8sIngressController.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve ingress controllers |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_ingresses**
> List[KubernetesK8sIngressInfo] get_all_kubernetes_ingresses(id, namespace)

Get a list of Ingresses

Get a list of Ingresses. If namespace is provided, it will return the list of Ingresses in that namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_info import KubernetesK8sIngressInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name

    try:
        # Get a list of Ingresses
        api_response = api_instance.get_all_kubernetes_ingresses(id, namespace)
        print("The response of KubernetesApi->get_all_kubernetes_ingresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_ingresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 

### Return type

[**List[KubernetesK8sIngressInfo]**](KubernetesK8sIngressInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve ingresses |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_services_count**
> int get_all_kubernetes_services_count(id)

Get services count

Get the count of services that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get services count
        api_response = api_instance.get_all_kubernetes_services_count(id)
        print("The response of KubernetesApi->get_all_kubernetes_services_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_services_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**int**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the total count of all services. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_volumes**
> Dict[str, KubernetesK8sVolumeInfo] get_all_kubernetes_volumes(id, with_applications=with_applications)

Get Kubernetes volumes within the given Portainer environment

Get a list of all kubernetes volumes within the given environment (Endpoint). The Endpoint ID must be a valid Portainer environment identifier.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_volume_info import KubernetesK8sVolumeInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    with_applications = True # bool | When set to True, include the applications that are using the volumes. It is set to false by default (optional)

    try:
        # Get Kubernetes volumes within the given Portainer environment
        api_response = api_instance.get_all_kubernetes_volumes(id, with_applications=with_applications)
        print("The response of KubernetesApi->get_all_kubernetes_volumes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_volumes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **with_applications** | **bool**| When set to True, include the applications that are using the volumes. It is set to false by default | [optional] 

### Return type

[**Dict[str, KubernetesK8sVolumeInfo]**](KubernetesK8sVolumeInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**403** | Unauthorized access or operation not allowed. |  -  |
**500** | Server error occurred while attempting to retrieve kubernetes volumes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kubernetes_volumes_count**
> int get_all_kubernetes_volumes_count(id)

Get the total number of kubernetes volumes within the given Portainer environment.

Get the total number of kubernetes volumes within the given environment (Endpoint). The total count depends on the user's role and permissions. The Endpoint ID must be a valid Portainer environment identifier.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get the total number of kubernetes volumes within the given Portainer environment.
        api_response = api_instance.get_all_kubernetes_volumes_count(id)
        print("The response of KubernetesApi->get_all_kubernetes_volumes_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_all_kubernetes_volumes_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**int**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**403** | Unauthorized access or operation not allowed. |  -  |
**500** | Server error occurred while attempting to retrieve kubernetes volumes count. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications_resources**
> KubernetesK8sApplicationResource get_applications_resources(id, node)

Get the total resource requests and limits of all applications

Get the total CPU (cores) and memory (bytes) requests and limits of all applications across all namespaces.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_application_resource import KubernetesK8sApplicationResource
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    node = 'node_example' # str | Node name

    try:
        # Get the total resource requests and limits of all applications
        api_response = api_instance.get_applications_resources(id, node)
        print("The response of KubernetesApi->get_applications_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_applications_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **node** | **str**| Node name | 

### Return type

[**KubernetesK8sApplicationResource**](KubernetesK8sApplicationResource.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the total resource requests and limits for all applications from the cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_config**
> object get_kubernetes_config(ids=ids, exclude_ids=exclude_ids)

Generate a kubeconfig file

Generate a kubeconfig file that allows a client to communicate with the Kubernetes API server
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    ids = [56] # List[int] | will include only these environments(endpoints) (optional)
    exclude_ids = [56] # List[int] | will exclude these environments(endpoints) (optional)

    try:
        # Generate a kubeconfig file
        api_response = api_instance.get_kubernetes_config(ids=ids, exclude_ids=exclude_ids)
        print("The response of KubernetesApi->get_kubernetes_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_config: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[int]**](int.md)| will include only these environments(endpoints) | [optional] 
 **exclude_ids** | [**List[int]**](int.md)| will exclude these environments(endpoints) | [optional] 

### Return type

**object**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json,  application/yaml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to generate the kubeconfig file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_config_map**
> KubernetesK8sConfigMap get_kubernetes_config_map(id, namespace, configmap)

Get a ConfigMap

Get a ConfigMap by name for a given namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_config_map import KubernetesK8sConfigMap
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | The namespace name where the configmap is located
    configmap = 'configmap_example' # str | The configmap name to get details for

    try:
        # Get a ConfigMap
        api_response = api_instance.get_kubernetes_config_map(id, namespace, configmap)
        print("The response of KubernetesApi->get_kubernetes_config_map:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_config_map: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| The namespace name where the configmap is located | 
 **configmap** | **str**| The configmap name to get details for | 

### Return type

[**KubernetesK8sConfigMap**](KubernetesK8sConfigMap.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or a configmap with the specified name in the given namespace. |  -  |
**500** | Server error occurred while attempting to retrieve a configmap by name within the specified namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_cron_jobs**
> List[KubernetesK8sCronJob] get_kubernetes_cron_jobs(id)

Get a list of kubernetes Cron Jobs

Get a list of kubernetes Cron Jobs that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_cron_job import KubernetesK8sCronJob
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get a list of kubernetes Cron Jobs
        api_response = api_instance.get_kubernetes_cron_jobs(id)
        print("The response of KubernetesApi->get_kubernetes_cron_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_cron_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

[**List[KubernetesK8sCronJob]**](KubernetesK8sCronJob.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of Cron Jobs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_dashboard**
> List[KubernetesK8sDashboard] get_kubernetes_dashboard(id)

Get the dashboard summary data

Get the dashboard summary data which is simply a count of a range of different commonly used kubernetes resources.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_dashboard import KubernetesK8sDashboard
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment (Endpoint) identifier

    try:
        # Get the dashboard summary data
        api_response = api_instance.get_kubernetes_dashboard(id)
        print("The response of KubernetesApi->get_kubernetes_dashboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_dashboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment (Endpoint) identifier | 

### Return type

[**List[KubernetesK8sDashboard]**](KubernetesK8sDashboard.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_events_for_namespace**
> List[KubernetesK8sEvent] get_kubernetes_events_for_namespace(id, namespace, resource_id=resource_id)

Gets kubernetes events for namespace

Get events by optional query param resourceId for a given namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_event import KubernetesK8sEvent
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | The namespace name the events are associated to
    resource_id = 'resource_id_example' # str | The resource id of the involved kubernetes object (optional)

    try:
        # Gets kubernetes events for namespace
        api_response = api_instance.get_kubernetes_events_for_namespace(id, namespace, resource_id=resource_id)
        print("The response of KubernetesApi->get_kubernetes_events_for_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_events_for_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| The namespace name the events are associated to | 
 **resource_id** | **str**| The resource id of the involved kubernetes object | [optional] 

### Return type

[**List[KubernetesK8sEvent]**](KubernetesK8sEvent.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**500** | Server error occurred while attempting to retrieve the events within the specified namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_ingress**
> KubernetesK8sIngressInfo get_kubernetes_ingress(id, namespace, ingress)

Get an Ingress by name

Get an Ingress by name for the provided environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_info import KubernetesK8sIngressInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name
    ingress = 'ingress_example' # str | Ingress name

    try:
        # Get an Ingress by name
        api_response = api_instance.get_kubernetes_ingress(id, namespace, ingress)
        print("The response of KubernetesApi->get_kubernetes_ingress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_ingress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 
 **ingress** | **str**| Ingress name | 

### Return type

[**KubernetesK8sIngressInfo**](KubernetesK8sIngressInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find an ingress with the specified name. |  -  |
**500** | Server error occurred while attempting to retrieve an ingress. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_ingress_controllers_by_namespace**
> List[KubernetesK8sIngressController] get_kubernetes_ingress_controllers_by_namespace(id, namespace)

Get a list ingress controllers by namespace

Get a list of ingress controllers for the given environment in the provided namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_controller import KubernetesK8sIngressController
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace

    try:
        # Get a list ingress controllers by namespace
        api_response = api_instance.get_kubernetes_ingress_controllers_by_namespace(id, namespace)
        print("The response of KubernetesApi->get_kubernetes_ingress_controllers_by_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_ingress_controllers_by_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace | 

### Return type

[**List[KubernetesK8sIngressController]**](KubernetesK8sIngressController.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or a namespace with the specified name. |  -  |
**500** | Server error occurred while attempting to retrieve ingress controllers by a namespace |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_jobs**
> List[KubernetesK8sJob] get_kubernetes_jobs(id, include_cron_job_children=include_cron_job_children)

Get a list of kubernetes Jobs

Get a list of kubernetes Jobs that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_job import KubernetesK8sJob
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    include_cron_job_children = True # bool | Whether to include Jobs that have a cronjob owner (optional)

    try:
        # Get a list of kubernetes Jobs
        api_response = api_instance.get_kubernetes_jobs(id, include_cron_job_children=include_cron_job_children)
        print("The response of KubernetesApi->get_kubernetes_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_jobs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **include_cron_job_children** | **bool**| Whether to include Jobs that have a cronjob owner | [optional] 

### Return type

[**List[KubernetesK8sJob]**](KubernetesK8sJob.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of Jobs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_max_resource_limits**
> Dict[str, PortainerK8sNodeLimits] get_kubernetes_max_resource_limits(id)

Get max CPU and memory limits of all nodes within k8s cluster

Get max CPU and memory limits (unused resources) of all nodes within k8s cluster.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_k8s_node_limits import PortainerK8sNodeLimits
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # Get max CPU and memory limits of all nodes within k8s cluster
        api_response = api_instance.get_kubernetes_max_resource_limits(id)
        print("The response of KubernetesApi->get_kubernetes_max_resource_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_max_resource_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

[**Dict[str, PortainerK8sNodeLimits]**](PortainerK8sNodeLimits.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve nodes limits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_metrics_for_all_nodes**
> V1beta1NodeMetricsList get_kubernetes_metrics_for_all_nodes(id)

Get a list of nodes with their live metrics

Get a list of metrics associated with all nodes of a cluster.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.v1beta1_node_metrics_list import V1beta1NodeMetricsList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get a list of nodes with their live metrics
        api_response = api_instance.get_kubernetes_metrics_for_all_nodes(id)
        print("The response of KubernetesApi->get_kubernetes_metrics_for_all_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_metrics_for_all_nodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

[**V1beta1NodeMetricsList**](V1beta1NodeMetricsList.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**500** | Server error occurred while attempting to retrieve the list of nodes with their live metrics. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_metrics_for_all_pods**
> V1beta1PodMetricsList get_kubernetes_metrics_for_all_pods(id, namespace)

Get a list of pods with their live metrics

Get a list of pods with their live metrics for the specified namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.v1beta1_pod_metrics_list import V1beta1PodMetricsList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace

    try:
        # Get a list of pods with their live metrics
        api_response = api_instance.get_kubernetes_metrics_for_all_pods(id, namespace)
        print("The response of KubernetesApi->get_kubernetes_metrics_for_all_pods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_metrics_for_all_pods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace | 

### Return type

[**V1beta1PodMetricsList**](V1beta1PodMetricsList.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**500** | Server error occurred while attempting to retrieve the list of pods with their live metrics. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_metrics_for_node**
> V1beta1NodeMetrics get_kubernetes_metrics_for_node(id, name)

Get live metrics for a node

Get live metrics for the specified node.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.v1beta1_node_metrics import V1beta1NodeMetrics
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    name = 'name_example' # str | Node identifier

    try:
        # Get live metrics for a node
        api_response = api_instance.get_kubernetes_metrics_for_node(id, name)
        print("The response of KubernetesApi->get_kubernetes_metrics_for_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_metrics_for_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **name** | **str**| Node identifier | 

### Return type

[**V1beta1NodeMetrics**](V1beta1NodeMetrics.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**500** | Server error occurred while attempting to retrieve the live metrics for the specified node. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_metrics_for_pod**
> V1beta1PodMetrics get_kubernetes_metrics_for_pod(id, namespace, name)

Get live metrics for a pod

Get live metrics for the specified pod.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.v1beta1_pod_metrics import V1beta1PodMetrics
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace
    name = 'name_example' # str | Pod identifier

    try:
        # Get live metrics for a pod
        api_response = api_instance.get_kubernetes_metrics_for_pod(id, namespace, name)
        print("The response of KubernetesApi->get_kubernetes_metrics_for_pod:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_metrics_for_pod: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace | 
 **name** | **str**| Pod identifier | 

### Return type

[**V1beta1PodMetrics**](V1beta1PodMetrics.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**500** | Server error occurred while attempting to retrieve the live metrics for the specified pod. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_namespace**
> PortainerK8sNamespaceInfo get_kubernetes_namespace(id, namespace, with_resource_quota)

Get namespace details

Get namespace details for the provided namespace within the given environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_k8s_namespace_info import PortainerK8sNamespaceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | The namespace name to get details for
    with_resource_quota = True # bool | When set to true, include the resource quota information as part of the Namespace information. Default is false

    try:
        # Get namespace details
        api_response = api_instance.get_kubernetes_namespace(id, namespace, with_resource_quota)
        print("The response of KubernetesApi->get_kubernetes_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| The namespace name to get details for | 
 **with_resource_quota** | **bool**| When set to true, include the resource quota information as part of the Namespace information. Default is false | 

### Return type

[**PortainerK8sNamespaceInfo**](PortainerK8sNamespaceInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific namespace. |  -  |
**500** | Server error occurred while attempting to retrieve specified namespace information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_namespaces**
> List[PortainerK8sNamespaceInfo] get_kubernetes_namespaces(id, with_resource_quota, with_unhealthy_events)

Get a list of namespaces

Get a list of all namespaces within the given environment based on the user role and permissions. If the user is an admin, they can access all namespaces. If the user is not an admin, they can only access namespaces that they have access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_k8s_namespace_info import PortainerK8sNamespaceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    with_resource_quota = True # bool | When set to true, include the resource quota information as part of the Namespace information. Default is false
    with_unhealthy_events = True # bool | When set to true, include the unhealthy events information as part of the Namespace information. Default is false

    try:
        # Get a list of namespaces
        api_response = api_instance.get_kubernetes_namespaces(id, with_resource_quota, with_unhealthy_events)
        print("The response of KubernetesApi->get_kubernetes_namespaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_namespaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **with_resource_quota** | **bool**| When set to true, include the resource quota information as part of the Namespace information. Default is false | 
 **with_unhealthy_events** | **bool**| When set to true, include the unhealthy events information as part of the Namespace information. Default is false | 

### Return type

[**List[PortainerK8sNamespaceInfo]**](PortainerK8sNamespaceInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of namespaces. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_namespaces_count**
> int get_kubernetes_namespaces_count(id)

Get the total number of kubernetes namespaces within the given Portainer environment.

Get the total number of kubernetes namespaces within the given environment, including the system namespaces. The total count depends on the user's role and permissions.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get the total number of kubernetes namespaces within the given Portainer environment.
        api_response = api_instance.get_kubernetes_namespaces_count(id)
        print("The response of KubernetesApi->get_kubernetes_namespaces_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_namespaces_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**int**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to compute the namespace count. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_nodes_limits**
> Dict[str, PortainerK8sNodeLimits] get_kubernetes_nodes_limits(id)

Get CPU and memory limits of all nodes within k8s cluster

Get CPU and memory limits of all nodes within k8s cluster.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_k8s_node_limits import PortainerK8sNodeLimits
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # Get CPU and memory limits of all nodes within k8s cluster
        api_response = api_instance.get_kubernetes_nodes_limits(id)
        print("The response of KubernetesApi->get_kubernetes_nodes_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_nodes_limits: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

[**Dict[str, PortainerK8sNodeLimits]**](PortainerK8sNodeLimits.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve nodes limits. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_rbac_status**
> bool get_kubernetes_rbac_status(id)

Check if RBAC is enabled

Check if RBAC is enabled in the specified Kubernetes cluster.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # Check if RBAC is enabled
        api_response = api_instance.get_kubernetes_rbac_status(id)
        print("The response of KubernetesApi->get_kubernetes_rbac_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_rbac_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

**bool**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RBAC status |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the RBAC status. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_role_bindings**
> List[KubernetesK8sRoleBinding] get_kubernetes_role_bindings(id)

Get a list of kubernetes role bindings

Get a list of kubernetes role bindings that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_role_binding import KubernetesK8sRoleBinding
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get a list of kubernetes role bindings
        api_response = api_instance.get_kubernetes_role_bindings(id)
        print("The response of KubernetesApi->get_kubernetes_role_bindings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_role_bindings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

[**List[KubernetesK8sRoleBinding]**](KubernetesK8sRoleBinding.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of role bindings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_roles**
> List[KubernetesK8sRole] get_kubernetes_roles(id)

Get a list of kubernetes roles

Get a list of kubernetes roles that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_role import KubernetesK8sRole
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get a list of kubernetes roles
        api_response = api_instance.get_kubernetes_roles(id)
        print("The response of KubernetesApi->get_kubernetes_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

[**List[KubernetesK8sRole]**](KubernetesK8sRole.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of roles. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_secret**
> KubernetesK8sSecret get_kubernetes_secret(id, namespace, secret)

Get a Secret

Get a Secret by name for a given namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_secret import KubernetesK8sSecret
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | The namespace name where the secret is located
    secret = 'secret_example' # str | The secret name to get details for

    try:
        # Get a Secret
        api_response = api_instance.get_kubernetes_secret(id, namespace, secret)
        print("The response of KubernetesApi->get_kubernetes_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| The namespace name where the secret is located | 
 **secret** | **str**| The secret name to get details for | 

### Return type

[**KubernetesK8sSecret**](KubernetesK8sSecret.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve a secret by name belong in a namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_secrets**
> List[KubernetesK8sSecret] get_kubernetes_secrets(id, is_used)

Get a list of Secrets

Get a list of Secrets for a given namespace. If isUsed is set to true, information about the applications that use the secrets is also returned.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_secret import KubernetesK8sSecret
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    is_used = True # bool | When set to true, associate the Secrets with the applications that use them

    try:
        # Get a list of Secrets
        api_response = api_instance.get_kubernetes_secrets(id, is_used)
        print("The response of KubernetesApi->get_kubernetes_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_secrets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **is_used** | **bool**| When set to true, associate the Secrets with the applications that use them | 

### Return type

[**List[KubernetesK8sSecret]**](KubernetesK8sSecret.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve all secrets from the cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_secrets_count**
> int get_kubernetes_secrets_count(id)

Get Secrets count

Get the count of Secrets across all namespaces that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get Secrets count
        api_response = api_instance.get_kubernetes_secrets_count(id)
        print("The response of KubernetesApi->get_kubernetes_secrets_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_secrets_count: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

**int**

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the count of all secrets from the cluster. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_service_accounts**
> List[KubernetesK8sServiceAccount] get_kubernetes_service_accounts(id)

Get a list of kubernetes service accounts

Get a list of kubernetes service accounts that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_service_account import KubernetesK8sServiceAccount
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier

    try:
        # Get a list of kubernetes service accounts
        api_response = api_instance.get_kubernetes_service_accounts(id)
        print("The response of KubernetesApi->get_kubernetes_service_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_service_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 

### Return type

[**List[KubernetesK8sServiceAccount]**](KubernetesK8sServiceAccount.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve the list of service accounts. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_services**
> List[KubernetesK8sServiceInfo] get_kubernetes_services(id, with_applications=with_applications)

Get a list of services

Get a list of services that the user has access to.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_service_info import KubernetesK8sServiceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    with_applications = True # bool | Lookup applications associated with each service (optional)

    try:
        # Get a list of services
        api_response = api_instance.get_kubernetes_services(id, with_applications=with_applications)
        print("The response of KubernetesApi->get_kubernetes_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **with_applications** | **bool**| Lookup applications associated with each service | [optional] 

### Return type

[**List[KubernetesK8sServiceInfo]**](KubernetesK8sServiceInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve all services. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_services_by_namespace**
> List[KubernetesK8sServiceInfo] get_kubernetes_services_by_namespace(id, namespace)

Get a list of services for a given namespace

Get a list of services for a given namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_service_info import KubernetesK8sServiceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name

    try:
        # Get a list of services for a given namespace
        api_response = api_instance.get_kubernetes_services_by_namespace(id, namespace)
        print("The response of KubernetesApi->get_kubernetes_services_by_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_services_by_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 

### Return type

[**List[KubernetesK8sServiceInfo]**](KubernetesK8sServiceInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to retrieve all services for a namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_volume**
> KubernetesK8sVolumeInfo get_kubernetes_volume(id, namespace, volume)

Get a Kubernetes volume within the given Portainer environment

Get a Kubernetes volume within the given environment (Endpoint). The Endpoint ID must be a valid Portainer environment identifier.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_volume_info import KubernetesK8sVolumeInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace identifier
    volume = 'volume_example' # str | Volume name

    try:
        # Get a Kubernetes volume within the given Portainer environment
        api_response = api_instance.get_kubernetes_volume(id, namespace, volume)
        print("The response of KubernetesApi->get_kubernetes_volume:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_volume: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace identifier | 
 **volume** | **str**| Volume name | 

### Return type

[**KubernetesK8sVolumeInfo**](KubernetesK8sVolumeInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_volumes_in_namespace**
> Dict[str, KubernetesK8sVolumeInfo] get_kubernetes_volumes_in_namespace(id, namespace, with_applications=with_applications)

Get Kubernetes volumes within a namespace in the given Portainer environment

Get a list of kubernetes volumes within the specified namespace in the given environment (Endpoint). The Endpoint ID must be a valid Portainer environment identifier.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_volume_info import KubernetesK8sVolumeInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace identifier
    with_applications = True # bool | When set to True, include the applications that are using the volumes. It is set to false by default (optional)

    try:
        # Get Kubernetes volumes within a namespace in the given Portainer environment
        api_response = api_instance.get_kubernetes_volumes_in_namespace(id, namespace, with_applications=with_applications)
        print("The response of KubernetesApi->get_kubernetes_volumes_in_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_volumes_in_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace identifier | 
 **with_applications** | **bool**| When set to True, include the applications that are using the volumes. It is set to false by default | [optional] 

### Return type

[**Dict[str, KubernetesK8sVolumeInfo]**](KubernetesK8sVolumeInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**403** | Unauthorized access or operation not allowed. |  -  |
**500** | Server error occurred while attempting to retrieve kubernetes volumes in the namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kubernetes_namespaces_toggle_system**
> kubernetes_namespaces_toggle_system(id, namespace, body)

Toggle the system state for a namespace

Toggle the system state for a namespace
**Access policy**: Administrator or environment administrator.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_namespaces_toggle_system_payload import KubernetesNamespacesToggleSystemPayload
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name
    body = openapi_client.KubernetesNamespacesToggleSystemPayload() # KubernetesNamespacesToggleSystemPayload | Update details

    try:
        # Toggle the system state for a namespace
        api_instance.kubernetes_namespaces_toggle_system(id, namespace, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->kubernetes_namespaces_toggle_system: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 
 **body** | [**KubernetesNamespacesToggleSystemPayload**](KubernetesNamespacesToggleSystemPayload.md)| Update details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find the namespace to update. |  -  |
**500** | Server error occurred while attempting to update the system state of the namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_ingress**
> update_kubernetes_ingress(id, namespace, body)

Update an Ingress

Update an Ingress for the provided environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_info import KubernetesK8sIngressInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name
    body = openapi_client.KubernetesK8sIngressInfo() # KubernetesK8sIngressInfo | Ingress details

    try:
        # Update an Ingress
        api_instance.update_kubernetes_ingress(id, namespace, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->update_kubernetes_ingress: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 
 **body** | [**KubernetesK8sIngressInfo**](KubernetesK8sIngressInfo.md)| Ingress details | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find the specified ingress. |  -  |
**500** | Server error occurred while attempting to update the specified ingress. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_ingress_controllers**
> update_kubernetes_ingress_controllers(id, body)

Update (block/unblock) ingress controllers

Update (block/unblock) ingress controllers for the provided environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_controller import KubernetesK8sIngressController
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    body = [openapi_client.KubernetesK8sIngressController()] # List[KubernetesK8sIngressController] | Ingress controllers

    try:
        # Update (block/unblock) ingress controllers
        api_instance.update_kubernetes_ingress_controllers(id, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->update_kubernetes_ingress_controllers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **body** | [**List[KubernetesK8sIngressController]**](KubernetesK8sIngressController.md)| Ingress controllers | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find the ingress controllers to update. |  -  |
**500** | Server error occurred while attempting to update ingress controllers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_ingress_controllers_by_namespace**
> update_kubernetes_ingress_controllers_by_namespace(id, namespace, body)

Update (block/unblock) ingress controllers by namespace

Update (block/unblock) ingress controllers by namespace for the provided environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_ingress_controller import KubernetesK8sIngressController
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name
    body = [openapi_client.KubernetesK8sIngressController()] # List[KubernetesK8sIngressController] | Ingress controllers

    try:
        # Update (block/unblock) ingress controllers by namespace
        api_instance.update_kubernetes_ingress_controllers_by_namespace(id, namespace, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->update_kubernetes_ingress_controllers_by_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 
 **body** | [**List[KubernetesK8sIngressController]**](KubernetesK8sIngressController.md)| Ingress controllers | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier. |  -  |
**500** | Server error occurred while attempting to update ingress controllers by namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_namespace**
> PortainerK8sNamespaceInfo update_kubernetes_namespace(id, namespace, body)

Update a namespace

Update a namespace within the given environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_namespace_details import KubernetesK8sNamespaceDetails
from openapi_client.models.portainer_k8s_namespace_info import PortainerK8sNamespaceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace
    body = openapi_client.KubernetesK8sNamespaceDetails() # KubernetesK8sNamespaceDetails | Namespace details

    try:
        # Update a namespace
        api_response = api_instance.update_kubernetes_namespace(id, namespace, body)
        print("The response of KubernetesApi->update_kubernetes_namespace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->update_kubernetes_namespace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace | 
 **body** | [**KubernetesK8sNamespaceDetails**](KubernetesK8sNamespaceDetails.md)| Namespace details | 

### Return type

[**PortainerK8sNamespaceInfo**](PortainerK8sNamespaceInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific namespace. |  -  |
**500** | Server error occurred while attempting to update the namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_namespace_deprecated**
> PortainerK8sNamespaceInfo update_kubernetes_namespace_deprecated(id, namespace, body)

Update a namespace

Update a namespace within the given environment.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_namespace_details import KubernetesK8sNamespaceDetails
from openapi_client.models.portainer_k8s_namespace_info import PortainerK8sNamespaceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace
    body = openapi_client.KubernetesK8sNamespaceDetails() # KubernetesK8sNamespaceDetails | Namespace details

    try:
        # Update a namespace
        api_response = api_instance.update_kubernetes_namespace_deprecated(id, namespace, body)
        print("The response of KubernetesApi->update_kubernetes_namespace_deprecated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->update_kubernetes_namespace_deprecated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace | 
 **body** | [**KubernetesK8sNamespaceDetails**](KubernetesK8sNamespaceDetails.md)| Namespace details | 

### Return type

[**PortainerK8sNamespaceInfo**](PortainerK8sNamespaceInfo.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find a specific namespace. |  -  |
**500** | Server error occurred while attempting to update the namespace. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kubernetes_service**
> update_kubernetes_service(id, namespace, body)

Update a service

Update a service within a given namespace.
**Access policy**: Authenticated user.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.kubernetes_k8s_service_info import KubernetesK8sServiceInfo
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: jwt
configuration.api_key['jwt'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['jwt'] = 'Bearer'

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.KubernetesApi(api_client)
    id = 56 # int | Environment identifier
    namespace = 'namespace_example' # str | Namespace name
    body = openapi_client.KubernetesK8sServiceInfo() # KubernetesK8sServiceInfo | Service definition

    try:
        # Update a service
        api_instance.update_kubernetes_service(id, namespace, body)
    except Exception as e:
        print("Exception when calling KubernetesApi->update_kubernetes_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment identifier | 
 **namespace** | **str**| Namespace name | 
 **body** | [**KubernetesK8sServiceInfo**](KubernetesK8sServiceInfo.md)| Service definition | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**401** | Unauthorized access - the user is not authenticated or does not have the necessary permissions. Ensure that you have provided a valid API key or JWT token, and that you have the required permissions. |  -  |
**403** | Permission denied - the user is authenticated but does not have the necessary permissions to access the requested resource or perform the specified operation. Check your user roles and permissions. |  -  |
**404** | Unable to find an environment with the specified identifier or unable to find the service to update. |  -  |
**500** | Server error occurred while attempting to update a service. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

