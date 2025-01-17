# permify_async.BundleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_delete**](BundleApi.md#bundle_delete) | **POST** /v1/tenants/{tenant_id}/bundle/delete | delete bundle
[**bundle_read**](BundleApi.md#bundle_read) | **POST** /v1/tenants/{tenant_id}/bundle/read | read bundle
[**bundle_write**](BundleApi.md#bundle_write) | **POST** /v1/tenants/{tenant_id}/bundle/write | write bundle


# **bundle_delete**
> BundleDeleteResponse bundle_delete(tenant_id, body)

delete bundle

### Example


```python
import permify_async
from permify_async.models.bundle_delete_body import BundleDeleteBody
from permify_async.models.bundle_delete_response import BundleDeleteResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.BundleDeleteBody() # BundleDeleteBody | 

    try:
        # delete bundle
        api_response = await api_instance.bundle_delete(tenant_id, body)
        print("The response of BundleApi->bundle_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundleApi->bundle_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**BundleDeleteBody**](BundleDeleteBody.md)|  | 

### Return type

[**BundleDeleteResponse**](BundleDeleteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_read**
> BundleReadResponse bundle_read(tenant_id, body)

read bundle

### Example


```python
import permify_async
from permify_async.models.bundle_read_body import BundleReadBody
from permify_async.models.bundle_read_response import BundleReadResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.BundleReadBody() # BundleReadBody | 

    try:
        # read bundle
        api_response = await api_instance.bundle_read(tenant_id, body)
        print("The response of BundleApi->bundle_read:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundleApi->bundle_read: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**BundleReadBody**](BundleReadBody.md)|  | 

### Return type

[**BundleReadResponse**](BundleReadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_write**
> BundleWriteResponse bundle_write(tenant_id, body)

write bundle

### Example


```python
import permify_async
from permify_async.models.bundle_write_body import BundleWriteBody
from permify_async.models.bundle_write_response import BundleWriteResponse
from permify_async.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = permify_async.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with permify_async.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = permify_async.BundleApi(api_client)
    tenant_id = 'tenant_id_example' # str | Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant <code>t1</code> for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes.
    body = permify_async.BundleWriteBody() # BundleWriteBody | 

    try:
        # write bundle
        api_response = await api_instance.bundle_write(tenant_id, body)
        print("The response of BundleApi->bundle_write:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BundleApi->bundle_write: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| Identifier of the tenant, if you are not using multi-tenancy (have only one tenant) use pre-inserted tenant &lt;code&gt;t1&lt;/code&gt; for this field. Required, and must match the pattern \\“[a-zA-Z0-9-,]+\\“, max 64 bytes. | 
 **body** | [**BundleWriteBody**](BundleWriteBody.md)|  | 

### Return type

[**BundleWriteResponse**](BundleWriteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

