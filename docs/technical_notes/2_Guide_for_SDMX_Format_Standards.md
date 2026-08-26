# Guide for SDMX Format Standards

## Introduction

This guide exists to provide information to implementers of the SDMX
format standards – SDMX-ML, SDMX-JSON and SDMX-CSV – that are concerned
with data, i.e., Data Structure Definitions and Data Sets. This section
is intended to provide information that will help users of SDMX
understand and implement the standards. It is not normative, and it does
not provide any rules for the use of the standards, such as those found
in [SDMX-ML: Schema and Documentation](../../ml/index.md).

## SDMX Information Model for Format Implementers

### Introduction

The purpose of this sub-section is to provide an introduction to the
SDMX-IM relating to Data Structure Definitions and Data Sets for those
whose primary interest is in the use of the XML, JSON or CSV formats.
For those wishing to have a deeper understanding of the Information
Model, the full SDMX-IM document, and other sections in this guide
provide a more in-depth view, along with UML diagrams and supporting
explanation. For those who are unfamiliar with DSDs, an appendix to the
SDMX-IM provides a tutorial which may serve as a useful introduction.

The SDMX-IM is used to describe the basic data and metadata structures
used in all of the SDMX data formats. The Information Model concerns
itself with statistical data and its structural metadata, and that is
what is described here. Both structural metadata and data have some
additional metadata in common, related to their management and
administration. These aspects of the data model are not addressed in
this section and covered elsewhere in this guide or in the full SDMX-IM
document.

Note that in the descriptions below, text in courier and italics are the
names used in the information model (e.g., `DataSet`).

## SDMX Formats: Expressive Capabilities and Function

SDMX offers several equivalent formats for describing data and
structural metadata, optimized for use in different applications.
Although all of these formats are derived directly from the SDMX-IM, and
are thus equivalent, the syntaxes used to express the model place some
restrictions on their use. Also, different optimizations provide
different capabilities. This section describes these differences and
provides some rules for applications which may need to support more than
one SDMX format or syntax. This section is constrained to the Data
Structure Definition and the `DataSet`.

### Format Optimizations and Differences

The following section provides a brief overview of the differences
between the various SDMX formats.

Version 2.0 was characterised by 4 data messages, each with a distinct
format: Generic, Compact, Cross-Sectional and Utility. Because of the
design, data in some formats could not always be related to another
format. In version 2.1, this issue has been addressed by merging some
formats and eliminating others. As a result, in SDMX 2.1 there were just
two types of data formats: `GenericData` and `StructureSpecificData`
(i.e., specific to one Data Structure Definition). As of SDMX 3.0, based
also on the real-life usage of 2.1 XML formats but also the new formats
introduced (JSON and CSV), only one XML format remains, i.e.,
`StructureSpecificData`. Furthermore, the time specific sub-formats have
also been deprecated due to the lack of usage.

SDMX-JSON and SDMX-CSV feature also only one flavour, each. It should be
noted, though, that both XML and JSON messages allow for series oriented
as well as flat representations.

#### Structure Definition

- The SDMX-ML Structure Message is currently the main way of modelling
    a DSD. The SDMX-JSON version follows the same principles, while the
    SDMX-CSV does not support structures, yet.
- The SDMX-ML Structure Message allows for the structures on which a
    Data Structure Definition depends – that is, codelists and concepts
    – to be either included in the message or to be referenced by the
    message containing the data structure definition. XML syntax is
    designed to leverage URIs and other Internet-based referencing
    mechanisms, and these are used in the SDMX-ML message. This option
    is also available in SDMX-JSON. The latter, though, further supports
    conveying data with some structural metadata within a single
    message.
- All structures can be inserted, replaced or deleted, unless
    structural dependencies are not respected.

#### Validation

- The SDMX-ML structure specific messages will allow validation of XML
    syntax and data typing to be performed with a generic XML parser and
    enforce agreement between the structural definition and the data to
    a moderate degree with the same tool.
