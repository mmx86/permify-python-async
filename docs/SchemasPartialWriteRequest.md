# SchemasPartialWriteRequest

It contains the tenant_id to identify the tenant and metadata of the schema to be edited, with the corresponding edits to various entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**SchemaPartialWriteRequestMetadata**](SchemaPartialWriteRequestMetadata.md) |  | [optional] 
**partials** | [**Dict[str, Partials]**](Partials.md) |  | [optional] 

## Example

```python
from permify_async.models.schemas_partial_write_request import SchemasPartialWriteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasPartialWriteRequest from a JSON string
schemas_partial_write_request_instance = SchemasPartialWriteRequest.from_json(json)
# print the JSON string representation of the object
print(SchemasPartialWriteRequest.to_json())

# convert the object into a dict
schemas_partial_write_request_dict = schemas_partial_write_request_instance.to_dict()
# create an instance of SchemasPartialWriteRequest from a dict
schemas_partial_write_request_from_dict = SchemasPartialWriteRequest.from_dict(schemas_partial_write_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


