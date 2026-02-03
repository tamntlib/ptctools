# openapi_client.WebsocketApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**websocket_attach_get**](WebsocketApi.md#websocket_attach_get) | **GET** /websocket/attach | Attach a websocket
[**websocket_exec_get**](WebsocketApi.md#websocket_exec_get) | **GET** /websocket/exec | Execute a websocket
[**websocket_kubernetes_shell_get**](WebsocketApi.md#websocket_kubernetes_shell_get) | **GET** /websocket/kubernetes-shell | Execute a websocket on kubectl shell pod
[**websocket_pod_get**](WebsocketApi.md#websocket_pod_get) | **GET** /websocket/pod | Execute a websocket on pod


# **websocket_attach_get**
> websocket_attach_get(endpoint_id, token, node_name=node_name)

Attach a websocket

If the nodeName query parameter is present, the request will be proxied to the underlying agent environment(endpoint).
If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and
an AttachStart operation HTTP request will be created and hijacked.
**Access policy**: authenticated

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
    api_instance = openapi_client.WebsocketApi(api_client)
    endpoint_id = 56 # int | environment(endpoint) ID of the environment(endpoint) where the resource is located
    token = 'token_example' # str | JWT token used for authentication against this environment(endpoint)
    node_name = 'node_name_example' # str | node name (optional)

    try:
        # Attach a websocket
        api_instance.websocket_attach_get(endpoint_id, token, node_name=node_name)
    except Exception as e:
        print("Exception when calling WebsocketApi->websocket_attach_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| environment(endpoint) ID of the environment(endpoint) where the resource is located | 
 **token** | **str**| JWT token used for authentication against this environment(endpoint) | 
 **node_name** | **str**| node name | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **websocket_exec_get**
> websocket_exec_get(endpoint_id, token, node_name=node_name)

Execute a websocket

If the nodeName query parameter is present, the request will be proxied to the underlying agent environment(endpoint).
If the nodeName query parameter is not specified, the request will be upgraded to the websocket protocol and
an ExecStart operation HTTP request will be created and hijacked.

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
    api_instance = openapi_client.WebsocketApi(api_client)
    endpoint_id = 56 # int | environment(endpoint) ID of the environment(endpoint) where the resource is located
    token = 'token_example' # str | JWT token used for authentication against this environment(endpoint)
    node_name = 'node_name_example' # str | node name (optional)

    try:
        # Execute a websocket
        api_instance.websocket_exec_get(endpoint_id, token, node_name=node_name)
    except Exception as e:
        print("Exception when calling WebsocketApi->websocket_exec_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| environment(endpoint) ID of the environment(endpoint) where the resource is located | 
 **token** | **str**| JWT token used for authentication against this environment(endpoint) | 
 **node_name** | **str**| node name | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **websocket_kubernetes_shell_get**
> websocket_kubernetes_shell_get(endpoint_id, token)

Execute a websocket on kubectl shell pod

The request will be upgraded to the websocket protocol. The request will proxy input from the client to the pod via long-lived websocket connection.
**Access policy**: authenticated

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
    api_instance = openapi_client.WebsocketApi(api_client)
    endpoint_id = 56 # int | environment(endpoint) ID of the environment(endpoint) where the resource is located
    token = 'token_example' # str | JWT token used for authentication against this environment(endpoint)

    try:
        # Execute a websocket on kubectl shell pod
        api_instance.websocket_kubernetes_shell_get(endpoint_id, token)
    except Exception as e:
        print("Exception when calling WebsocketApi->websocket_kubernetes_shell_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| environment(endpoint) ID of the environment(endpoint) where the resource is located | 
 **token** | **str**| JWT token used for authentication against this environment(endpoint) | 

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
**200** | Success |  -  |
**400** | Invalid request |  -  |
**403** | Permission denied |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **websocket_pod_get**
> websocket_pod_get(endpoint_id, namespace, pod_name, container_name, command, token)

Execute a websocket on pod

The request will be upgraded to the websocket protocol.
**Access policy**: authenticated

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
    api_instance = openapi_client.WebsocketApi(api_client)
    endpoint_id = 56 # int | environment(endpoint) ID of the environment(endpoint) where the resource is located
    namespace = 'namespace_example' # str | namespace where the container is located
    pod_name = 'pod_name_example' # str | name of the pod containing the container
    container_name = 'container_name_example' # str | name of the container
    command = 'command_example' # str | command to execute in the container
    token = 'token_example' # str | JWT token used for authentication against this environment(endpoint)

    try:
        # Execute a websocket on pod
        api_instance.websocket_pod_get(endpoint_id, namespace, pod_name, container_name, command, token)
    except Exception as e:
        print("Exception when calling WebsocketApi->websocket_pod_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| environment(endpoint) ID of the environment(endpoint) where the resource is located | 
 **namespace** | **str**| namespace where the container is located | 
 **pod_name** | **str**| name of the pod containing the container | 
 **container_name** | **str**| name of the container | 
 **command** | **str**| command to execute in the container | 
 **token** | **str**| JWT token used for authentication against this environment(endpoint) | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

