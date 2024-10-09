from __future__ import annotations as _annotations

"""
Profile: http://hl7.org/fhir/StructureDefinition/CompartmentDefinition
Release: R4B
Version: 4.3.0
Build ID: c475c22
Last updated: 2022-05-28T12:47:40.239+10:00
"""
import typing

from pydantic import Field

from . import backboneelement, domainresource, fhirtypes


class CompartmentDefinition(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Compartment Definition for a resource.
    A compartment definition that defines how resources are accessed on a
    server.
    """

    __resource_type__ = "CompartmentDefinition"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Patient | Encounter | RelatedPerson | Practitioner | Device",
        description="Which compartment this definition describes.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": [
                "Patient",
                "Encounter",
                "RelatedPerson",
                "Practitioner",
                "Device",
            ],
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    contact: typing.List[fhirtypes.ContactDetailType] | None = Field(  # type: ignore
        None,
        alias="contact",
        title="Contact details for the publisher",
        description=(
            "Contact details to assist a user in finding and communicating with the"
            " publisher."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    date: fhirtypes.DateTimeType | None = Field(  # type: ignore
        None,
        alias="date",
        title="Date last changed",
        description=(
            "The date  (and optionally time) when the compartment definition was "
            "published. The date must change when the business version changes and "
            "it must change if the status code changes. In addition, it should "
            "change when the substantive content of the compartment definition "
            "changes."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_date", title="Extension field for ``date``."
    )

    description: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="description",
        title="Natural language description of the compartment definition",
        description=(
            "A free text natural language description of the compartment definition"
            " from a consumer's perspective."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_description", title="Extension field for ``description``."
    )

    experimental: bool | None = Field(  # type: ignore
        None,
        alias="experimental",
        title="For testing purposes, not real usage",
        description=(
            "A Boolean value to indicate that this compartment definition is "
            "authored for testing purposes (or education/evaluation/marketing) and "
            "is not intended to be used for genuine usage."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    experimental__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_experimental", title="Extension field for ``experimental``."
    )

    name: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="name",
        title="Name for this compartment definition (computer friendly)",
        description=(
            "A natural language name identifying the compartment definition. This "
            "name should be usable as an identifier for the module by machine "
            "processing applications such as code generation."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_name", title="Extension field for ``name``."
    )

    publisher: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="publisher",
        title="Name of the publisher (organization or individual)",
        description=(
            "The name of the organization or individual that published the "
            "compartment definition."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    publisher__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_publisher", title="Extension field for ``publisher``."
    )

    purpose: fhirtypes.MarkdownType | None = Field(  # type: ignore
        None,
        alias="purpose",
        title="Why this compartment definition is defined",
        description=(
            "Explanation of why this compartment definition is needed and why it "
            "has been designed as it has."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    purpose__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_purpose", title="Extension field for ``purpose``."
    )

    resource: typing.List[fhirtypes.CompartmentDefinitionResourceType] | None = Field(  # type: ignore
        None,
        alias="resource",
        title="How a resource is related to the compartment",
        description="Information about how a resource is related to the compartment.",
        json_schema_extra={
            "element_property": True,
        },
    )

    search: bool | None = Field(  # type: ignore
        None,
        alias="search",
        title="Whether the search syntax is supported",
        description="Whether the search syntax is supported,.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    search__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_search", title="Extension field for ``search``."
    )

    status: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="status",
        title="draft | active | retired | unknown",
        description=(
            "The status of this compartment definition. Enables tracking the life-"
            "cycle of the content."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
            # note: Enum values can be used in validation,
            # but use in your own responsibilities, read official FHIR documentation.
            "enum_values": ["draft", "active", "retired", "unknown"],
        },
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_status", title="Extension field for ``status``."
    )

    url: fhirtypes.UriType | None = Field(  # type: ignore
        None,
        alias="url",
        title=(
            "Canonical identifier for this compartment definition, represented as a"
            " URI (globally unique)"
        ),
        description=(
            "An absolute URI that is used to identify this compartment definition "
            "when it is referenced in a specification, model, design or an "
            "instance; also called its canonical identifier. This SHOULD be "
            "globally unique and SHOULD be a literal address at which at which an "
            "authoritative instance of this compartment definition is (or will be) "
            "published. This URL can be the target of a canonical reference. It "
            "SHALL remain the same when the compartment definition is stored on "
            "different servers."
        ),
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    url__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_url", title="Extension field for ``url``."
    )

    useContext: typing.List[fhirtypes.UsageContextType] | None = Field(  # type: ignore
        None,
        alias="useContext",
        title="The context that the content is intended to support",
        description=(
            "The content was developed with a focus and intent of supporting the "
            "contexts that are listed. These contexts may be general categories "
            "(gender, age, ...) or may be references to specific programs "
            "(insurance plans, studies, ...) and may be used to assist with "
            "indexing and searching for appropriate compartment definition "
            "instances."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )

    version: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="version",
        title="Business version of the compartment definition",
        description=(
            "The identifier that is used to identify this version of the "
            "compartment definition when it is referenced in a specification, "
            "model, design or instance. This is an arbitrary value managed by the "
            "compartment definition author and is not expected to be globally "
            "unique. For example, it might be a timestamp (e.g. yyyymmdd) if a "
            "managed version is not available. There is also no expectation that "
            "versions can be placed in a lexicographical sequence."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    version__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_version", title="Extension field for ``version``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompartmentDefinition`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "url",
            "version",
            "name",
            "status",
            "experimental",
            "date",
            "publisher",
            "contact",
            "description",
            "useContext",
            "purpose",
            "code",
            "search",
            "resource",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [
            ("code", "code__ext"),
            ("name", "name__ext"),
            ("search", "search__ext"),
            ("status", "status__ext"),
            ("url", "url__ext"),
        ]
        return required_fields


class CompartmentDefinitionResource(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    How a resource is related to the compartment.
    Information about how a resource is related to the compartment.
    """

    __resource_type__ = "CompartmentDefinitionResource"

    code: fhirtypes.CodeType | None = Field(  # type: ignore
        None,
        alias="code",
        title="Name of resource type",
        description="The name of a resource supported by the server.",
        json_schema_extra={
            "element_property": True,
            "element_required": True,
        },
    )
    code__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_code", title="Extension field for ``code``."
    )

    documentation: fhirtypes.StringType | None = Field(  # type: ignore
        None,
        alias="documentation",
        title="Additional documentation about the resource and compartment",
        description=None,
        json_schema_extra={
            "element_property": True,
        },
    )
    documentation__ext: fhirtypes.FHIRPrimitiveExtensionType | None = Field(  # type: ignore
        None, alias="_documentation", title="Extension field for ``documentation``."
    )

    param: typing.List[fhirtypes.StringType | None] | None = Field(  # type: ignore
        None,
        alias="param",
        title="Search Parameter Name, or chained parameters",
        description=(
            "The name of a search parameter that represents the link to the "
            "compartment. More than one may be listed because a resource may be "
            "linked to a compartment in more than one way,."
        ),
        json_schema_extra={
            "element_property": True,
        },
    )
    param__ext: typing.List[fhirtypes.FHIRPrimitiveExtensionType | None] | None = Field(  # type: ignore
        None, alias="_param", title="Extension field for ``param``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``CompartmentDefinitionResource`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "extension",
            "modifierExtension",
            "code",
            "param",
            "documentation",
        ]

    def get_required_fields(self) -> typing.List[typing.Tuple[str, str]]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("code", "code__ext")]
        return required_fields
