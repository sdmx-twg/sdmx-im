

### SDMX-ML

SDMX-ML is the XML transmission format specification for exchanging
structural metadata, data and reference metadata, and interacting with
SDMX registry services. It is designed as a general-purpose format for
all automation and data / metadata exchange tasks, and provides the most
complete coverage.

There are four distinct types of message:

1. **Structure Definition:** For the exchange of structural metadata. A
    SDMX-ML structure message can carry details of any number and
    combination of structural metadata artefacts like DSDs, code lists
    and constraints.

2. **Structure-specific Data:** For the exchange of data. This format is
    specific to the Data Structure Definitions of the data sets (in
    other terms, it is DSD-specific) and is created by following
    mappings between the metadata constructs defined in the Structure
    Definition message and the technical specification of the format. It
    supports the exchange of large data sets in XML format, provides
    strict validation of conformance with the DSD using a generic XML
    parser, and supports the transmission of partial data sets
    (incremental updates) as well as whole data sets.

    Many XML tools and technologies have expectations about the functions
    performed by an XML schema, one of which is a very direct relationship
    between the XML constructs described in the XML schema and the tagged
    data in the XML instance. Strong data typing is also considered
    normal, supporting full validation of the tagged data. These message
    types are designed to support validation and other expected XML schema
    functions.

3. **Generic Metadata:** For the exchange of reference metadata sets.
    'Generic' means the XML elements and XML attributes are the same
    regardless of the metadata set.

4. **Registry:** All of the possible interactions with the SDMX registry
    services are supported using SDMX-ML interfaces and REST API calls.
    Submission of structural metadata content, data / metadata
    registrations and subscriptions is performed by a synchronous
    exchange of documents -- a "request" message answered by a
    "response" message.

### SDMX-JSON

SDMX-JSON is the JSON transmission format specification for exchanging
structural metadata, data and reference metadata. It provides an
alternative to SDMX-ML and is most suited to applications like web data
dissemination.

SDMX-JSON messages serve the same function as those of the XML formats
but have a different structure. For data, an important distinction is
that they carry both component codes and labels which provides all the
information needed to display the content in a single JSON response. The
XML Structure-specific Data format by contrast carries only code IDs
thus requiring applications obtain and hold structural metadata about
the data set in order to display the content in human-readable form.

SDMX-JSON does not include messages for subscription / notification or
registration registry services - SDMX-ML must be used for those
purposes.

There are three distinct message types:

1. **Structure:** For the exchange structural metadata. SDMX-JSON
    structure messages follow the same principles as for SDMX-ML in that
    a single message can transmit any number and combination of
    structural metadata artefacts. While the SDMX-ML and SDMX-JSON
    messages are structured differently, it is possible to freely
    convert between them.
2. **Data:** For the exchange of data. Unlike SDMX-ML, the structure of a
    SDMX-JSON data message is not specific to the DSDs of the data sets
    so schema validation will not check for compliance of the data with
    the DSDs.
3. **Metadata:** For the exchange of reference metadata sets.

### SDMX-CSV

SDMX-CSV is the CSV transmission format specification for exchanging
data and reference metadata only.

SDMX-CSV provides a simple columnar format for data and metadata that
can be readily created and interpreted by standard software tools such
as Microsoft Excel. Nevertheless, data and metadata can still be
converted between the CSV and the JSON / XML formats without loss.

There are two distinct message types:

1. **Data:** For the exchange of data. Like SDMX-JSON, SDMX-CSV can
    include both code IDs and labels which is helpful when using the
    data to create human readable charts and dashboards.
2. **Metadata:** For the exchange of reference metadata sets.

### Formats and Messages Deprecated in Version 3.0

The following formats and messages have been deprecated in version 3.0
to simplify, modernise and rationalise the standard.

- SDMX-EDI
- SDMX-ML 1.0/2.0 Generic (time-series) data message
- SDMX-ML 1.0/2.0 Compact (time-series) data message
- SDMX-ML 1.0/2.0 Utility (time-series) data message
- SDMX-ML 1.0/2.0 Cross-Sectional data message
- SDMX-ML 2.1 Generic (Time Series) data messages (for observations,
    time-series and cross-sectional data)
- SDMX-ML 2.1 Structure Specific Time Series data message

The following messages were deprecated in version 3.0 as a consequence
of the deprecation of the SOAP web services:

- SDMX-ML Query messages
- SDMX-ML Submit Structure Request messages