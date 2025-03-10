# PartialWriteBody

It contains the tenant_id to identify the tenant and metadata of the schema to be edited, with the corresponding edits to various entities

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**SchemaPartialWriteRequestMetadata**](SchemaPartialWriteRequestMetadata.md) |  | [optional] 
**partials** | [**Dict[str, Partials]**](Partials.md) |  | [optional] 

## Example

```python
from permify_async.models.partial_write_body import PartialWriteBody

# TODO update the JSON string below
json = "{}"
# create an instance of PartialWriteBody from a JSON string
partial_write_body_instance = PartialWriteBody.from_json(json)
# print the JSON string representation of the object
print(PartialWriteBody.to_json())

# convert the object into a dict
partial_write_body_dict = partial_write_body_instance.to_dict()
# create an instance of PartialWriteBody from a dict
partial_write_body_from_dict = PartialWriteBody.from_dict(partial_write_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


