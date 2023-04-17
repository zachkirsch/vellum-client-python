# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from .document_to_document_index import DocumentToDocumentIndex
from .processing_state_enum import ProcessingStateEnum
from .status_enum import StatusEnum


class SlimDocument(pydantic.BaseModel):
    id: str = pydantic.Field(description=("Vellum-generated ID that uniquely identifies this document.\n"))
    external_id: typing.Optional[str] = pydantic.Field(
        description=("The external ID that was originally provided when uploading the document.\n")
    )
    last_uploaded_at: str = pydantic.Field(
        description=("A timestamp representing when this document was most recently uploaded.\n")
    )
    label: str = pydantic.Field(description=("Human-friendly name for this document.\n"))
    processing_state: typing.Optional[ProcessingStateEnum] = pydantic.Field(
        description=("The current processing state of the document\n")
    )
    status: typing.Optional[StatusEnum] = pydantic.Field(description=("The document's current status.\n"))
    keywords: typing.Optional[typing.List[str]] = pydantic.Field(
        description=(
            "A list of keywords associated with this document. Originally provided when uploading the document.\n"
        )
    )
    document_to_document_indexes: typing.List[DocumentToDocumentIndex]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        json_encoders = {dt.datetime: serialize_datetime}
