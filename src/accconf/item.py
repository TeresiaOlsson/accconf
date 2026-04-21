"""Data models for configuration."""

import logging

logger = logging.getLogger(__name__)

from typing import Any
from pydantic import BaseModel, Field, ConfigDict, model_validator

class BaseItem(BaseModel):
    """Base class for all items."""

    model_config = ConfigDict(extra="allow")

    name: str = Field(description="Name for the instance.")

    # Attributes for to object creation
    class_name: str = Field(description="Python class for creation")
    args: list[Any] = Field(default_factory=list)
    kwargs: dict[str, Any] = Field(default_factory=dict)

    # Attributes for validation
    # validate: bool = Field(default=False)
    # validation_model: str | None = None

    # TODO: add validation of name
    # TODO: add validation logic

    def to_dict(self) -> dict[str,Any]:
        data = self.model_dump(by_alias=True)
        return data

# class ObjectItem(BaseItem):
#     """Class to hold configuration for objects that can be created."""

#     model_config = ConfigDict(extra="allow")

#     class_name: str = Field(alias="class")
#     args: list[Any] = Field(default_factory=list)
#     kwargs: dict[str, Any] = Field(default_factory=dict)

#     @model_validator(mode="before")
#     @classmethod
#     def collect_extra_fields_into_kwargs(cls, data: Any) -> Any:
#         """Puts all the extra fields into the kwargs dict."""

#         if not isinstance(data, dict):
#             return data

#         data = dict(data)
#         kwargs = dict(data.get("kwargs") or {})

#         # Reserved fields
#         reserved = {
#             name
#             for name in cls.model_fields
#         } | {
#             field.alias
#             for field in cls.model_fields.values()
#             if field.alias is not None
#         }

#         for key in list(data.keys()):
#             if key not in reserved:
#                 kwargs[key] = data.pop(key)

#         data["kwargs"] = kwargs
#         return data


# class MetadataItem(BaseItem):
#     """Class to hold metadata information."""

#     class_name: str = Field(alias="class")
#     data: dict[str, Any] = Field(default_factory=dict)

#     @model_validator(mode="before")
#     @classmethod
#     def collect_extra_fields_into_data(cls, data: Any) -> Any:
#         if not isinstance(data, dict):
#             return data

#         data = dict(data)
#         payload = dict(data.get("data") or {})

#         reserved = {
#             name for name in cls.model_fields
#         } | {
#             field.alias
#             for field in cls.model_fields.values()
#             if field.alias is not None
#         }

#         for key in list(data.keys()):
#             if key not in reserved:
#                 payload[key] = data.pop(key)

#         data["data"] = payload
#         return data