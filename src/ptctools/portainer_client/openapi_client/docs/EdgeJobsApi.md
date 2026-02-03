# openapi_client.EdgeJobsApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edge_job_create_file**](EdgeJobsApi.md#edge_job_create_file) | **POST** /edge_jobs/create/file | Create an EdgeJob from a file
[**edge_job_create_string**](EdgeJobsApi.md#edge_job_create_string) | **POST** /edge_jobs/create/string | Create an EdgeJob from a text
[**edge_job_delete**](EdgeJobsApi.md#edge_job_delete) | **DELETE** /edge_jobs/{id} | Delete an EdgeJob
[**edge_job_file**](EdgeJobsApi.md#edge_job_file) | **GET** /edge_jobs/{id}/file | Fetch a file of an EdgeJob
[**edge_job_inspect**](EdgeJobsApi.md#edge_job_inspect) | **GET** /edge_jobs/{id} | Inspect an EdgeJob
[**edge_job_list**](EdgeJobsApi.md#edge_job_list) | **GET** /edge_jobs | Fetch EdgeJobs list
[**edge_job_task_logs_inspect**](EdgeJobsApi.md#edge_job_task_logs_inspect) | **GET** /edge_jobs/{id}/tasks/{taskID}/logs | Fetch the log for a specifc task on an EdgeJob
[**edge_job_tasks_clear**](EdgeJobsApi.md#edge_job_tasks_clear) | **DELETE** /edge_jobs/{id}/tasks/{taskID}/logs | Clear the log for a specifc task on an EdgeJob
[**edge_job_tasks_collect**](EdgeJobsApi.md#edge_job_tasks_collect) | **POST** /edge_jobs/{id}/tasks/{taskID}/logs | Collect the log for a specifc task on an EdgeJob
[**edge_job_tasks_list**](EdgeJobsApi.md#edge_job_tasks_list) | **GET** /edge_jobs/{id}/tasks | Fetch the list of tasks on an EdgeJob
[**edge_job_update**](EdgeJobsApi.md#edge_job_update) | **PUT** /edge_jobs/{id} | Update an EdgeJob


# **edge_job_create_file**
> PortainerEdgeGroup edge_job_create_file(file, name, cron_expression, edge_groups, endpoints, recurring=recurring)

Create an EdgeJob from a file

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_edge_group import PortainerEdgeGroup
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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    file = None # bytearray | Content of the Stack file
    name = 'name_example' # str | Name of the stack
    cron_expression = 'cron_expression_example' # str | A cron expression to schedule this job
    edge_groups = 'edge_groups_example' # str | JSON stringified array of Edge Groups ids
    endpoints = 'endpoints_example' # str | JSON stringified array of Environment ids
    recurring = True # bool | If recurring (optional)

    try:
        # Create an EdgeJob from a file
        api_response = api_instance.edge_job_create_file(file, name, cron_expression, edge_groups, endpoints, recurring=recurring)
        print("The response of EdgeJobsApi->edge_job_create_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_create_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Content of the Stack file | 
 **name** | **str**| Name of the stack | 
 **cron_expression** | **str**| A cron expression to schedule this job | 
 **edge_groups** | **str**| JSON stringified array of Edge Groups ids | 
 **endpoints** | **str**| JSON stringified array of Environment ids | 
 **recurring** | **bool**| If recurring | [optional] 

### Return type

[**PortainerEdgeGroup**](PortainerEdgeGroup.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_create_string**
> PortainerEdgeGroup edge_job_create_string(body)

Create an EdgeJob from a text

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgejobs_edge_job_create_from_file_content_payload import EdgejobsEdgeJobCreateFromFileContentPayload
from openapi_client.models.portainer_edge_group import PortainerEdgeGroup
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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    body = openapi_client.EdgejobsEdgeJobCreateFromFileContentPayload() # EdgejobsEdgeJobCreateFromFileContentPayload | EdgeGroup data when method is string

    try:
        # Create an EdgeJob from a text
        api_response = api_instance.edge_job_create_string(body)
        print("The response of EdgeJobsApi->edge_job_create_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_create_string: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EdgejobsEdgeJobCreateFromFileContentPayload**](EdgejobsEdgeJobCreateFromFileContentPayload.md)| EdgeGroup data when method is string | 

### Return type

[**PortainerEdgeGroup**](PortainerEdgeGroup.md)

### Authorization

[jwt](../README.md#jwt), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**500** | Internal Server Error |  -  |
**503** | Edge compute features are disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edge_job_delete**
> edge_job_delete(id)

Delete an EdgeJob

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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id

    try:
        # Delete an EdgeJob
        api_instance.edge_job_delete(id)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 

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

# **edge_job_file**
> EdgejobsEdgeJobFileResponse edge_job_file(id)

Fetch a file of an EdgeJob

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgejobs_edge_job_file_response import EdgejobsEdgeJobFileResponse
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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id

    try:
        # Fetch a file of an EdgeJob
        api_response = api_instance.edge_job_file(id)
        print("The response of EdgeJobsApi->edge_job_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 

### Return type

[**EdgejobsEdgeJobFileResponse**](EdgejobsEdgeJobFileResponse.md)

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

# **edge_job_inspect**
> PortainerEdgeJob edge_job_inspect(id)

Inspect an EdgeJob

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_edge_job import PortainerEdgeJob
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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id

    try:
        # Inspect an EdgeJob
        api_response = api_instance.edge_job_inspect(id)
        print("The response of EdgeJobsApi->edge_job_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 

### Return type

[**PortainerEdgeJob**](PortainerEdgeJob.md)

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

# **edge_job_list**
> List[PortainerEdgeJob] edge_job_list()

Fetch EdgeJobs list

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.portainer_edge_job import PortainerEdgeJob
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
    api_instance = openapi_client.EdgeJobsApi(api_client)

    try:
        # Fetch EdgeJobs list
        api_response = api_instance.edge_job_list()
        print("The response of EdgeJobsApi->edge_job_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PortainerEdgeJob]**](PortainerEdgeJob.md)

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

# **edge_job_task_logs_inspect**
> EdgejobsFileResponse edge_job_task_logs_inspect(id, task_id)

Fetch the log for a specifc task on an EdgeJob

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgejobs_file_response import EdgejobsFileResponse
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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id
    task_id = 56 # int | Task Id

    try:
        # Fetch the log for a specifc task on an EdgeJob
        api_response = api_instance.edge_job_task_logs_inspect(id, task_id)
        print("The response of EdgeJobsApi->edge_job_task_logs_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_task_logs_inspect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 
 **task_id** | **int**| Task Id | 

### Return type

[**EdgejobsFileResponse**](EdgejobsFileResponse.md)

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

# **edge_job_tasks_clear**
> edge_job_tasks_clear(id, task_id)

Clear the log for a specifc task on an EdgeJob

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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id
    task_id = 56 # int | Task Id

    try:
        # Clear the log for a specifc task on an EdgeJob
        api_instance.edge_job_tasks_clear(id, task_id)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_tasks_clear: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 
 **task_id** | **int**| Task Id | 

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

# **edge_job_tasks_collect**
> edge_job_tasks_collect(id, task_id)

Collect the log for a specifc task on an EdgeJob

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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id
    task_id = 56 # int | Task Id

    try:
        # Collect the log for a specifc task on an EdgeJob
        api_instance.edge_job_tasks_collect(id, task_id)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_tasks_collect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 
 **task_id** | **int**| Task Id | 

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

# **edge_job_tasks_list**
> List[EdgejobsTaskContainer] edge_job_tasks_list(id)

Fetch the list of tasks on an EdgeJob

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgejobs_task_container import EdgejobsTaskContainer
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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id

    try:
        # Fetch the list of tasks on an EdgeJob
        api_response = api_instance.edge_job_tasks_list(id)
        print("The response of EdgeJobsApi->edge_job_tasks_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_tasks_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 

### Return type

[**List[EdgejobsTaskContainer]**](EdgejobsTaskContainer.md)

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

# **edge_job_update**
> PortainerEdgeJob edge_job_update(id, body)

Update an EdgeJob

**Access policy**: administrator

### Example

* Api Key Authentication (jwt):
* Api Key Authentication (ApiKeyAuth):

```python
import openapi_client
from openapi_client.models.edgejobs_edge_job_update_payload import EdgejobsEdgeJobUpdatePayload
from openapi_client.models.portainer_edge_job import PortainerEdgeJob
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
    api_instance = openapi_client.EdgeJobsApi(api_client)
    id = 56 # int | EdgeJob Id
    body = openapi_client.EdgejobsEdgeJobUpdatePayload() # EdgejobsEdgeJobUpdatePayload | EdgeGroup data

    try:
        # Update an EdgeJob
        api_response = api_instance.edge_job_update(id, body)
        print("The response of EdgeJobsApi->edge_job_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeJobsApi->edge_job_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| EdgeJob Id | 
 **body** | [**EdgejobsEdgeJobUpdatePayload**](EdgejobsEdgeJobUpdatePayload.md)| EdgeGroup data | 

### Return type

[**PortainerEdgeJob**](PortainerEdgeJob.md)

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

