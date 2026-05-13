# Dependencies on SDMX content-oriented guidelines

The technical standards proposed here are designed so that they can be
used in conjunction with other SDMX guidelines which are more closely
tied to the content and semantics of statistical data exchange. The SDMX
Information Model works equally well with any statistical concept, but
to encourage interoperability, it is also necessary to standardize and
harmonize the use of specific concepts and terminology. To achieve this
goal, SDMX creates and maintains guidelines for cross-domain concepts,
terminology, and structural definitions. There are three major parts to
this effort.

## Cross-Domain Concepts

The SDMX Cross-Domain Concepts is a content guideline concerning
concepts which are used across statistical domains. This list is
expected to grow and to be subject to revision as SDMX is used in a
growing number of domains. The use of the SDMX Cross-Domain Concepts,
where appropriate, provides a framework to further promote
interoperability among organisations using the technical standards
presented here. The harmonization of statistical concepts includes not
only the definitions of the concepts, and their names, but also, where
appropriate, their representation with standard code lists, and the role
they play within data structure definitions and metadata structure
definitions.

The intent of this guideline is two-fold: to provide a core set of
concepts which can be used to structure statistical data and metadata,
to promote interoperability between systems ("structural metadata", as
described above); and to promote the exchange of metadata more widely,
with a set of harmonized concept names and definitions for other types
of metadata ("reference metadata", as defined above.)

## Metadata Common Vocabulary

The Metadata Common Vocabulary is an SDMX guideline which provides
definition of terms to be used for the comparison and mapping of
terminology found in data structure definitions and in other aspects of
statistical metadata management. Essentially, it provides ISO-compliant
definitions for a wide range of statistical terms, which may be used
directly, or against which other terminology systems may be mapped. This
set of terms is inclusive of the terminology used within the SDMX
Technical Standards.

The MCV provides definitions for terms on which the SDMX Cross-Domain
Metadata Concepts work is built.

## Statistical Subject-Matter Domains

The Statistical Subject-Matter Domains is a listing of the breadth of
statistical information for the purposes of organizing widespread
statistical exchange and categorization. It acts as a standard scheme
against which the categorization schemes of various counterparties can
be mapped, to facilitate interoperable data and metadata exchange. It
serves another useful purpose, however, which is to allow an
organization of corresponding "domain groups", each of which could
define standard data structure definitions, concepts, etc. within their
domains. Such groups already exist within the international community.
SDMX would use the Statistical Subject-Matter Domains list to facilitate
the efforts of these groups to develop the kinds of content standards
which could support the interoperation of SDMX-conformant technical
systems within and across statistical domains. The organisation of the
content of such schemes is supported in SDMX as a Category Scheme.

SDMX Statistical Subject-Matter Domains will be listed and maintained by
the SDMX Initiative and will be subject to adjustment.

## SDMX Concept Roles

These guidelines define the standard set of SDMX Concept Roles and their
use. This set of standard SDMX Concepts are implemented as a
cross-domain Concept Scheme that defines the set of concept roles and
gives examples on concept role implementation in SDMX 2.0, 2.1 and 3.0.
A concept role gives a particular context to a concept for easy and
systematic interpretation by machine processing and visualization tools.

For example, the concepts `REPORTING_AREA` and `COUNTERPART_AREA` are
different concepts but they are both geographical characteristics,
therefore they can be associated with the same concept role ID: `GEO`.
This allows visualization systems to interpret these concepts as
geographical data in order to generate maps. The implementation of
concept roles is different in versions 2.0 and 2.1/3.0 of the SDMX
technical standard. Specifically for SDMX 3.0, this set of roles is
considered a normative list that must be interpreted in the same way by
all organisations. Additional roles may be provided via the standard
roles' mechanism in SDMX 3.0, i.e., via Concept Schemes; the semantics
of these roles have to be agreed bilateraly in data exchanges. The
Concept Roles are available as an SDMX Concept Scheme on the SDMX Global
Registry.
