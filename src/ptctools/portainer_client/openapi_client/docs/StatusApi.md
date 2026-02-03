# openapi_client.StatusApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_inspect**](StatusApi.md#status_inspect) | **GET** /status | Check Portainer status


# **status_inspect**
> SystemStatus status_inspect()

Check Portainer status

Deprecated: use the `/system/status` endpoint instead.
Retrieve Portainer status
**Access policy**: public

### Example


```python
import openapi_client
from openapi_client.models.system_status import SystemStatus
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
    api_instance = openapi_client.StatusApi(api_client)

    try:
        # Check Portainer status
        api_response = api_instance.status_inspect()
        print("The response of StatusApi->status_inspect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_inspect: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SystemStatus**](SystemStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