- Similarly, the SDMX-JSON message can be validated using JSON Schema
    and hence may also be generically parsed and validated.
- The SDMX-CSV format cannot be validated by generic tools.

#### Update and Delete Messages

- All data messages allow for both append/replace/delete messages.
- These messages allow also transmitting only data or only
    documentation (i.e., Attribute values without Observation values).

#### Character Encodings

All formats use the UTF-8 encoding. The SDMX-CSV may use a different
encoding if this is reported properly in the mime type of a web service
response.

#### Data Typing

The XML syntax and JSON syntax have similar data-typing mechanisms.
Hence, there is no need for conventions in order to allow transition
from one format to another, like those required for EDIFACT in SDMX 2.1.
On the other hand, JSON schema has a simpler set of data types (as
explained in Section [Information Model, paragraph “Representation Constructs”](../../information_model/information_model/2_SDMX_Base_Package.md#representation-constructs))
but complements its data types with a fixed set of formats or regular
expressions. In addition, the JSON schema has also types that are not
natively supported in XML schema and need to be implemented as complex
types in the latter. The section below provides examples of those cases
that are not natively supported by either the XML or JSON data types.
More details on the data mapping between XML and JSON schemas are also
explained in section [“Data Types”](./3_General_Notes_for_Implementers.md#data-types).

## SDMX Best Practices

### Reporting and Dissemination Guidelines

#### Central Institutions and Their Role in Statistical Data Exchanges

Central institutions are the organisations to which other partner
institutions "report" statistics. These statistics are used by central
institutions either to compile aggregates and/or they are put together
and made available in a uniform manner (e.g., on-line or on a CD-ROM or
through file transfers). Therefore, central institutions receive data
from other institutions and, usually, they also "disseminate" data to
individual and/or institutions for end-use. Within a country, a NSI or a
national central bank (NCB) plays, of course, a central institution role
as it collects data from other entities and it disseminates statistical
information to end users. In SDMX the role of central institution is
very important: every statistical message is based on underlying
structural definitions (statistical concepts, code lists, DSDs) which
have been devised by a particular agency, usually a central institution.
Such an institution plays the role of the reference "structural
definitions maintenance agency" for the corresponding messages which are
exchanged. Of course, two institutions could exchange data
using/referring to structural information devised by a third
institution.

Central institutions can play a double role:

- collecting and further disseminating statistics;
- devising structural definitions for use in data exchanges.

#### Defining Data Structure Definitions (DSDs)

The following guidelines are suggested for building a DSD. However, it
is expected that these guidelines will be considered by central
institutions when devising new DSDs.

##### Dimensions, Attributes and Codelists

- **Avoid dimensions that are not appropriate for all the series in
    the data structure definition**. If some dimensions are not
    applicable (this is evident from the need to have a code in a code
    list which is marked as "not applicable", "not relevant" or "total")
    for some series then consider moving these series to a new data
    structure definition in which these dimensions are dropped from the
    key structure. This is a judgement call as it is sometimes difficult
    to achieve this without increasing considerably the number of DSDs.
- **Devise DSDs with a small number of Dimensions for public viewing
    of data**. A DSD with the number dimensions in excess 6 or 7 is
    often difficult for non-specialist users to understand. In these
    cases, it is better to have a larger number of DSDs with smaller
    "cubes" of data, or to eliminate dimensions and aggregate the data
    at a higher level. Dissemination of data on the web is a growing use
    case for the SDMX standards: the differentiation of observations by
    dimensionality, which are necessary for statisticians and
    economists, are often obscure to public consumers who may not always
    understand the semantic of the differentiation.
- **Avoid composite dimensions**. Each dimension should correspond to
    a single characteristic of the data, not to a combination of
    characteristics.
- Consider the inclusion of the following attributes. Once the key
    structure of a data structure definition has been decided, then the
    set of (preferably mandatory) attributes of this data structure
    definition has to be defined. In general, some statistical concepts
    are deemed necessary across all Data Structure Definitions to
    qualify the contained information. Examples of these are:
    - A descriptive title for the series (this is most useful for
      dissemination of data for viewing e.g., on the web).
    - Collection (e.g., end of period, averaged or summed over period).
    - Unit (e.g., currency of denomination).
    - Unit multiplier (e.g., expressed in millions).
    - Availability (which institutions can a series become available to).
    - Decimals (i.e., number of decimal digits used in numerical observations).
    - Observation Status (e.g., estimate, provisional, normal).

Moreover, additional attributes may be considered as mandatory when a
specific data structure definition is defined.

- **Avoid creating a new code list where one already exists**. It is
    highly recommended that structural definitions and code lists be
    consistent with internationally agreed standard methodologies,
    wherever they exist, e.g., System of National Accounts 1993; Balance
    of Payments Manual, Fifth Edition; Monetary and Financial Statistics
    Manual; Government Finance Statistics Manual, etc. When setting-up a
    new data exchange, the following order of priority is suggested when
    considering the use of code lists:
    - international standard code lists;
    - international code lists supplemented by other international and/or regional institutions;
    - standardised lists used already by international institutions;
    - new code lists agreed between two international or regional institutions;
    - new code lists which extend existing code lists, by adding only missing codes;
    - new specific code lists.

The same code list can be used for several statistical concepts, within
a data structure definition or across DSDs. Note that SDMX has
recognised that these classifications are often quite large and the
usage of codes in any one DSD is only a small extract of the full code
list. In this version of the standard, it is possible to exchange and
disseminate a **partial code list** which is extracted from the full
code list and which supports the dimension values valid for a particular
DSD.

##### Data Structure Definition Structure

- The following items have to be specified by a structural definitions
    maintenance agency when defining a new data structure definition:
- Data structure definition (DSD) identification:
    - DSD identifier
    - DSD name
- A list of metadata concepts assigned as dimensions of the data
    structure definition. For each:
    - (statistical) concept identifier
    - code list identifier (id, version, maintenance agency) if the
        representation is coded
- A list of (statistical) concepts assigned as attributes for the data
    structure definition. For each:
    - (statistical) concept identifier
    - code list identifier if the concept is coded
    - usage: mandatory, optional
    - relationship to dimensions and measures
    - maximum text length for the uncoded concepts
    - maximum code length for the coded concepts
- A list of the code lists used in the data structure definition. For
    each:
    - code list identifier
    - code list name
    - code values and descriptions
- Definition of Dataflow. Two (or more) partners performing data
    exchanges in a certain context need to agree on:
    - the list of dataset identifiers they will be using;
    - for each Dataflow:
        - its content (e.g., by Constraints) and description
        - the relevant DSD that defines the structure of the data reported
            or disseminated according the Dataflow

#### Exchanging Attributes

##### Attributes on series and group levels

Static properties.

- Upon creation of a series the sender has to provide to the receiver
    values for all mandatory attributes. In case they are available,
    values for conditional attributes should also be provided. Whereas
    initially this information may be provided by means other than
    SDMX-ML/JSON/CSV messages (e.g., paper, telephone) it is expected
    that partner institutions will be in a position to provide this
    information in the available formats over time.
- A centre may agree with its data exchange partners special
    procedures for authorising the setting of attributes' initial
    values.

Communication of changes to the centre.

- Following the creation of a series, the attribute values do not have
    to be reported again by senders, as long as they do not change.
- Whenever changes in attribute values for a series (or group) occur,
    the reporting institutions should report either all attribute values
    again (this is the recommended option) or only the attribute values
    which have changed. This applies both to the mandatory and the
    conditional attributes. For example, if a previously reported value
    for a conditional attribute is no longer valid, this has to be
    reported to the centre.
- A centre may agree with its data exchange partners special
    procedures for authorising modifications in the attribute values.
- Communication of observation level attributes "observation status",
    "observation confidentiality", "observation pre-break" is
    recommended.
- Whenever an observation is exchanged, the corresponding observation
    status is recommended to also be exchanged attached to the
    observation, regardless of whether it has changed or not since the
    previous data exchange.
- If the "observation status" changes and the observation remains
    unchanged, both components would have to be reported (unless the
    observation is deleted).

    For Data Structure Definitions having also the observation level
    attributes "observation confidentiality" and "observation pre-break"
    defined, this rule applies to these attributes as well: if an
    institution receives from another institution an observation with an
    observation status attribute only attached, this means that the
    associated observation confidentiality and pre-break observation
    attributes either never existed or from now they do not have a value for
    this observation.

### Best Practices for Batch Data Exchange

#### Introduction

Batch data exchange is the exchange and maintenance of entire databases
between counterparties. It is an activity that often employs SDMX-CSV
format, and might also use the SDMX-ML dataset. The following points
apply equally to both formats.

#### Positioning of the Dimension "Frequency"

In SDMX 3.0, the "frequency" dimension is not special in the data
structure definition. Many central institutions devising structural
definitions have decided to assign to this dimension the first position
in the key structure. Nevertheless, a standard role (i.e., that of
‘Frequency’) may facilitate the easy identification of this dimension.
This is necessary to frequency's crucial role in several database
systems and in attaching attributes at the "sibling" group level.

#### Identification of Data Structure Definitions (DSDs)

In order to facilitate the easy and immediate recognition of the
structural definition maintenance agency that defined a data structure
definition, some central institutions devising structural definitions
use the first characters of the data structure definition identifiers to
identify their institution: e.g., BIS\_EER, EUROSTAT\_BOP\_01,
ECB\_BOP1, etc. Nevertheless, using the `AgencyId` may disambiguate any
Artefact in a more efficient and machine readable way.

#### Identification of the Dataflows

In order to facilitate the easy and immediate recognition of the
institution administrating a Dataflow, some central institutions prefer
to use the first characters of the Dataflow identifiers to identify
their institution: e.g. `BIS_EER`, `ECB_BOP1`, `ECB_BOP1`, etc.
Nevertheless, using the `AgencyId` may disambiguate any Artefact in a more
efficient and machine readable way.

The statistical information in SDMX is broken down into two fundamental
parts – structural metadata (comprising the `DataStructureDefinition`, and
associated `Concepts` and `Codelists`) – see Framework for Standards – and
observational data (the `DataSet`). This is an important distinction, with
specific terminology associated with each part. Data, which is typically
a set of numeric observations at specific points in time, is organised
into data sets (`DataSet`). These data sets are structured according to a
specific `DataStructureDefinition` and are described in the `Dataflow` (via
`Constraints`). The `DataStructureDefinition` describes the metadata that
allows an understanding of what is expressed in the `DataSet`, whilst the
`Dataflow` provides the identifier and other important information (such
as the periodicity of reporting) that is common to all its Components.

Note that the role of the `Dataflow` and `DataSet` is very specific in the
model, and the terminology used may not be the same as used in all
organisations, and specifically the term `DataSet` is used differently in
SDMX than in GESMES/TS. Essentially the GESMES/TS term "Data Set" is, in
SDMX, the "Dataflow" whilst the term "Data Set" in SDMX is used to
describe the "container" for an instance of the data.

#### Special Issues

##### "Frequency" related issues

- **Special frequencies.** The issue of data collected at special
    (regular or irregular) intervals at a lower than daily frequency
    (e.g., 24 or 36 or 48 observations per year, on irregular days
    during the year) is not extensively discussed here. However, for
    data exchange purposes:
    - such data can be mapped into a series with daily frequency; this
        daily series will only hold observations for those days on which the
        measured event takes place;
    - if the collection intervals are regular, additional values to the
        existing frequency code list(s) could be added in the future.
- **Tick data.** The issue of data collected at irregular intervals
    at a higher than daily frequency (e.g., tick-by-tick data) is not
    discussed here either.
