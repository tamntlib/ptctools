# openapi_client.EdgeStacksApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_stack_create_file**](EdgeStacksApi.md#edge_stack_create_file) | **POST** /edge_stacks/create/file | Create an EdgeStack from file
[**edge_stack_create_repository**](EdgeStacksApi.md#edge_stack_create_repository) | **POST** /edge_stacks/create/repository | Create an EdgeStack from a git repository
[**edge_stack_create_string**](EdgeStacksApi.md#edge_stack_create_string) | **POST** /edge_stacks/create/string | Create an EdgeStack from a text
[**edge_stack_delete**](EdgeStacksApi.md#edge_stack_delete) | **DELETE** /edge_stacks/{id} | Delete an EdgeStack
[**edge_stack_file**](EdgeStacksApi.md#edge_stack_file) | **GET** /edge_stacks/{id}/file | Fetches the stack file for an EdgeStack
[**edge_stack_inspect**](EdgeStacksApi.md#edge_stack_inspect) | **GET** /edge_stacks/{id} | Inspect an EdgeStack
[**edge_stack_list**](EdgeStacksApi.md#edge_stack_list) | **GET** /edge_stacks | Fetches the list of EdgeStacks
[**edge_stack_status_update**](EdgeStacksApi.md#edge_stack_status_update) | **PUT** /edge_stacks/{id}/status | Update an EdgeStack status
[**edge_stack_update**](EdgeStacksApi.md#edge_stack_update) | **PUT** /edge_stacks/{id} | Update an EdgeStack
[**endpoints_id_edge_stacks_stack_id_get**](EdgeStacksApi.md#endpoints_id_edge_stacks_stack_id_get) | **GET** /endpoints/{id}/edge/stacks/{stackId} | Inspect an Edge Stack for an Environment(Endpoint)


# **edge_stack_create_file**
> PortainerEdgeStack edge_stack_create_file(name, file, edge_groups, deployment_type, dryrun=dryrun, registries=registries, use_manifest_namespaces=use_manifest_namespaces, pre_pull_image=pre_pull_image, retry_deploy=retry_deploy)

Create an EdgeStack from file

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    name = 'name_example' # str | Name of the stack. it must only consist of lowercase alphanumeric characters, hyphens, or underscores as well as start with a letter or number
    file = None # bytearray | Content of the Stack file
    edge_groups = 'edge_groups_example' # str | JSON stringified array of Edge Groups ids
    deployment_type = 56 # int | deploy type 0 - 'compose', 1 - 'kubernetes'
    dryrun = 'dryrun_example' # str | if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object (optional)
    registries = 'registries_example' # str | JSON stringified array of Registry ids to use for this stack (optional)
    use_manifest_namespaces = True # bool | Uses the manifest's namespaces instead of the default one, relevant only for kube environments (optional)
    pre_pull_image = True # bool | Pre Pull image (optional)
    retry_deploy = True # bool | Retry deploy (optional)

    try:
        # Create an EdgeStack from file
        api_response = api_instance.edge_stack_create_file(name, file, edge_groups, deployment_type, dryrun=dryrun, registries=registries, use_manifest_namespaces=use_manifest_namespaces, pre_pull_image=pre_pull_image, retry_deploy=retry_deploy)
        print("The response of EdgeStacksApi->edge_stack_create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the stack. it must only consist of lowercase alphanumeric characters, hyphens, or underscores as well as start with a letter or number | 
 **file** | **bytearray**| Content of the Stack file | 
 **edge_groups** | **str**| JSON stringified array of Edge Groups ids | 
 **deployment_type** | **int**| deploy type 0 - &#39;compose&#39;, 1 - &#39;kubernetes&#39; | 
 **dryrun** | **str**| if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object | [optional] 
 **registries** | **str**| JSON stringified array of Registry ids to use for this stack | [optional] 
 **use_manifest_namespaces** | **bool**| Uses the manifest&#39;s namespaces instead of the default one, relevant only for kube environments | [optional] 
 **pre_pull_image** | **bool**| Pre Pull image | [optional] 
 **retry_deploy** | **bool**| Retry deploy | [optional] 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_create_repository**
> PortainerEdgeStack edge_stack_create_repository(body, dryrun=dryrun)

Create an EdgeStack from a git repository

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgestacks_edge_stack_from_git_repository_payload import EdgestacksEdgeStackFromGitRepositoryPayload
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    body = openapi_client.EdgestacksEdgeStackFromGitRepositoryPayload() # EdgestacksEdgeStackFromGitRepositoryPayload | stack config
    dryrun = 'dryrun_example' # str | if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object (optional)

    try:
        # Create an EdgeStack from a git repository
        api_response = api_instance.edge_stack_create_repository(body, dryrun=dryrun)
        print("The response of EdgeStacksApi->edge_stack_create_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_create_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdgestacksEdgeStackFromGitRepositoryPayload**](EdgestacksEdgeStackFromGitRepositoryPayload.md)| stack config | 
 **dryrun** | **str**| if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object | [optional] 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_create_string**
> PortainerEdgeStack edge_stack_create_string(body, dryrun=dryrun)

Create an EdgeStack from a text

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgestacks_edge_stack_from_string_payload import EdgestacksEdgeStackFromStringPayload
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    body = openapi_client.EdgestacksEdgeStackFromStringPayload() # EdgestacksEdgeStackFromStringPayload | stack config
    dryrun = 'dryrun_example' # str | if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object (optional)

    try:
        # Create an EdgeStack from a text
        api_response = api_instance.edge_stack_create_string(body, dryrun=dryrun)
        print("The response of EdgeStacksApi->edge_stack_create_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_create_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdgestacksEdgeStackFromStringPayload**](EdgestacksEdgeStackFromStringPayload.md)| stack config | 
 **dryrun** | **str**| if true, will not create an edge stack, but just will check the settings and return a non-persisted edge stack object | [optional] 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**500** | Internal server error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_delete**
> edge_stack_delete(id)

Delete an EdgeStack

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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    id = 56 # int | EdgeStack Id

    try:
        # Delete an EdgeStack
        api_instance.edge_stack_delete(id)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeStack Id | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_file**
> EdgestacksStackFileResponse edge_stack_file(id)

Fetches the stack file for an EdgeStack

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgestacks_stack_file_response import EdgestacksStackFileResponse
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    id = 56 # int | EdgeStack Id

    try:
        # Fetches the stack file for an EdgeStack
        api_response = api_instance.edge_stack_file(id)
        print("The response of EdgeStacksApi->edge_stack_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeStack Id | 

### Return type

[**EdgestacksStackFileResponse**](EdgestacksStackFileResponse.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_inspect**
> PortainerEdgeStack edge_stack_inspect(id)

Inspect an EdgeStack

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    id = 56 # int | EdgeStack Id

    try:
        # Inspect an EdgeStack
        api_response = api_instance.edge_stack_inspect(id)
        print("The response of EdgeStacksApi->edge_stack_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeStack Id | 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_list**
> List[PortainerEdgeStack] edge_stack_list(summarize_statuses=summarize_statuses)

Fetches the list of EdgeStacks

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    summarize_statuses = True # bool | will summarize the statuses (optional)

    try:
        # Fetches the list of EdgeStacks
        api_response = api_instance.edge_stack_list(summarize_statuses=summarize_statuses)
        print("The response of EdgeStacksApi->edge_stack_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **summarize_statuses** | **bool**| will summarize the statuses | [optional] 

### Return type

[**List[PortainerEdgeStack]**](PortainerEdgeStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_status_update**
> PortainerEdgeStack edge_stack_status_update(id, body)

Update an EdgeStack status

Authorized only if the request is done by an Edge Environment(Endpoint)

### Example


```python
import openapi_client
from openapi_client.models.edgestacks_update_status_payload import EdgestacksUpdateStatusPayload
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    id = 56 # int | EdgeStack Id
    body = openapi_client.EdgestacksUpdateStatusPayload() # EdgestacksUpdateStatusPayload | EdgeStack status payload

    try:
        # Update an EdgeStack status
        api_response = api_instance.edge_stack_status_update(id, body)
        print("The response of EdgeStacksApi->edge_stack_status_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_status_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeStack Id | 
 **body** | [**EdgestacksUpdateStatusPayload**](EdgestacksUpdateStatusPayload.md)| EdgeStack status payload | 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_stack_update**
> PortainerEdgeStack edge_stack_update(id, body)

Update an EdgeStack

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgestacks_update_edge_stack_payload import EdgestacksUpdateEdgeStackPayload
from openapi_client.models.portainer_edge_stack import PortainerEdgeStack
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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    id = 56 # int | EdgeStack Id
    body = openapi_client.EdgestacksUpdateEdgeStackPayload() # EdgestacksUpdateEdgeStackPayload | EdgeStack data

    try:
        # Update an EdgeStack
        api_response = api_instance.edge_stack_update(id, body)
        print("The response of EdgeStacksApi->edge_stack_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->edge_stack_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeStack Id | 
 **body** | [**EdgestacksUpdateEdgeStackPayload**](EdgestacksUpdateEdgeStackPayload.md)| EdgeStack data | 

### Return type

[**PortainerEdgeStack**](PortainerEdgeStack.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**500** | Internal Server Error |  -  |
**503** | Edge compute features are disabled |  -  |

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
    api_instance = openapi_client.EdgeStacksApi(api_client)
    id = 56 # int | environment(endpoint) Id
    stack_id = 56 # int | EdgeStack Id

    try:
        # Inspect an Edge Stack for an Environment(Endpoint)
        api_response = api_instance.endpoints_id_edge_stacks_stack_id_get(id, stack_id)
        print("The response of EdgeStacksApi->endpoints_id_edge_stacks_stack_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeStacksApi->endpoints_id_edge_stacks_stack_id_get: %s\n" % e)
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

