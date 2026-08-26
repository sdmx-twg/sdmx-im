# The SDMX Information Model

SDMX provides a way of modelling statistical data, and defines the set
of metadata constructs used for this purpose. Because SDMX specifies a
number of transmission formats for expressing data and structural
metadata, the model is used as a mechanism for guaranteeing that
transformation between the different formats is lossless. In this sense,
all of the formats are syntax-bound expressions of the common
information model.

SDMX recognizes that statistical data is structured; in SDMX this
structure is termed a Data Structure Definition. "Data sets" are made up
of one or more lower-level "groups", based on their degrees of
similarity. Each group is in turn comprised of one or more "series" of
data. Each series or section has a "key" - values for each of a cluster
of concepts, also called "dimensions" - which identifies it, and one
or more "observations", which typically combine the time of the
observation, and the value of the observation (e.g., measurement).
Additionally, metadata may be attached at any level of this structure as
descriptive "attributes". Code lists (enumerations) and other patterns
for representation of data and metadata are also modelled.

There is some similarity between "cube" structures commonly used to
process statistical data, and the Data Structure Definition idea in the
SDMX Information Model. It is important to note that the data as
structured according to the SDMX Information Model is optimized for
exchange, potentially with partners who may have no ability to process a
"cube" of data coming from complex statistical systems. SDMX time series
can be understood as "slices" of the cube. Such a slice is identified by
its key. A "series" key consists of the values for all dimensions
specified by the key family except time. Thus, it is possible to
reconstruct and describe data cubes from SDMX-structured data, and to
exchange such databases using the interfaces and formats provided for
that purpose in the standard. Additional objects such as hierarchical
code lists, constraints and structure maps make it possible to more
fully model the structure of cubes.

The information model also provides a view of reference metadata: a
mechanism for referencing the meaningful "objects" within the SDMX view
of statistical exchange processes (data providers, structures,
provisioning agreements, dataflows, metadata flows, etc.) to which
metadata is attached; a mechanism for describing a set of meaningful
concepts, of organizing them into a presentational structure, and of
indicating how their values are represented. This is based on a simple,
hierarchical view of reference metadata which is common to many metadata
systems and classification/categorization schemes. SDMX provides a model
(and XML and JSON formats) for both describing reference metadata
structures, and of reporting reference metadata according to those
structures.

Version 2.0/2.1 introduced support for metadata related to the process
aspects of statistical exchange. A step-by-step process can be modelled;
information about who is providing data and reference metadata and how
they are providing it can be expressed; and the technical aspects of
service-level agreements (and similar types of provisioning agreements)
can be represented.

Support for the Validation and Transformation Language (VTL) in the SDMX
Information Model was introduced in the July 2020 revision of 2.1 and is
retained in version 3.0 with minimal changes. This allows reusable VTL
'programs' (a cohesive set of transformation statements designed to be
executed together) and their associated constructs such as validation
rulesets and user-defined operators to be managed and exchanged as SDMX
structural metadata. Mappings between objects such as data sets
referenced in VTL programs and the actual SDMX artefacts to which they
relate is essential when it comes to actually executing programs, and
this information can also be defined. Chapter 7 has more information on
VTL and its integration with SDMX.

A full UML conceptual design of the information model is set out in
[Section 2 of the Technical Specifications](../../information_model/information_model/0_Introduction.md).