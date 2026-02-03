# openapi_client.EdgeApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**endpoints_id_edge_jobs_job_id_logs_post**](EdgeApi.md#endpoints_id_edge_jobs_job_id_logs_post) | **POST** /endpoints/{id}/edge/jobs/{jobID}/logs | Inspect an EdgeJob Log
[**endpoints_id_edge_stacks_stack_id_get**](EdgeApi.md#endpoints_id_edge_stacks_stack_id_get) | **GET** /endpoints/{id}/edge/stacks/{stackId} | Inspect an Edge Stack for an Environment(Endpoint)


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
    api_instance = openapi_client.EdgeApi(api_client)
    id = 56 # int | environment(endpoint) Id
    job_id = 56 # int | Job Id

    try:
        # Inspect an EdgeJob Log
        api_instance.endpoints_id_edge_jobs_job_id_logs_post(id, job_id)
    except Exception as e:
        print("Exception when calling EdgeApi->endpoints_id_edge_jobs_job_id_logs_post: %s\n" % e)
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
    api_instance = openapi_client.EdgeApi(api_client)
    id = 56 # int | environment(endpoint) Id
    stack_id = 56 # int | EdgeStack Id

    try:
        # Inspect an Edge Stack for an Environment(Endpoint)
        api_response = api_instance.endpoints_id_edge_stacks_stack_id_get(id, stack_id)
        print("The response of EdgeApi->endpoints_id_edge_stacks_stack_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EdgeApi->endpoints_id_edge_stacks_stack_id_get: %s\n" % e)
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

