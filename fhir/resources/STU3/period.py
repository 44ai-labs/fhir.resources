from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Period
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
from pydantic import Field

from . import element, fhirtypes


class Period(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Time range defined by start and end date/time.
    A time period defined by a start and end date and optionally time.
    """

    __resource_type__ = "Period"

    end: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="end",
        title="End time with inclusive boundary, if not ongoing",
        description=(
            "The end of the period. If the end of the period is missing, it means "
            "that the period is ongoing. The start may be in the past, and the end "
            "date in the future, which means that period is expected/planned to end"
            " at that time."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    end__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_end", title="Extension field for ``end``."
    )

    start: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="start",
        title="Starting time with inclusive boundary",
        description="The start of the period. The boundary is inclusive.",
        json_schema_extra={
            "element_property": True,
        },
    )
    start__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_start", title="Extension field for ``start``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Period`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "start", "end"]
