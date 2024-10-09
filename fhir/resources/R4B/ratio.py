from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/Ratio
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
from pydantic import Field

from . import element, fhirtypes


class Ratio(element.Element):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    A ratio of two Quantity values - a numerator and a denominator.
    A relationship of two Quantity values - expressed as a numerator and a
    denominator.
    """

    __resource_type__ = "Ratio"

    denominator: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="denominator",
        title="Denominator value",
        description="The value of the denominator.",
        json_schema_extra={
            "element_property": True,
        },
    )

    numerator: fhirtypes.QuantityType | None = Field(  # type: ignore
        None,
        alias="numerator",
        title="Numerator value",
        description="The value of the numerator.",
        json_schema_extra={
            "element_property": True,
        },
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Ratio`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "numerator", "denominator"]
