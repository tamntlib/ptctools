# openapi_client.UploadApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_tls**](UploadApi.md#upload_tls) | **POST** /upload/tls/{certificate} | Upload TLS files


# **upload_tls**
> upload_tls(certificate, folder, file)

Upload TLS files

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
    api_instance = openapi_client.UploadApi(api_client)
    certificate = 'certificate_example' # str | TLS file type. Valid values are 'ca', 'cert' or 'key'.
    folder = 'folder_example' # str | Folder where the TLS file will be stored. Will be created if not existing
    file = None # bytearray | The file to upload

    try:
        # Upload TLS files
        api_instance.upload_tls(certificate, folder, file)
    except Exception as e:
        print("Exception when calling UploadApi->upload_tls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | **str**| TLS file type. Valid values are &#39;ca&#39;, &#39;cert&#39; or &#39;key&#39;. | 
 **folder** | **str**| Folder where the TLS file will be stored. Will be created if not existing | 
 **file** | **bytearray**| The file to upload | 

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

