# openapi_client.EndpointsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoint_association_delete**](EndpointsApi.md#endpoint_association_delete) | **PUT** /endpoints/{id}/association | De-association an edge environment(endpoint)
[**endpoint_create**](EndpointsApi.md#endpoint_create) | **POST** /endpoints | Create a new environment(endpoint)
[**endpoint_create_global_key**](EndpointsApi.md#endpoint_create_global_key) | **POST** /endpoints/global-key | Create or retrieve the endpoint for an EdgeID
[**endpoint_delete**](EndpointsApi.md#endpoint_delete) | **DELETE** /endpoints/{id} | Remove an environment
[**endpoint_delete_batch**](EndpointsApi.md#endpoint_delete_batch) | **POST** /endpoints/delete | Remove multiple environments
[**endpoint_delete_batch_deprecated**](EndpointsApi.md#endpoint_delete_batch_deprecated) | **DELETE** /endpoints | Remove multiple environments
[**endpoint_dockerhub_status**](EndpointsApi.md#endpoint_dockerhub_status) | **GET** /endpoints/{id}/dockerhub/{registryId} | fetch docker pull limits
[**endpoint_edge_status_inspect**](EndpointsApi.md#endpoint_edge_status_inspect) | **GET** /endpoints/{id}/edge/status | Get environment(endpoint) status
[**endpoint_force_update_service**](EndpointsApi.md#endpoint_force_update_service) | **PUT** /endpoints/{id}/forceupdateservice | force update a docker service
[**endpoint_inspect**](EndpointsApi.md#endpoint_inspect) | **GET** /endpoints/{id} | Inspect an environment(endpoint)
[**endpoint_list**](EndpointsApi.md#endpoint_list) | **GET** /endpoints | List environments(endpoints)
[**endpoint_registries_list**](EndpointsApi.md#endpoint_registries_list) | **GET** /endpoints/{id}/registries | List Registries on environment
[**endpoint_registry_access**](EndpointsApi.md#endpoint_registry_access) | **PUT** /endpoints/{id}/registries/{registryId} | update registry access for environment
[**endpoint_settings_update**](EndpointsApi.md#endpoint_settings_update) | **PUT** /endpoints/{id}/settings | Update settings for an environment(endpoint)
[**endpoint_snapshot**](EndpointsApi.md#endpoint_snapshot) | **POST** /endpoints/{id}/snapshot | Snapshots an environment(endpoint)
[**endpoint_snapshots**](EndpointsApi.md#endpoint_snapshots) | **POST** /endpoints/snapshot | Snapshot all environments(endpoints)
[**endpoint_update**](EndpointsApi.md#endpoint_update) | **PUT** /endpoints/{id} | Update an environment(endpoint)
[**endpoint_update_relations**](EndpointsApi.md#endpoint_update_relations) | **PUT** /endpoints/relations | Update relations for a list of environments
[**endpoints_id_docker_v2_browse_put_post**](EndpointsApi.md#endpoints_id_docker_v2_browse_put_post) | **POST** /endpoints/{id}/docker/v2/browse/put | Upload a file under a specific path on the file system of an environment (endpoint)
[**endpoints_id_edge_jobs_job_id_logs_post**](EndpointsApi.md#endpoints_id_edge_jobs_job_id_logs_post) | **POST** /endpoints/{id}/edge/jobs/{jobID}/logs | Inspect an EdgeJob Log
[**endpoints_id_edge_stacks_stack_id_get**](EndpointsApi.md#endpoints_id_edge_stacks_stack_id_get) | **GET** /endpoints/{id}/edge/stacks/{stackId} | Inspect an Edge Stack for an Environment(Endpoint)


# **endpoint_association_delete**
> endpoint_association_delete(id)

De-association an edge environment(endpoint)

De-association an edge environment(endpoint).
**Access policy**: administrator

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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # De-association an edge environment(endpoint)
        api_instance.endpoint_association_delete(id)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_association_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**404** | Environment(Endpoint) not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_create**
> PortainerEndpoint endpoint_create(name, endpoint_creation_type, edge_tunnel_server_address, container_engine=container_engine, url=url, public_url=public_url, group_id=group_id, tls=tls, tls_skip_verify=tls_skip_verify, tls_skip_client_verify=tls_skip_client_verify, tlsca_cert_file=tlsca_cert_file, tls_cert_file=tls_cert_file, tls_key_file=tls_key_file, azure_application_id=azure_application_id, azure_tenant_id=azure_tenant_id, azure_authentication_key=azure_authentication_key, tag_ids=tag_ids, edge_checkin_interval=edge_checkin_interval, gpus=gpus)

Create a new environment(endpoint)

Create a new environment(endpoint) that will be used to manage an environment(endpoint).
**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_endpoint import PortainerEndpoint
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
    api_instance = openapi_client.EndpointsApi(api_client)
    name = 'name_example' # str | Name that will be used to identify this environment(endpoint) (example: my-environment)
    endpoint_creation_type = 56 # int | Environment(Endpoint) type. Value must be one of: 1 (Local Docker environment), 2 (Agent environment), 3 (Azure environment), 4 (Edge agent environment) or 5 (Local Kubernetes Environment)
    edge_tunnel_server_address = 'edge_tunnel_server_address_example' # str | URL or IP address that will be used to establish a reverse tunnel
    container_engine = 'container_engine_example' # str | Container engine used by the environment(endpoint). Value must be one of: 'docker' or 'podman' (optional)
    url = 'url_example' # str | URL or IP address of a Docker host (example: docker.mydomain.tld:2375). Defaults to local if not specified (Linux: /var/run/docker.sock, Windows: //./pipe/docker_engine). Cannot be empty if EndpointCreationType is set to 4 (Edge agent environment) (optional)
    public_url = 'public_url_example' # str | URL or IP address where exposed containers will be reachable. Defaults to URL if not specified (example: docker.mydomain.tld:2375) (optional)
    group_id = 56 # int | Environment(Endpoint) group identifier. If not specified will default to 1 (unassigned). (optional)
    tls = True # bool | Require TLS to connect against this environment(endpoint). Must be true if EndpointCreationType is set to 2 (Agent environment) (optional)
    tls_skip_verify = True # bool | Skip server verification when using TLS. Must be true if EndpointCreationType is set to 2 (Agent environment) (optional)
    tls_skip_client_verify = True # bool | Skip client verification when using TLS. Must be true if EndpointCreationType is set to 2 (Agent environment) (optional)
    tlsca_cert_file = None # bytearray | TLS CA certificate file (optional)
    tls_cert_file = None # bytearray | TLS client certificate file (optional)
    tls_key_file = None # bytearray | TLS client key file (optional)
    azure_application_id = 'azure_application_id_example' # str | Azure application ID. Required if environment(endpoint) type is set to 3 (optional)
    azure_tenant_id = 'azure_tenant_id_example' # str | Azure tenant ID. Required if environment(endpoint) type is set to 3 (optional)
    azure_authentication_key = 'azure_authentication_key_example' # str | Azure authentication key. Required if environment(endpoint) type is set to 3 (optional)
    tag_ids = [56] # List[int] | List of tag identifiers to which this environment(endpoint) is associated (optional)
    edge_checkin_interval = 56 # int | The check in interval for edge agent (in seconds) (optional)
    gpus = 'gpus_example' # str | List of GPUs - json stringified array of {name, value} structs (optional)

    try:
        # Create a new environment(endpoint)
        api_response = api_instance.endpoint_create(name, endpoint_creation_type, edge_tunnel_server_address, container_engine=container_engine, url=url, public_url=public_url, group_id=group_id, tls=tls, tls_skip_verify=tls_skip_verify, tls_skip_client_verify=tls_skip_client_verify, tlsca_cert_file=tlsca_cert_file, tls_cert_file=tls_cert_file, tls_key_file=tls_key_file, azure_application_id=azure_application_id, azure_tenant_id=azure_tenant_id, azure_authentication_key=azure_authentication_key, tag_ids=tag_ids, edge_checkin_interval=edge_checkin_interval, gpus=gpus)
        print("The response of EndpointsApi->endpoint_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name that will be used to identify this environment(endpoint) (example: my-environment) | 
 **endpoint_creation_type** | **int**| Environment(Endpoint) type. Value must be one of: 1 (Local Docker environment), 2 (Agent environment), 3 (Azure environment), 4 (Edge agent environment) or 5 (Local Kubernetes Environment) | 
 **edge_tunnel_server_address** | **str**| URL or IP address that will be used to establish a reverse tunnel | 
 **container_engine** | **str**| Container engine used by the environment(endpoint). Value must be one of: &#39;docker&#39; or &#39;podman&#39; | [optional] 
 **url** | **str**| URL or IP address of a Docker host (example: docker.mydomain.tld:2375). Defaults to local if not specified (Linux: /var/run/docker.sock, Windows: //./pipe/docker_engine). Cannot be empty if EndpointCreationType is set to 4 (Edge agent environment) | [optional] 
 **public_url** | **str**| URL or IP address where exposed containers will be reachable. Defaults to URL if not specified (example: docker.mydomain.tld:2375) | [optional] 
 **group_id** | **int**| Environment(Endpoint) group identifier. If not specified will default to 1 (unassigned). | [optional] 
 **tls** | **bool**| Require TLS to connect against this environment(endpoint). Must be true if EndpointCreationType is set to 2 (Agent environment) | [optional] 
 **tls_skip_verify** | **bool**| Skip server verification when using TLS. Must be true if EndpointCreationType is set to 2 (Agent environment) | [optional] 
 **tls_skip_client_verify** | **bool**| Skip client verification when using TLS. Must be true if EndpointCreationType is set to 2 (Agent environment) | [optional] 
 **tlsca_cert_file** | **bytearray**| TLS CA certificate file | [optional] 
 **tls_cert_file** | **bytearray**| TLS client certificate file | [optional] 
 **tls_key_file** | **bytearray**| TLS client key file | [optional] 
 **azure_application_id** | **str**| Azure application ID. Required if environment(endpoint) type is set to 3 | [optional] 
 **azure_tenant_id** | **str**| Azure tenant ID. Required if environment(endpoint) type is set to 3 | [optional] 
 **azure_authentication_key** | **str**| Azure authentication key. Required if environment(endpoint) type is set to 3 | [optional] 
 **tag_ids** | [**List[int]**](int.md)| List of tag identifiers to which this environment(endpoint) is associated | [optional] 
 **edge_checkin_interval** | **int**| The check in interval for edge agent (in seconds) | [optional] 
 **gpus** | **str**| List of GPUs - json stringified array of {name, value} structs | [optional] 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**409** | Name is not unique |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_create_global_key**
> EndpointsEndpointCreateGlobalKeyResponse endpoint_create_global_key()

Create or retrieve the endpoint for an EdgeID

### Example


```python
import openapi_client
from openapi_client.models.endpoints_endpoint_create_global_key_response import EndpointsEndpointCreateGlobalKeyResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointsApi(api_client)

    try:
        # Create or retrieve the endpoint for an EdgeID
        api_response = api_instance.endpoint_create_global_key()
        print("The response of EndpointsApi->endpoint_create_global_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_create_global_key: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**EndpointsEndpointCreateGlobalKeyResponse**](EndpointsEndpointCreateGlobalKeyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_delete**
> endpoint_delete(id)

Remove an environment

Remove the environment associated to the specified identifier and optionally clean-up associated resources.
**Access policy**: Administrator only.

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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # Remove an environment
        api_instance.endpoint_delete(id)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Environment successfully deleted. |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**403** | Unauthorized access or operation not allowed. |  -  |
**404** | Unable to find the environment with the specified identifier inside the database. |  -  |
**500** | Server error occurred while attempting to delete the environment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_delete_batch**
> endpoint_delete_batch(body)

Remove multiple environments

Remove multiple environments and optionally clean-up associated resources.
**Access policy**: Administrator only.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpoints_endpoint_delete_batch_payload import EndpointsEndpointDeleteBatchPayload
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
    api_instance = openapi_client.EndpointsApi(api_client)
    body = openapi_client.EndpointsEndpointDeleteBatchPayload() # EndpointsEndpointDeleteBatchPayload | List of environments to delete, with optional deleteCluster flag to clean-up associated resources (cloud environments only)

    try:
        # Remove multiple environments
        api_instance.endpoint_delete_batch(body)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_delete_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointsEndpointDeleteBatchPayload**](EndpointsEndpointDeleteBatchPayload.md)| List of environments to delete, with optional deleteCluster flag to clean-up associated resources (cloud environments only) | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Environment(s) successfully deleted. |  -  |
**207** | Partial success. Some environments were deleted successfully, while others failed. |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**403** | Unauthorized access or operation not allowed. |  -  |
**500** | Server error occurred while attempting to delete the specified environments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_delete_batch_deprecated**
> endpoint_delete_batch_deprecated(body)

Remove multiple environments

Deprecated: use the `POST` endpoint instead.
Remove multiple environments and optionally clean-up associated resources.
**Access policy**: Administrator only.

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpoints_endpoint_delete_batch_payload import EndpointsEndpointDeleteBatchPayload
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
    api_instance = openapi_client.EndpointsApi(api_client)
    body = openapi_client.EndpointsEndpointDeleteBatchPayload() # EndpointsEndpointDeleteBatchPayload | List of environments to delete, with optional deleteCluster flag to clean-up associated resources (cloud environments only)

    try:
        # Remove multiple environments
        api_instance.endpoint_delete_batch_deprecated(body)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_delete_batch_deprecated: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointsEndpointDeleteBatchPayload**](EndpointsEndpointDeleteBatchPayload.md)| List of environments to delete, with optional deleteCluster flag to clean-up associated resources (cloud environments only) | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Environment(s) successfully deleted. |  -  |
**207** | Partial success. Some environments were deleted successfully, while others failed. |  -  |
**400** | Invalid request payload, such as missing required fields or fields not meeting validation criteria. |  -  |
**403** | Unauthorized access or operation not allowed. |  -  |
**500** | Server error occurred while attempting to delete the specified environments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_dockerhub_status**
> EndpointsDockerhubStatusResponse endpoint_dockerhub_status(id, registry_id)

fetch docker pull limits

get docker pull limits for a docker hub registry in the environment
**Access policy**:

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpoints_dockerhub_status_response import EndpointsDockerhubStatusResponse
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | endpoint ID
    registry_id = 56 # int | registry ID

    try:
        # fetch docker pull limits
        api_response = api_instance.endpoint_dockerhub_status(id, registry_id)
        print("The response of EndpointsApi->endpoint_dockerhub_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_dockerhub_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| endpoint ID | 
 **registry_id** | **int**| registry ID | 

### Return type

[**EndpointsDockerhubStatusResponse**](EndpointsDockerhubStatusResponse.md)

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
**403** | Permission denied |  -  |
**404** | registry or endpoint not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_edge_status_inspect**
> EndpointedgeEndpointEdgeStatusInspectResponse endpoint_edge_status_inspect(id)

Get environment(endpoint) status

environment(endpoint) for edge agent to check status of environment(endpoint)
**Access policy**: restricted only to Edge environments(endpoints)

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpointedge_endpoint_edge_status_inspect_response import EndpointedgeEndpointEdgeStatusInspectResponse
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # Get environment(endpoint) status
        api_response = api_instance.endpoint_edge_status_inspect(id)
        print("The response of EndpointsApi->endpoint_edge_status_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_edge_status_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

[**EndpointedgeEndpointEdgeStatusInspectResponse**](EndpointedgeEndpointEdgeStatusInspectResponse.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied to access environment(endpoint) |  -  |
**404** | Environment(Endpoint) not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_force_update_service**
> SwarmServiceUpdateResponse endpoint_force_update_service(id, body)

force update a docker service

force update a docker service
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpoints_force_update_service_payload import EndpointsForceUpdateServicePayload
from openapi_client.models.swarm_service_update_response import SwarmServiceUpdateResponse
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | endpoint identifier
    body = openapi_client.EndpointsForceUpdateServicePayload() # EndpointsForceUpdateServicePayload | details

    try:
        # force update a docker service
        api_response = api_instance.endpoint_force_update_service(id, body)
        print("The response of EndpointsApi->endpoint_force_update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_force_update_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| endpoint identifier | 
 **body** | [**EndpointsForceUpdateServicePayload**](EndpointsForceUpdateServicePayload.md)| details | 

### Return type

[**SwarmServiceUpdateResponse**](SwarmServiceUpdateResponse.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied |  -  |
**404** | endpoint not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_inspect**
> PortainerEndpoint endpoint_inspect(id, exclude_snapshot=exclude_snapshot)

Inspect an environment(endpoint)

Retrieve details about an environment(endpoint).
**Access policy**: restricted

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_endpoint import PortainerEndpoint
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    exclude_snapshot = True # bool | if true, the snapshot data won't be retrieved (optional)

    try:
        # Inspect an environment(endpoint)
        api_response = api_instance.endpoint_inspect(id, exclude_snapshot=exclude_snapshot)
        print("The response of EndpointsApi->endpoint_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **exclude_snapshot** | **bool**| if true, the snapshot data won&#39;t be retrieved | [optional] 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

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
**404** | Environment(Endpoint) not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_list**
> List[PortainerEndpoint] endpoint_list(start=start, limit=limit, sort=sort, order=order, search=search, group_ids=group_ids, status=status, types=types, tag_ids=tag_ids, tags_partial_match=tags_partial_match, endpoint_ids=endpoint_ids, exclude_ids=exclude_ids, provisioned=provisioned, agent_versions=agent_versions, edge_async=edge_async, edge_device_untrusted=edge_device_untrusted, edge_check_in_passed_seconds=edge_check_in_passed_seconds, exclude_snapshots=exclude_snapshots, name=name, edge_stack_status=edge_stack_status, edge_group_ids=edge_group_ids, exclude_edge_group_ids=exclude_edge_group_ids)

List environments(endpoints)

List all environments(endpoints) based on the current user authorizations. Will
return all environments(endpoints) if using an administrator or team leader account otherwise it will
only return authorized environments(endpoints).
**Access policy**: restricted

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_endpoint import PortainerEndpoint
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
    api_instance = openapi_client.EndpointsApi(api_client)
    start = 56 # int | Start searching from (optional)
    limit = 56 # int | Limit results to this value (optional)
    sort = 'sort_example' # str | Sort results by this value (optional)
    order = 56 # int | Order sorted results by desc/asc (optional)
    search = 'search_example' # str | Search query (optional)
    group_ids = [56] # List[int] | List environments(endpoints) of these groups (optional)
    status = [56] # List[int] | List environments(endpoints) by this status (optional)
    types = [56] # List[int] | List environments(endpoints) of this type (optional)
    tag_ids = [56] # List[int] | search environments(endpoints) with these tags (depends on tagsPartialMatch) (optional)
    tags_partial_match = True # bool | If true, will return environment(endpoint) which has one of tagIds, if false (or missing) will return only environments(endpoints) that has all the tags (optional)
    endpoint_ids = [56] # List[int] | will return only these environments(endpoints) (optional)
    exclude_ids = [56] # List[int] | will exclude these environments(endpoints) (optional)
    provisioned = True # bool | If true, will return environment(endpoint) that were provisioned (optional)
    agent_versions = ['agent_versions_example'] # List[str] | will return only environments with on of these agent versions (optional)
    edge_async = True # bool | if exists true show only edge async agents, false show only standard edge agents. if missing, will show both types (relevant only for edge agents) (optional)
    edge_device_untrusted = True # bool | if true, show only untrusted edge agents, if false show only trusted edge agents (relevant only for edge agents) (optional)
    edge_check_in_passed_seconds = 3.4 # float | if bigger then zero, show only edge agents that checked-in in the last provided seconds (relevant only for edge agents) (optional)
    exclude_snapshots = True # bool | if true, the snapshot data won't be retrieved (optional)
    name = 'name_example' # str | will return only environments(endpoints) with this name (optional)
    edge_stack_status = 'edge_stack_status_example' # str | only applied when edgeStackId exists. Filter the returned environments based on their deployment status in the stack (not the environment status!) (optional)
    edge_group_ids = [56] # List[int] | List environments(endpoints) of these edge groups (optional)
    exclude_edge_group_ids = [56] # List[int] | Exclude environments(endpoints) of these edge groups (optional)

    try:
        # List environments(endpoints)
        api_response = api_instance.endpoint_list(start=start, limit=limit, sort=sort, order=order, search=search, group_ids=group_ids, status=status, types=types, tag_ids=tag_ids, tags_partial_match=tags_partial_match, endpoint_ids=endpoint_ids, exclude_ids=exclude_ids, provisioned=provisioned, agent_versions=agent_versions, edge_async=edge_async, edge_device_untrusted=edge_device_untrusted, edge_check_in_passed_seconds=edge_check_in_passed_seconds, exclude_snapshots=exclude_snapshots, name=name, edge_stack_status=edge_stack_status, edge_group_ids=edge_group_ids, exclude_edge_group_ids=exclude_edge_group_ids)
        print("The response of EndpointsApi->endpoint_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **int**| Start searching from | [optional] 
 **limit** | **int**| Limit results to this value | [optional] 
 **sort** | **str**| Sort results by this value | [optional] 
 **order** | **int**| Order sorted results by desc/asc | [optional] 
 **search** | **str**| Search query | [optional] 
 **group_ids** | [**List[int]**](int.md)| List environments(endpoints) of these groups | [optional] 
 **status** | [**List[int]**](int.md)| List environments(endpoints) by this status | [optional] 
 **types** | [**List[int]**](int.md)| List environments(endpoints) of this type | [optional] 
 **tag_ids** | [**List[int]**](int.md)| search environments(endpoints) with these tags (depends on tagsPartialMatch) | [optional] 
 **tags_partial_match** | **bool**| If true, will return environment(endpoint) which has one of tagIds, if false (or missing) will return only environments(endpoints) that has all the tags | [optional] 
 **endpoint_ids** | [**List[int]**](int.md)| will return only these environments(endpoints) | [optional] 
 **exclude_ids** | [**List[int]**](int.md)| will exclude these environments(endpoints) | [optional] 
 **provisioned** | **bool**| If true, will return environment(endpoint) that were provisioned | [optional] 
 **agent_versions** | [**List[str]**](str.md)| will return only environments with on of these agent versions | [optional] 
 **edge_async** | **bool**| if exists true show only edge async agents, false show only standard edge agents. if missing, will show both types (relevant only for edge agents) | [optional] 
 **edge_device_untrusted** | **bool**| if true, show only untrusted edge agents, if false show only trusted edge agents (relevant only for edge agents) | [optional] 
 **edge_check_in_passed_seconds** | **float**| if bigger then zero, show only edge agents that checked-in in the last provided seconds (relevant only for edge agents) | [optional] 
 **exclude_snapshots** | **bool**| if true, the snapshot data won&#39;t be retrieved | [optional] 
 **name** | **str**| will return only environments(endpoints) with this name | [optional] 
 **edge_stack_status** | **str**| only applied when edgeStackId exists. Filter the returned environments based on their deployment status in the stack (not the environment status!) | [optional] 
 **edge_group_ids** | [**List[int]**](int.md)| List environments(endpoints) of these edge groups | [optional] 
 **exclude_edge_group_ids** | [**List[int]**](int.md)| Exclude environments(endpoints) of these edge groups | [optional] 

### Return type

[**List[PortainerEndpoint]**](PortainerEndpoint.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Endpoints |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_registries_list**
> List[PortainerRegistry] endpoint_registries_list(id, namespace=namespace)

List Registries on environment

List all registries based on the current user authorizations in current environment.
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_registry import PortainerRegistry
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    namespace = 'namespace_example' # str | required if kubernetes environment, will show registries by namespace (optional)

    try:
        # List Registries on environment
        api_response = api_instance.endpoint_registries_list(id, namespace=namespace)
        print("The response of EndpointsApi->endpoint_registries_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_registries_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **namespace** | **str**| required if kubernetes environment, will show registries by namespace | [optional] 

### Return type

[**List[PortainerRegistry]**](PortainerRegistry.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_registry_access**
> endpoint_registry_access(id, registry_id, body)

update registry access for environment

**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpoints_registry_access_payload import EndpointsRegistryAccessPayload
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    registry_id = 56 # int | Registry identifier
    body = openapi_client.EndpointsRegistryAccessPayload() # EndpointsRegistryAccessPayload | details

    try:
        # update registry access for environment
        api_instance.endpoint_registry_access(id, registry_id, body)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_registry_access: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **registry_id** | **int**| Registry identifier | 
 **body** | [**EndpointsRegistryAccessPayload**](EndpointsRegistryAccessPayload.md)| details | 

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
**400** | Invalid request |  -  |
**403** | Permission denied |  -  |
**404** | Endpoint not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_settings_update**
> PortainerEndpoint endpoint_settings_update(id, body)

Update settings for an environment(endpoint)

Update settings for an environment(endpoint).
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpoints_endpoint_settings_update_payload import EndpointsEndpointSettingsUpdatePayload
from openapi_client.models.portainer_endpoint import PortainerEndpoint
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    body = openapi_client.EndpointsEndpointSettingsUpdatePayload() # EndpointsEndpointSettingsUpdatePayload | Environment(Endpoint) details

    try:
        # Update settings for an environment(endpoint)
        api_response = api_instance.endpoint_settings_update(id, body)
        print("The response of EndpointsApi->endpoint_settings_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_settings_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **body** | [**EndpointsEndpointSettingsUpdatePayload**](EndpointsEndpointSettingsUpdatePayload.md)| Environment(Endpoint) details | 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**404** | Environment(Endpoint) not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_snapshot**
> endpoint_snapshot(id)

Snapshots an environment(endpoint)

Snapshots an environment(endpoint)
**Access policy**: administrator

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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier

    try:
        # Snapshots an environment(endpoint)
        api_instance.endpoint_snapshot(id)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**404** | Environment(Endpoint) not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_snapshots**
> endpoint_snapshots()

Snapshot all environments(endpoints)

Snapshot all environments(endpoints)
**Access policy**: administrator

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
    api_instance = openapi_client.EndpointsApi(api_client)

    try:
        # Snapshot all environments(endpoints)
        api_instance.endpoint_snapshots()
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_snapshots: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_update**
> PortainerEndpoint endpoint_update(id, body)

Update an environment(endpoint)

Update an environment(endpoint).
**Access policy**: authenticated

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.endpoints_endpoint_update_payload import EndpointsEndpointUpdatePayload
from openapi_client.models.portainer_endpoint import PortainerEndpoint
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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    body = openapi_client.EndpointsEndpointUpdatePayload() # EndpointsEndpointUpdatePayload | Environment(Endpoint) details

    try:
        # Update an environment(endpoint)
        api_response = api_instance.endpoint_update(id, body)
        print("The response of EndpointsApi->endpoint_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **body** | [**EndpointsEndpointUpdatePayload**](EndpointsEndpointUpdatePayload.md)| Environment(Endpoint) details | 

### Return type

[**PortainerEndpoint**](PortainerEndpoint.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**404** | Environment(Endpoint) not found |  -  |
**409** | Name is not unique |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoint_update_relations**
> endpoint_update_relations(body)

Update relations for a list of environments

Update relations for a list of environments
Edge groups, tags and environment group can be updated.

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):

```python
import openapi_client
from openapi_client.models.endpoints_endpoint_update_relations_payload import EndpointsEndpointUpdateRelationsPayload
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

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointsApi(api_client)
    body = openapi_client.EndpointsEndpointUpdateRelationsPayload() # EndpointsEndpointUpdateRelationsPayload | Environment relations data

    try:
        # Update relations for a list of environments
        api_instance.endpoint_update_relations(body)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoint_update_relations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EndpointsEndpointUpdateRelationsPayload**](EndpointsEndpointUpdateRelationsPayload.md)| Environment relations data | 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_id_docker_v2_browse_put_post**
> endpoints_id_docker_v2_browse_put_post(id, path, file, volume_id=volume_id)

Upload a file under a specific path on the file system of an environment (endpoint)

Use this environment(endpoint) to upload TLS files.
**Access policy**: administrator

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
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | Environment(Endpoint) identifier
    path = 'path_example' # str | The destination path to upload the file to
    file = None # bytearray | The file to upload
    volume_id = 'volume_id_example' # str | Optional volume identifier to upload the file (optional)

    try:
        # Upload a file under a specific path on the file system of an environment (endpoint)
        api_instance.endpoints_id_docker_v2_browse_put_post(id, path, file, volume_id=volume_id)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_id_docker_v2_browse_put_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Environment(Endpoint) identifier | 
 **path** | **str**| The destination path to upload the file to | 
 **file** | **bytearray**| The file to upload | 
 **volume_id** | **str**| Optional volume identifier to upload the file | [optional] 

### Return type

void (empty response body)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Invalid request |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_id_edge_jobs_job_id_logs_post**
> endpoints_id_edge_jobs_job_id_logs_post(id, job_id)

Inspect an EdgeJob Log

**Access policy**: public

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | environment(endpoint) Id
    job_id = 56 # int | Job Id

    try:
        # Inspect an EdgeJob Log
        api_instance.endpoints_id_edge_jobs_job_id_logs_post(id, job_id)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_id_edge_jobs_job_id_logs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| environment(endpoint) Id | 
 **job_id** | **int**| Job Id | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **endpoints_id_edge_stacks_stack_id_get**
> EdgeStackPayload endpoints_id_edge_stacks_stack_id_get(id, stack_id)

Inspect an Edge Stack for an Environment(Endpoint)

**Access policy**: public

### Example


```python
import openapi_client
from openapi_client.models.edge_stack_payload import EdgeStackPayload
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EndpointsApi(api_client)
    id = 56 # int | environment(endpoint) Id
    stack_id = 56 # int | EdgeStack Id

    try:
        # Inspect an Edge Stack for an Environment(Endpoint)
        api_response = api_instance.endpoints_id_edge_stacks_stack_id_get(id, stack_id)
        print("The response of EndpointsApi->endpoints_id_edge_stacks_stack_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EndpointsApi->endpoints_id_edge_stacks_stack_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| environment(endpoint) Id | 
 **stack_id** | **int**| EdgeStack Id | 

### Return type

[**EdgeStackPayload**](EdgeStackPayload.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

