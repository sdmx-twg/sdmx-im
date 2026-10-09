# Validation and Transformation Language (VTL)

## Introduction

The Validation and Transformation Language (VTL) supports the definition
of Transformations, which are algorithms to calculate new data starting
from already existing ones[^1]. The purpose of the VTL in the SDMX
context is to enable the:

- definition of validation and transformation algorithms, in order to
    specify how to calculate new data from existing ones;
- exchange of the definition of VTL algorithms, also together the
    definition of the data structures of the involved data (for example,
    exchange the data structures of a reporting framework together with
    the validation rules to be applied, exchange the input and output
    data structures of a calculation task together with the VTL
    Transformations describing the calculation algorithms);
- compilation and execution of VTL algorithms, either interpreting the
    VTL Transformations or translating them in whatever other computer
    language is deemed as appropriate.

[^1]:
    The Validation and Transformation Language is a standard language
    designed and published under the SDMX initiative. VTL is described in
    the VTL User and Reference Guides available on the [SDMX website](https://sdmx.org).

It is important to note that the VTL has its own information model (IM),
derived from the Generic Statistical Information Model (GSIM) and
described in the VTL User Guide. The VTL IM is designed to be compatible
with more standards, like SDMX, DDI (Data Documentation Initiative) and
GSIM, and includes the model artefacts that can be manipulated (inputs
and/or outputs of Transformations, e.g. "Data Set", "Data Structure")
and the model artefacts that allow the definition of the transformation
algorithms (e.g. "Transformation", "Transformation Scheme").

The VTL language can be applied to SDMX artefacts by mapping the SDMX IM
model artefacts to the model artefacts that VTL can manipulate[^2]. Thus,
the SDMX artefacts can be used in VTL as inputs and/or outputs of
Transformations. It is important to be aware that the artefacts do not
always have the same names in the SDMX and VTL IMs, nor do they always
have the same meaning. The more evident example is given by the SDMX
Dataset and the VTL "Data Set", which do not correspond one another: as
a matter of fact, the VTL "Data Set" maps to the SDMX "`Dataflow`" (or,
more generally, to a `DataStructureDefinition`, `Dataflow` or
`ProvisionAgreement`, see the paragraph
“[Mapping VTL Data Sets and Value Domains to SDMX artefacts](#mapping-vtl-data-sets-and-value-domains-to-sdmx-artefacts)”),
while the SDMX "`Dataset`" has no explicit mapping to VTL (such an
abstraction is not needed in the definition of VTL Transformations). A SDMX
"`Dataset`", however, is an instance of a SDMX "`Dataflow`" and can be the
artefact on which the VTL transformations are executed (i.e., the
Transformations are defined on `Dataflows` and are applied to `Dataflow`
instances that can be `Datasets`).

[^2]:
    In this chapter, in order to distinguish VTL and SDMX model
    artefacts, the VTL ones are written in the standard font while the SDMX
    ones in monospace font

The VTL programs (Transformation Schemes) are represented in SDMX
through the `TransformationScheme` maintainable class which is composed of
`Transformation` (nameable artefact). Each `Transformation` assigns the
outcome of the evaluation of a VTL expression to a result.

This section does not explain the VTL language or any of the content
published in the VTL guides. Rather, this is a description of how the
VTL can be used in the SDMX context and applied to SDMX artefacts.

## References to SDMX artefacts from VTL statements

### Introduction

The VTL can manipulate SDMX artefacts (or objects) by referencing them
through pre-defined conventional names (aliases).

The alias of an SDMX artefact can be its URN (Universal Resource Name),
an abbreviation of its URN or another user-defined name.

In any case, the aliases used in the VTL Transformations have to be
mapped to the SDMX artefacts through the `VtlMappingScheme` and `VtlMapping`
classes (see the section of the SDMX IM relevant to the VTL). A
`VtlMapping` allows specifying the alias (`vtlAlias`) to be used in the
VTL Transformations, Rulesets[^3] or User Defined Operators[^4] to
reference a SDMX artefact, together with the URN of such artefact
(`sdmxUrn`). A `VtlMappingScheme` is a container for zero or more
`VtlMapping`.

[^3]: See also the section "VTL-DL Rulesets" in the VTL Reference Manual.
[^4]:
    The VTLMappings are used also for User Defined Operators (UDO).
    Although UDOs are envisaged to be defined on generic operands, so that
    the specific artefacts to be manipulated are passed as parameters at
    their invocation, it is also possible that an UDO invokes directly some
    specific SDMX artefacts. These SDMX artefacts have to be mapped to the
    corresponding aliases used in the definition of the UDO through the
    `VtlMappingScheme` and `VtlMapping` classes as well.

The correspondence between aliases and SDMX artefacts is defined within
a `VtlMappingScheme`: an alias identifies one and just one SDMX artefact,
i.e. different `VtlMapping`s of the same `VtlMappingScheme` cannot have
the same alias, while the same SDMX artefact can be referenced through
different aliases (for example, when distinct VTL Data Sets are fed with
different parts of the data of the same SDMX artefact, see the section
“[Retrieving the data of the input VTL Data Sets](#retrieving-the-data-of-the-input-vtl-data-sets)”).

!!! note
    The direct references to SDMX artefacts through their URN or an
    abbreviation of their URN, written in the VTL statements and
    described in the paragraphs “References through the URN” and
    “Abbreviation of the URN” below, have been deprecated in SDMX 3.2;
    thus, the SDMX artefacts are referenced through user-defined aliases
    (see the paragraph “User-defined alias” below), which are mapped to
    the URNs of the artefacts by the `VtlMapping`s. The components of the
    VTL Data Sets are referenced through their names, which under the
    Basic mapping are the ids of the corresponding SDMX `Components`.

The references through the URN and the abbreviated URN are described in
the following paragraphs.

### References through the URN

!!! note
    The references to SDMX artefacts through their URN, written directly
    in the VTL statements, have been deprecated in SDMX 3.2; thus, the
    SDMX artefacts are referenced through user-defined aliases, mapped to
    their URN by the `VtlMapping`s (see the paragraph “User-defined alias”
    below).

This approach has the advantage that in the VTL code the URN of the
referenced artefacts is directly intelligible by a human reader but has
the drawback that the references are verbose.

The SDMX URN[^5] is the concatenation of the following parts, separated
by special symbols like dot, equal, asterisk, comma, and parenthesis:

- `SDMXprefix`
- `SDMX-IM-package-name`
- `class-name`
- `agency-id`
- `maintainedobject-id`
- `maintainedobject-version`
- `container-object-id` [^6]
- `object-id`

[^5]:
    For a complete description of the structure of the URN see the SDMX
    2.1 Standards - Section 5 - Registry Specifications, paragraph 6.2.2
    ("Universal Resource Name (URN)").
[^6]:
    The container-object-id can repeat and may not be present.

The generic structure of the URN is the following:

```text
SDMXprefix.SDMX-IM-package-name.class-name=agency-id:maintainedobject-id
(maintainedobject-version).*container-object-id.object-id
```

The `SDMXprefix` is `"urn:sdmx:org"`, always the same for all SDMX
artefacts.

The `SDMX-IM-package-name` is the concatenation of the string
`"sdmx.infomodel."` with the package-name, which the artefact belongs to.
For example, for referencing a `Dataflow` the `SDMX-IM-package-name` is
`"sdmx.infomodel.datastructure"`, because the class Dataflow belongs to
the package `"datastructure"`.

The `class-name` is the name of the SDMX object class, which the SDMX
object belongs to (e.g., for referencing a `Dataflow` the `class-name` is
`"Dataflow"`). The VTL can reference SDMX artefacts that belong to the
classes `Dataflow`, `Dimension`, `TimeDimension`, `Measure`, `DataAttribute`,
`Concept`, `Codelist`.

The `agency-id` is the acronym of the agency that owns the definition of
the artefact, for example for the Eurostat artefacts the `agency-id` is
`"ESTAT"`). The `agency-id` can be composite (for example
`AgencyA.Dept1.Unit2`).

The `maintainedobject-id` is the name of the maintained object which the
artefact belongs to, and in case the artefact itself is
maintainable[^7], coincides with the name of the artefact. Therefore the
`maintainedobject-id` depends on the class of the artefact:

- if the artefact is a `Dataflow`, which is a maintainable class, the
    `maintainedobject-id` is the `Dataflow` name (`dataflow-id`);
- if the artefact is a `Dimension`, `Measure`, `TimeDimension` or
    `DataAttribute`, which are not maintainable and belong to the
    `DataStructure` maintainable class, the `maintainedobject-id` is the
    name of the `DataStructure` (`dataStructure-id`) which the artefact
    belongs to;
- if the artefact is a `Concept`, which is not maintainable and belongs
    to the `ConceptScheme` maintainable class, the `maintainedobject-id` is
    the name of the `ConceptScheme` (`conceptScheme-id`) which the artefact
    belongs to;
- if the artefact is a `Codelist`, which is a maintainable class, the
    `maintainedobject-id` is the `Codelist` name (`codelist-id`).

[^7]: i.e., the artefact belongs to a maintainable class

The `maintainedobject-version` is the version, according to the SDMX
versioning rules, of the maintained object which the artefact belongs to
(for example, possible versions might be 1.0, 2.3, 1.0.0, 2.1.0 or
3.1.2).

The `container-object-id` does not apply to the classes that can be
referenced in VTL Transformations, therefore is not present in their URN

The `object-id` is the name of the non-maintainable artefact (when the
artefact is maintainable its name is already specified as the
`maintainedobject-id`, see above), in particular it has to be specified:

- if the artefact is a `Dimension`, `TimeDimension`, `Measure` or
    `DataAttribute` (the `object-id` is the name of one of the artefacts
    above, which are data structure components)
- if the artefact is a `Concept` (the `object-id` is the name of the
    `Concept`)

For example, by using the URN, the VTL Transformation that sums two SDMX
`Dataflows` `DF1` and `DF2` and assigns the result to a third persistent
`Dataflow` `DFR`, assuming that `DF1`, `DF2` and `DFR` are the `maintainedobject-id`
of the three `Dataflows`, that their version is 1.0.0 and their Agency is
`AG`, would be written as[^8]:

```text
'urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=AG:DFR(1.0.0)' <-
'urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=AG:DF1(1.0.0)' +
'urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=AG:DF2(1.0.0)'
```

[^8]:
    Since these references to SDMX objects include non-permitted
    characters as per the VTL ID notation, they need to be included between
    single quotes, according to the VTL rules for irregular names.

### Abbreviation of the URN

!!! note
    The references to SDMX artefacts through an abbreviation of their
    URN, written directly in the VTL statements, have been deprecated in
    SDMX 3.2; thus, the SDMX artefacts are referenced through user-defined
    aliases, mapped to their URN by the `VtlMapping`s (see the paragraph
    “User-defined alias” below). The components of the VTL Data Sets are
    still referenced through their names, which under the Basic mapping
    coincide with the ids of the SDMX `Components`.

The complete formulation of the URN described above is exhaustive but
verbose, even for very simple statements. In order to reduce the
verbosity through a simplified identifier and make the work of
transformation definers easier, proper abbreviations of the URN are
possible. Using this approach, the referenced artefacts remain
intelligible in the VTL code by a human reader.

The URN can be abbreviated by omitting the parts that are not essential
for the identification of the artefact or that can be deduced from other
available information, including the context in which the invocation is
made. The possible abbreviations are described below.

- The `SDMXprefix` can be omitted for all the SDMX objects, because it
    is a prefixed string (urn:sdmx:org), always the same for SDMX
    objects.
- The `SDMX-IM-package-name` can be omitted as well because it can be
    deduced from the `class-name` that follows it (the table of the
    SDMX-IM packages and classes that allows this deduction is in the 
    [Registry Specifications Section](../../logical_interfaces/logical_interfaces/6_Identification_of_SDMX_Objects.md#unique-identification-of-sdmx-objects)
    ). In particular, considering the object classes of the
    artefacts that VTL can reference, the package is:
    - `"datastructure"` for the classes `Dataflow`, `Dimension`,
        `TimeDimension`, `Measure`, `DataAttribute`,
    - `"conceptscheme"` for the class `Concept`,
    - `"codelist"` for the class `Codelist`.
- The `class-name` can be omitted as it can be deduced from the VTL
    invocation. In particular, starting from the VTL class of the
    invoked artefact (e.g. dataset, component, identifier, measure,
    attribute, variable, valuedomain), which is known given the syntax
    of the invoking VTL operator[^9], the SDMX class can be deduced from
    the mapping rules between VTL and SDMX (see the section 
    ["Mapping between VTL and SDMX"](#mapping-from-vtl-to-sdmx-data-structures) hereinafter)[^10].
- If the agency-id is not specified, it is assumed by default equal to
    the agency-id of the `TransformationScheme`, `UserDefinedOperatorScheme`
    or `RulesetScheme` from which the artefact is invoked. For example,
    the `agency-id` can be omitted if it is the same as the invoking
    `TransformationScheme` and cannot be omitted if the artefact comes
    from another agency[^11]. Take also into account that, according to
    the VTL consistency rules, the agency of the result of a
    `Transformation` must be the same as its `TransformationScheme`,
    therefore the `agency-id` can be omitted for all the results (left
    part of Transformation statements).
- As for the `maintainedobject-id`, this is essential in some cases
    while in other cases it can be omitted:
    - if the referenced artefact is a `Dataflow`, which is a
        maintainable class, the `maintainedobject-id` is the `dataflow-id`
        and obviously cannot be omitted;
    - if the referenced artefact is a `Dimension`, `TimeDimension`,
        `Measure`, `DataAttribute`, which are not maintainable and belong to
        the `DataStructure` maintainable class, the `maintainedobject-id` is
        the `dataStructure`-id and can be omitted, given that these
        components are always invoked within the invocation of a
        Dataflow, whose dataStructure-id can be deduced from the SDMX
        structural definitions;
    - if the referenced artefact is a `Concept`, which is not
        maintainable and belong to the `ConceptScheme` maintainable class,
        the maintained object is the `conceptScheme-id` and cannot be
        omitted;
    - if the referenced artefact is a `Codelist`, which is a
        maintainable class, the `maintainedobject-id` is the codelist-id
        and obviously cannot be omitted.
- When the `maintainedobject-id` is omitted, the
    `maintainedobject-version` is omitted too. When the
    `maintainedobject-id` is not omitted and the `maintainedobject-version`
    is omitted, the version 1.0 is assumed by default.
    - As said, the `container-object-id` does not apply to the classes that
        can be referenced in VTL Transformations, therefore is not present
        in their URN
    - The `object-id` does not exist for the artefacts belonging to the
        `Dataflow`, and `Codelist` classes, while it exists and cannot be
        omitted for the artefacts belonging to the classes `Dimension`,
        `TimeDimension`, `Measure`, `DataAttribute` and `Concept`, as for them the
        `object-id` is the main identifier of the artefact

[^9]: For the syntax of the VTL operators see the VTL Reference Manual
[^10]:
    In case the invoked artefact is a VTL component, which can be
    invoked only within the invocation of a VTL data set (SDMX Dataflow),
    the specific SDMX class-name (e.g. `Dimension`, `TimeDimension`, `Measure` or
    `DataAttribute`) can be deduced from the data structure of the SDMX
    Dataflow, which the component belongs to.
[^11]:
    If the Agency is composite (for example `AgencyA.Dept1.Unit2`), the
    agency is considered different even if only part of the composite name
    is different (for example `AgencyA.Dept1.Unit3` is a different Agency than
    the previous one). Moreover the `agency-id` cannot be omitted in part
    (i.e., if a `TransformationScheme` owned by `AgencyA.Dept1.Unit2` references
    an artefact coming from `AgencyA.Dept1.Unit3`, the specification of the
    `agency-id` becomes mandatory and must be complete, without omitting the
    possibly equal parts like `AgencyA.Dept1`)

The simplified object identifier is obtained by omitting all the first
part of the URN, including the special characters, till the first part
not omitted.

For example, the full formulation that uses the complete URN shown at
the end of the previous paragraph:

```text
'urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=AG:DFR(1.0.0)' :=
'urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=AG:DF1(1.0.0)' +
'urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=AG:DF2(1.0.0)'
```

by omitting all the non-essential parts would become simply:

```text
DFR := DF1 + DF2
```

The references to the `Codelists` can be simplified similarly. For
example, given the non-abbreviated reference to the `Codelist`
`AG:CL_FREQ(1.0.0)`, which is[^12]:

```text
'urn:sdmx:org.sdmx.infomodel.codelist.Codelist=AG:CL_FREQ(1.0.0)'
```

[^12]: 
    Single quotes are needed because this reference is not a VTL
    regular name.

if the `Codelist` is referenced from a `RulesetScheme` belonging to the
agency `AG`, omitting all the optional parts, the abbreviated reference
would become simply[^13]:

```text
CL_FREQ
```

[^13]:
    Single quotes are not needed in this case because `CL_FREQ` is a VTL
    regular name.

As for the references to the components, it can be enough to specify the
`component-Id`, given that the `dataStructure-Id` can be omitted. An example
of non-abbreviated reference, if the data structure is `DST1` and the
component is `SECTOR`, is the following:

```text
'urn:sdmx:org.sdmx.infomodel.datastructure.`DataStructure`=AG:DST1(1.0.0).SECTOR'
```

The corresponding fully abbreviated reference, if made from a
`TransformationScheme` belonging to `AG`, would become simply:

```text
SECTOR
```

For example, the `Transformation` for renaming the component `SECTOR` of the
`Dataflow` `DF1` into `SEC` can be written as[^14]:

```text
'DFR(1.0.0)' := 'DF1(1.0.0)' [rename SECTOR to SEC]
```

[^14]:
    The result `DFR(1.0.0)` is be equal to `DF1(1.0.0)` save that the
    component `SECTOR` is called `SEC`

In the references to the `Concepts`, which can exist for example in the
definition of the VTL Rulesets, at least the `conceptScheme-id` and the
`concept-id` must be specified.

An example of non-abbreviated reference, if the `conceptScheme-id` is `CS1`
and the `concept-id` is `SECTOR`, is the following:

```text
'urn:sdmx:org.sdmx.infomodel.conceptscheme.Concept=AG:CS1(1.0.0).SECTOR'
```

The corresponding fully abbreviated reference, if made from a
`RulesetScheme` belonging to `AG`, would become simply:

```text
CS1(1.0.0).SECTOR
```

The Codes and in general all the Values can be written without any other
specification, for example, the transformation to check if the values of
the measures of the `Dataflow` `DF1` are between 0 and 25000 can be written
like follows:

```text
'DFR(1.0.0)' := between ( 'DF1(1.0.0)', 0, 25000 )
```

The artefact (`Component`, `Concept`, `Codelist` …) which the Values are
referred to can be deduced from the context in which the reference is
made, taking also into account the VTL syntax. In the Transformation
above, for example, the values 0 and 2500 are compared to the values of
the measures of `DF1(1.0.0)`.

### User-defined alias

The third possibility for referencing SDMX artefacts from VTL statements
is to use user-defined aliases not related to the SDMX URN of the
artefact. As the references through the URN and the abbreviated URN
have been deprecated, this is the way of referencing SDMX artefacts from
VTL statements.

This approach gives preference to the use of symbolic names for the SDMX
artefacts. As a consequence, in the VTL code the referenced artefacts
may become not directly intelligible by a human reader. In any case, the
VTL aliases are associated to the SDMX URN through the `VtlMappingScheme`
and `VtlMapping` classes: each `VtlMapping` associates an alias
(`vtlAlias`) to the URN of a SDMX artefact (`sdmxUrn`). These classes
provide for structured references to SDMX artefacts whatever kind of
reference is used in VTL statements (URN, abbreviated URN or
user-defined aliases). The aliases follow the VTL naming rules: for
example, an alias containing characters that are not allowed in the VTL
regular names must be written between single quotes in the VTL
statements.

### References to SDMX artefacts from VTL Rulesets

The VTL Rulesets allow defining sets of reusable Rules that can be
applied by some VTL operators, like the ones for validation and
hierarchical roll-up. A "Rule" consists in a relationship between Values
belonging to some Value Domains or taken by some Variables, for example:
(i) when the Country is USA then the Currency is USD; (ii) the Benelux
is composed by Belgium, Luxembourg, Netherlands.

The VTL Rulesets have a signature, in which the Value Domains or the
Variables on which the Ruleset is defined are declared, and a body,
which contains the Rules.

In the signature, given the mapping between VTL and SDMX better
described in the following paragraphs, a reference to a VTL Value Domain
becomes a reference to a SDMX `Codelist` (mapped through a
`VtlCodelistMapping`), while a reference to a VTL
Represented Variable becomes a reference to a SDMX `Concept`, assuming for
it a definite representation[^15].

[^15]: Rulesets of this kind cannot be reused when the referenced Concept
has a different representation.

!!! note
    The mapping of the VTL Represented Variables to SDMX `Concepts`
    (`VtlConceptMapping`) has been deprecated in SDMX 3.2; thus, the
    Variables referenced in the Rulesets correspond to the components
    having the same names in the VTL Data Sets on which the Rulesets are
    applied, which under the Basic mapping are named after the ids of the
    SDMX `Components`.

In general, for referencing SDMX `Codelists` and `Concepts`, the conventions
described in the previous paragraphs apply. In the Ruleset syntax, the
elements that reference SDMX artefacts are called `"valueDomain"` and
`"variable"` for the Datapoint Rulesets and `"ruleValueDomain"`,
`"ruleVariable"`, `"condValueDomain"`, `"condVariable"` for the Hierarchical
Rulesets). The syntax of the Ruleset signature allows also to define
aliases of the elements above, these aliases are valid only within the
specific Ruleset definition statement and cannot be mapped to SDMX.[^16]

[^16]: See also the section "VTL-DL Rulesets" in the VTL Reference Manual.

In the body of the Rulesets, the Codes and in general all the Values can
be written without any other specification, because the artefact, which
the Values are referred (`Codelist`, `Concept`) to can be deduced from the
Ruleset signature.

## Mapping between SDMX and VTL artefacts

### When the mapping occurs

The mapping methods between the VTL and SDMX object classes allow
transforming a SDMX definition in a VTL one and vice-versa for the
artefacts to be manipulated.

It should be remembered that VTL programs (i.e. Transformation Schemes)
are represented in SDMX through the `TransformationScheme` maintainable
class which is composed of `Transformations` (nameable artefacts). Each
`Transformation` assigns the outcome of the evaluation of a VTL expression
to a result: the input operands of the expression and the result can be
SDMX artefacts.

Every time a SDMX object is referenced in a VTL Transformation as an
input operand, there is the need to generate a VTL definition of the
object, so that the VTL operations can take place. This can be made
starting from the SDMX definition and applying a SDMX-VTL mapping method
in the direction from SDMX to VTL. The mapping methods from SDMX to VTL
(of which only the Basic mapping is not deprecated) are described in the
following paragraphs and are conceived
to allow the automatic deduction of the VTL definition of the object
from the knowledge of the SDMX definition.

In the opposite direction, every time an object calculated by means of
VTL must be treated as a SDMX object (for example for exchanging it
through SDMX), there is the need of a SDMX definition of the object, so
that the SDMX operations can take place. The SDMX definition is needed
for the VTL objects for which a SDMX use is envisaged[^17].

[^17]:
    If a calculated artefact is persistent, it needs a persistent definition, 
    i.e. a SDMX definition in a SDMX environment. In addition,  possible calculated 
    artefact that are not persistent may require a SDMX definition, for example when 
    the result of a non-persistent calculation is disseminated through SDMX tools 
    (like an inquiry tool). However, only the persistent results can be
    mapped to SDMX artefacts as outputs of a VTL program (see the paragraph
    “[Mapping VTL Data Sets and Value Domains to SDMX artefacts](#mapping-vtl-data-sets-and-value-domains-to-sdmx-artefacts)”).

The mapping methods from VTL to SDMX are described in the following
paragraphs as well, however they do not allow the complete SDMX
definition to be automatically deduced from the VTL definition, more
than all because the former typically contains additional information in
respect to the latter. For example, the definition of a SDMX DSD
includes also some mandatory information not available in VTL (like the
concept scheme to which the SDMX components refer, the ‘usage’ and
‘`attributeRelationship`’ for the `DataAttributes` and so on). Therefore the
mapping methods from VTL to SDMX provide only a general guidance for
generating SDMX definitions properly starting from the information
available in VTL, independently of how the SDMX definition it is
actually generated (manually, automatically or part and part).

The direction of the mapping is declared through the `isInput` attribute
of the `VtlDatasetMapping` that maps the VTL Data Set: `true` for the
input operands of the VTL program (mapping from SDMX to VTL), `false`
for the results to be treated as SDMX objects (mapping from VTL to
SDMX), which must be persistent. For an output, the SDMX definition is
the one of the SDMX artefact referenced by the `sdmxUrn` of the
`VtlDatasetMapping`: its data structure must correspond, through the
Basic mapping from VTL to SDMX, to the data structure of the result of
the VTL Transformation.

### Mapping VTL Data Sets and Value Domains to SDMX artefacts

The VTL Data Sets and Value Domains used in a VTL program are mapped to
SDMX artefacts through the `VtlMapping` classes (see the section of the
SDMX IM relevant to the VTL):

- a `VtlDatasetMapping` maps a VTL Data Set, named by its alias
    (`vtlAlias`), to a SDMX `DataStructureDefinition`, `Dataflow` or
    `ProvisionAgreement`, identified by its URN (`sdmxUrn`), which also
    identifies the class of the artefact; it specifies as well whether
    the VTL Data Set is an input or an output of the VTL program
    (`isInput`);
- a `VtlCodelistMapping` maps a VTL Value Domain, named by its alias
    (`vtlAlias`), to a SDMX `Codelist`, identified by its URN
    (`sdmxUrn`), whose `Codes` are the values of the Value Domain; it is
    used only in input and does not have the `isInput` attribute.

As the VTL is strongly typed and does not include declarations of
variables, these mappings provide the definitions of the VTL Data Sets
and Value Domains used in the VTL program. Therefore, they are part of
the public definition of the VTL program: a `TransformationScheme` that
references SDMX artefacts is not complete without the `VtlMappingScheme`
containing these mappings.

The following rules apply to the `VtlDatasetMapping`:

1. `isInput` is mandatory: `true` means that the SDMX data are an input
    of the VTL program (from SDMX to VTL), `false` that they are an
    output (from VTL to SDMX). An alias identifies a VTL Data Set, which
    is either read or written by the VTL program: if the same SDMX
    artefact is both read and written, it is mapped by two
    `VtlDatasetMapping`s having distinct aliases.
2. The outputs must be persistent: a `VtlDatasetMapping` having
    `isInput` equal to `false` must correspond to a `Transformation`
    whose `result` is the `vtlAlias` and whose `isPersistent` is `true`.
    This can be checked by using the SDMX metadata only, without parsing
    the VTL expressions.
3. The data structure of the VTL Data Set corresponds to the data
    structure of the referenced SDMX artefact, i.e. of the
    `DataStructureDefinition` itself or of the one used by the
    `Dataflow` or by the `ProvisionAgreement`, through the Basic mapping
    (see below), which is the only mapping method for the
    `VtlDatasetMapping`.
4. The mapping is many-to-many: a `TransformationScheme` can use any
    number of VTL Data Sets, and the same SDMX artefact can be
    referenced by different `VtlDatasetMapping`s (with distinct aliases),
    within the same `VtlMappingScheme` or in different ones. For
    example, two VTL Data Sets can be mapped to the same SDMX `Dataflow`
    or `DataStructureDefinition` and be fed with different parts of its
    data (see the section
    “[Retrieving the data of the input VTL Data Sets](#retrieving-the-data-of-the-input-vtl-data-sets)”
    below).

For example, the `TransformationScheme` `OECD:TS_DIFF(1.0)`, whose
`vtlVersion` is “2.1”, calculates the difference between two VTL Data
Sets and stores the result persistently:

```text
diff <- ds_a - ds_b;
```

Its `VtlMappingScheme` `OECD:VTL_MAP(1.0)` contains the following
`VtlDatasetMapping`s:

| `vtlAlias` | `sdmxUrn` | `isInput` |
| :--- | :--- | :--- |
| `ds_a` | `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=OECD.SDD.NAD:DF_A(1.0)` | `true` |
| `ds_b` | `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=OECD.SDD.NAD:DF_B(1.0)` | `true` |
| `diff` | `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=OECD.SDD.NAD:DF_DIFF(1.0)` | `false` |

`ds_a` and `ds_b` are inputs, while `diff` is a persistent output. Under
the Basic mapping, the `Dimensions` and the `TimeDimension` of the
`Dataflows` become VTL Identifiers and their `Measures` become VTL
Measures, so that the expression `ds_a - ds_b` can be checked by the VTL
engine (assuming that `DF_A` and `DF_B` have the same `Dimensions` and
`Measures`); the data structure of `DF_DIFF` must correspond to the one
of the result.

As a second example, the `TransformationScheme` `ESTAT:TS_AREACHK(1.0)`,
whose `vtlVersion` is “2.1”, selects the data points of a VTL Data Set
whose reference area is not a valid code of a SDMX `Codelist`:

```text
ds_invalid <- ds_x [ filter not ( REF_AREA in cl_area ) ];
```

Its `VtlMappingScheme` contains the following `VtlMapping`s:

| Class | `vtlAlias` | `sdmxUrn` | `isInput` |
| :--- | :--- | :--- | :--- |
| `VtlDatasetMapping` | `ds_x` | `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=ESTAT:DF_X(1.0)` | `true` |
| `VtlDatasetMapping` | `ds_invalid` | `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=ESTAT:DF_INVALID(1.0)` | `false` |
| `VtlCodelistMapping` | `cl_area` | `urn:sdmx:org.sdmx.infomodel.codelist.Codelist=SDMX:CL_AREA(2.0)` | (not applicable) |

`cl_area` is the name of the VTL Value Domain whose values are the
`Codes` of the `Codelist` `SDMX:CL_AREA(2.0)`, and the VTL `in` operator
checks whether each value of the Identifier `REF_AREA` belongs to such a
Value Domain. As a Value Domain is structural metadata, its values are
obtained from the SDMX structural definitions and no data retrieval is
needed for it.

### General mapping of VTL and SDMX data structures

This section makes reference to the VTL "Model for data and their
structure"[^18] and the correspondent SDMX "Data Structure
Definition"[^19].

[^18]: See the VTL 2.0 User Manual
[^19]: See the [SDMX Standards Section Information Model](../../information_model/information_model/4_Data_Structure_Definition_and_Dataset.md)

The main type of artefact that the VTL can manipulate is the VTL Data
Set, which is mapped through a `VtlDatasetMapping` to a SDMX `Dataflow`
or, more generally, to a SDMX `DataStructureDefinition`, `Dataflow` or
`ProvisionAgreement`. This means that a VTL Transformation, in the SDMX
context, expresses the algorithm for calculating derived SDMX data (e.g.
a derived `Dataflow`) starting from some already existing SDMX data
(either collected or derived).[^20]

[^20]: 
    Besides the mapping between one SDMX `Dataflow` and one VTL Data Set,
    the same SDMX artefact can be mapped to more VTL Data Sets, possibly
    fed with different parts of its data (see the section
    “[Retrieving the data of the input VTL Data Sets](#retrieving-the-data-of-the-input-vtl-data-sets)”).
    The mapping of distinct parts of a SDMX `Dataflow` to different VTL
    Data Sets through the ordered concatenation notation, explained in a
    following paragraph, has been deprecated.

While the VTL Transformations are defined in term of `Dataflow`
definitions, they are assumed to be executed on instances of such
`Dataflow`s, provided at runtime to the VTL engine (the mechanism for
identifying the instances to be processed are not part of the VTL
specifications and depend on the implementation of the VTL-based
systems). As already said, the SDMX `Datasets` are instances of SDMX
`Dataflow`s, therefore a VTL Transformation defined on some SDMX `Dataflow`s
can be applied on some corresponding SDMX `Datasets`. In SDMX, the
retrieval of the data of the input VTL Data Sets can optionally be
specified through the `VtlDataExtraction` (see the section
“[Retrieving the data of the input VTL Data Sets](#retrieving-the-data-of-the-input-vtl-data-sets)”
below).

A VTL Data Set is structured by one and just one Data Structure and a
VTL Data Structure can structure any number of Data Sets.
Correspondingly, in the SDMX context a SDMX `Dataflow` is structured by
one and just one `DataStructureDefinition` and one `DataStructureDefinition`
can structure any number of `Dataflow`s.

A VTL Data Set has a Data Structure made of Components, which in turn
can be Identifiers, Measures and Attributes. Similarly, a SDMX
`DataflowDefinition` has a `DataStructureDefinition` made of components that
can be `DimensionComponents`, Measure and `DataAttributes`. In turn, a SDMX
`DimensionComponent` can be a Dimension or a `TimeDimension`.
Correspondingly, in the SDMX implementation of the VTL, the VTL
Identifiers can be (optionally) distinguished in similar sub-classes
(Simple Identifier, Time Identifier) even if such a distinction is not
evidenced in the VTL IM.

The possible mapping options are described in more detail in the
following sections.

### Mapping from SDMX to VTL data structures

#### Basic Mapping

The mapping method from SDMX to VTL is called **Basic** mapping. It is
the only mapping method applicable to the `VtlDatasetMapping`s: the
alternative methods described in the following paragraphs, which can be
declared only for the deprecated `VtlDataflowMapping`, have been
deprecated.

When transforming **from SDMX to VTL**, this method consists in leaving
the components unchanged and maintaining their names and roles,
according to the following normative table:

| SDMX component | VTL role | Nullable |
| :--- | :--- | :--- |
| `Dimension` | (Simple) Identifier | No |
| `TimeDimension` | (Time) Identifier | No |
| `Measure` | Measure | Yes |
| `DataAttribute` | Attribute | Yes |

The names of the VTL components are the ids of the corresponding SDMX
components. The VTL Identifiers cannot contain NULLs, while the VTL
Measures and Attributes can (a missing value in SDMX becomes a NULL in
VTL, see the paragraph “[Null Values](#null-values)” below).

The SDMX `DataAttributes`, in VTL they are all considered "at data point /
observation level" (i.e. dependent on all the VTL Identifiers), because
VTL does not have the SDMX `AttributeRelationships`, which defines the
construct to which the `DataAttribute` is related (e.g. observation,
dimension or set or group of dimensions, whole data set).

With the Basic mapping, one SDMX observation[^21] generates one VTL data
point.

[^21]:
    Here an SDMX observation is meant to correspond to one combination
    of values of the `DimensionComponents`.

#### Pivot Mapping

!!! note
    The Pivot mapping method has been deprecated in SDMX 3.2; thus, the
    Basic mapping applies, and the SDMX data structures having a
    `Dimension` that plays the role of measure dimension can be pivoted,
    if needed, in the VTL program (for example through the VTL `pivot`
    clause), as SDMX 3 supports multiple `Measures` natively.

An alternative mapping method from SDMX to VTL is the **Pivot** mapping,
which makes sense and is different from the Basic method only for the
SDMX data structures that contain a `Dimension` that plays the `role` of
measure dimension (like in SDMX 2.1) and just one `Measure`. Through this
method, these structures can be mapped to multi-measure VTL data
structures. Besides that, a user may choose to use any `Dimension` acting
as a list of `Measures` (e.g., a `Dimension` with indicators), either by
considering the “Measure” `role` of a `Dimension`, or at will using any
coded `Dimension`. Of course, in SDMX 3.0, this can only work when only
one `Measure` is defined in the DSD.

In SDMX 2.1 the `MeasureDimension` was a subclass of `DimensionComponent`
like `Dimension` and `TimeDimension`. In the current SDMX version, this
subclass does not exist anymore, however a `Dimension` can have the `role`
of measure dimension (i.e. a `Dimension` that contributes to the
identification of the measures). In SDMX 2.1 a `DataStructure` could have
zero or one `MeasureDimensions`, in the current version of the standard,
from zero to many `Dimension` may have the `role` of measure dimension.
Hereinafter a `Dimension` that plays the `role` of measure dimension is
referenced for simplicity as “`MeasureDimension`“, i.e. maintaining the
capital letters and the courier font even if the `MeasureDimension` is not
anymore a class in the SDMX Information Model of the current SDMX
version. For the sake of simplicity, the description below considers
just one `Dimension` having the `role` of `MeasureDimension` (i.e., the more
simple and common case). Nevertheless, it maintains its validity also if
in the `DataStructure` there are more dimension with the `role` of
`MeasureDimensions`: in this case what is said about the `MeasureDimension`
must be applied to the combination of all the `MeasureDimensions`
considered as a joint variable[^22].

[^22]:
    E.g., if in the data structure there exist 3 Dimensions `C,D,E`
    having the role of `MeasureDimension`, they should be considered as a
    joint `MeasureDimension Z=(C,D,E);` therefore when the description says
    “each possible value Cj of the `MeasureDimension` …” it means “each
    possible combination of values `(Cj, Dk, Ew)` of the joint
    `MeasureDimension Z=(C,D,E)`”.

Among other things, the Pivot method provides also backward
compatibility with the SDMX 2.1 data structures that contained a
`MeasureDimension`.

If applied to SDMX structures that do not contain any `MeasureDimension`,
this method behaves like the Basic mapping (see the previous paragraph).

The SDMX structures that contain a `MeasureDimension` are mapped as
described below (this mapping is equivalent to a pivoting operation):

- A SDMX simple dimension becomes a VTL (simple) identifier and a SDMX
    `TimeDimension` becomes a VTL (time) identifier;
- Each possible `Code Cj` of the SDMX `MeasureDimension` is mapped to a
    VTL Measure, having the same name as the SDMX Code (i.e. `Cj`); the
    VTL Measure `Cj` is a new VTL component even if the SDMX data
    structure has not such a `Component`;
- The SDMX `MeasureDimension` is not mapped to VTL (it disappears in the
    VTL Data Structure);
- The SDMX `Measure` is not mapped to VTL as well (it disappears in the
    VTL Data Structure);
- An SDMX `DataAttribute` is mapped in different ways according to its
    `AttributeRelationship`:
    - If, according to the SDMX `AttributeRelationship`, the values of
        the `DataAttribute` do not depend on the values of the
        `MeasureDimension`, the SDMX `DataAttribute` becomes a VTL Attribute
        having the same name. This happens if the `AttributeRelationship`
        is not specified (i.e. the `DataAttribute` does not depend on any
        `DimensionComponent` and therefore is at data set level), or if it
        refers to a set (or a group) of dimensions which does not
        include the `MeasureDimension`;
    - Otherwise, if, according to the SDMX `AttributeRelationship`, the
        values of the `DataAttribute` depend on the `MeasureDimension`, the
        SDMX `DataAttribute` is mapped to one VTL Attribute for each
        possible Code of the SDMX `MeasureDimension`. By default, the
        names of the VTL Attributes are obtained by concatenating the
        name of the SDMX `DataAttribute` and the names of the
        correspondent Code of the `MeasureDimension` separated by
        underscore. For example, if the SDMX `DataAttribute` is named `DA`
        and the possible Codes of the SDMX `MeasureDimension` are named
        `C1, C2, …, Cn`, then the corresponding VTL Attributes will be
        named `DA_C1, DA_C2, …, DA_Cn` (if different names are desired,
        they can be achieved afterwards by renaming the Attributes
        through VTL operators).
    - Like in the Basic mapping, the resulting VTL Attributes are
        considered as dependent on all the VTL identifiers (i.e. "at
        data point / observation level"), because VTL does not have the
        SDMX notion of Attribute Relationship.

The summary mapping table of the "pivot" mapping from SDMX to VTL for
the SDMX data structures that contain a `MeasureDimension` is the following:

| SDMX Component                                   | VTL Mapping                                      |
| :--------------------------------------------------- | :--------------------------------------------------- |
| Dimension                                            | (Simple) Identifier                                  |
| `TimeDimension`                                        | (Time) Identifier                                    |
| `MeasureDimension` & one `Measure`                       | One Measure for each `Code` of the SDMX `MeasureDimension`|
| `DataAttribute` (not depending on `MeasureDimension`)    | Attribute                                            |
| `DataAttribute` (depending on `MeasureDimension`)        | One Attribute for each `Code` of the SDMX `MeasureDimension` |

Using this mapping method, the components of the data structure can
change in the conversion from SDMX to VTL and it must be taken into
account that the VTL statements can reference only the components of the
resulting VTL data structure.

At observation / data point level, calling `Cj (j=1, … n)` the
j-th Code of the `MeasureDimension`:

- The set of SDMX observations having the same values for all the
    Dimensions except than the `MeasureDimension` become one multi-measure
    VTL Data Point, having one Measure for each Code Cj of the SDMX
    `MeasureDimension`;
- The values of the SDMX simple `Dimensions`, `TimeDimension` and
    `DataAttributes` not depending on the `MeasureDimension` (these
    components by definition have always the same values for all the
    observations of the set above) become the values of the
    corresponding VTL (simple) Identifiers, (time) Identifier and
    Attributes.
- The value of the Measure of the SDMX observation belonging to the
    set above and having `MeasureDimension=Cj` becomes the value of the
    VTL Measure `Cj`
- For the SDMX `DataAttributes` depending on the `MeasureDimension`, the
    value of the `DataAttribute DA` of the SDMX observation belonging to
    the set above and having `MeasureDimension=Cj` becomes the value of
    the VTL Attribute `DA_Cj`

#### From SDMX DataAttributes to VTL Measures

!!! note
    The `Basic_A2M` and `Pivot_A2M` mapping methods have been deprecated
    in SDMX 3.2; thus, the Basic mapping applies, and the role of the
    components can be changed, if needed, in the VTL program (for example
    through the VTL `calc` clause).

- In some cases, it may happen that the `DataAttributes` of the SDMX
    `DataStructure` need to be managed as Measures in VTL. Therefore, a
    variant of both the methods above consists in transforming all the
    SDMX `DataAttributes` in VTL Measures. When `DataAttributes` are
    converted to Measures, the two methods above are called `Basic_A2M`
    and `Pivot_A2M` (the suffix "A2M" stands for Attributes to Measures).
    Obviously, the resulting VTL data structure is, in general,
    multi-measure and does not contain Attributes.

The `Basic_A2M` and `Pivot_A2M` behaves respectively like the Basic and
Pivot methods, except that the final VTL components, which according to
the Basic and Pivot methods would have had the role of Attribute, assume
instead the role of Measure.

Proper VTL features allow changing the role of specific attributes even
after the SDMX to VTL mapping: they can be useful when only some of the
`DataAttributes` need to be managed as VTL Measures.

### Mapping from VTL to SDMX data structures

#### Basic Mapping

The mapping method **from VTL to SDMX** is called **Basic** mapping
as well.

It is the only mapping method applicable to the `VtlDatasetMapping`s:
the alternative methods described in the following paragraphs, which can
be declared only for the deprecated `VtlDataflowMapping`, have been
deprecated.

The method consists in leaving the components unchanged and maintaining
their names and roles in SDMX, according to the following mapping table,
which is the same as the basic mapping from SDMX to VTL, only seen in
the opposite direction.

Mapping table:

| VTL | SDMX |
| :--- | :--- |
| (Simple) Identifier | `Dimension` |
| (Time) Identifier | `TimeDimension` |
| Measure | `Measure` |
| Attribute | `DataAttribute` |

If the distinction between simple identifier and time identifier is not
maintained in the VTL environment, the classification between `Dimension`
and `TimeDimension` exists only in SDMX, as declared in the relevant
`DataStructureDefinition`.

Regarding the Attributes, because VTL considers all of them "at
observation level", the corresponding SDMX `DataAttributes` should be put
"at observation level" as well, unless some different information about
their `AttributeRelationship` is otherwise available.

Note that the basic mappings in the two directions (from SDMX to VTL and
vice-versa) are (almost completely) reversible. In fact, if a SDMX
structure is mapped to a VTL structure and then the latter is mapped
back to SDMX, the resulting data structure is like the original one
(apart for the `AttributeRelationship`, that can be different if the
original SDMX structure contains `DataAttributes` that are not at
observation level). In reverse order, if a VTL structure is mapped to
SDMX and then the latter is mapped back to VTL, the original data
structure is obtained.

As said, the resulting SDMX definitions must be compliant with the SDMX
consistency rules. For example, the SDMX DSD must have the
`AttributeRelationship` for the `DataAttributes`, which does not exist in
VTL.

#### Unpivot Mapping

!!! note
    The Unpivot mapping method has been deprecated in SDMX 3.2; thus, the
    Basic mapping applies, and the multi-measure VTL data structures can
    be unpivoted, if needed, in the VTL program (for example through the
    VTL `unpivot` clause) before being assigned to an output VTL Data Set.

An alternative mapping method from VTL to SDMX is the **Unpivot**
mapping.

Although this mapping method can be used in any case, it makes major
sense in case the VTL data structure has more than one measure component
(multi-measures VTL structure). This is used to support the SDMX 2.1
case of a `MeasureDimension` or any other Dimension acting as a list of
Measures, under the assumptions explained in section “Pivot Mapping”.

The multi-measures VTL structures are converted to SDMX `Dataflows` having
an added `MeasureDimension`, which disambiguates the VTL multiple
Measures, and a new Measure in place of the VTL ones, containing the
values of the VTL Measures.

The **unpivot** mapping behaves like follows:

- like in the basic mapping, a VTL (simple) identifier becomes a SDMX
    `Dimension` and a VTL (time) identifier becomes a SDMX `TimeDimension`
    (as said, a measure identifier cannot exist in multi-measure VTL
    structures);
- a `MeasureDimension` component called `"measure_name"` is added to the
    SDMX `DataStructure`;
- a `Measure` component called `"obs_value"` is added to the SDMX
    `DataStructure`;
- each VTL Measure is mapped to a `Code` of the SDMX `MeasureDimension`
    having the same name as the VTL Measure (therefore all the VTL
    Measure Components do not originate Components in the SDMX
    `DataStructure`);
- a VTL Attribute becomes a SDMX `DataAttribute` having
    `AttributeRelationship` referred to all the SDMX `DimensionComponents`
    including the `TimeDimension` and except the `MeasureDimension`.

The summary mapping table of the **unpivot** mapping method is the
following:

| VTL                | SDMX                                                                                     |
| :--------------------- | :-------------------------------------------------------------------------------------------- |
| (Simple) Identifier    | `Dimension`                                                                                     |
| (Time) Identifier      | `TimeDimension`                                                                                 |
| All Measure Components | `MeasureDimension` (having one `Code` for each VTL measure component) and one `Measure`             |
| Attribute              | `DataAttribute` depending on all SDMX `Dimensions` including the `TimeDimension` and except the `MeasureDimension` |

At observation / data point level:

- a multi-measure VTL Data Point becomes a set of SDMX observations,
    one for each VTL Measure;
- the values of the VTL Identifiers become the values of the
    corresponding SDMX `DimensionComponents`, for all the observations of
    the set above;
- the name of the j-th VTL Measure (e.g. “Cj”) becomes the
    Code of the SDMX `MeasureDimension` of the j-th observation
    of the set;
- the value of the j-th VTL Measure becomes the value of the
    SDMX Measure of the j-th observation of the set;
- the values of the VTL Attributes become the values of the
    corresponding SDMX `DataAttributes` (in principle for all the
    observations of the set above).

If desired, this method can be applied also to mono-measure VTL
structures, provided that none of the VTL Components has already the
role of Measure Identifier. Like in the general case, a `MeasureDimension`
component called “measure_name” is added to the SDMX `DataStructure`, in
this case it has just one possible `Code`, corresponding to the name of
the unique VTL Measure. The original VTL Measure would not become a
Component in the SDMX data structure. The value of the VTL Measure would
be assigned to the unique SDMX Measure called “obs_value”.

In any case, the resulting SDMX definitions must be compliant with the
SDMX consistency rules. For example, the possible `Codes` of the SDMX
`MeasureDimension` need to be listed in a SDMX `Codelist`, with proper id,
agency and version; moreover, the SDMX DSD must have the
`AttributeRelationship` for the `DataAttributes`, which does not exist in
VTL.

#### From VTL Measures to SDMX Data Attributes

!!! note
    The M2A mapping method has been deprecated in SDMX 3.2; thus, the
    Basic mapping applies, and the role of the VTL components can be
    changed, if needed, in the VTL program (for example, some Measures can
    become Attributes through the VTL `calc` clause), so that the result
    corresponds to the data structure of the output SDMX artefact.

More than all for the multi-measure VTL structures (having more than one
Measure Component), it may happen that the Measures of the VTL Data
Structure need to be managed as `DataAttributes` in SDMX. Therefore, a
third mapping method consists in transforming some VTL measures in a
corresponding SDMX `Measures` and all the other VTL Measures in SDMX
`DataAttributes`. This method is called `M2A` (“M2A” stands for “Measures to
`DataAttributes`”).

All VTL Measures maintain their names in SDMX. The VTL Measure
Components that become SDMX `DataAttributes` are the ones declared as
`DataAttributes` in the target SDMX data structure definition.

The mapping table is the following:

| VTL | SDMX |
| :--- | :--- |
| (Simple) Identifier | `Dimension` |
| (Time) Identifier | `TimeDimension` |
| Some Measures | `Measure` |
| Other Measures | `DataAttribute` |
| Attribute | `DataAttribute` |

Even in this case, the resulting SDMX definitions must be compliant with
the SDMX consistency rules. For example, the SDMX DSD must have the
`attributeRelationship` for the `DataAttributes`, which does not exist in
VTL.

### Declaration of the mapping methods between data structures

!!! note
    The declaration of the mapping methods through the `toVtlMappingMethod`
    and `fromVtlMappingMethod` attributes of the `VtlDataflowMapping`,
    including the conventional "generic_dataflow", has been deprecated in
    SDMX 3.2; thus, the Basic mapping is always applied to the VTL Data
    Sets mapped through a `VtlDatasetMapping`, which has no attributes for
    declaring the mapping methods.

In order to define and understand properly VTL Transformations, the
applied mapping methods must be specified in the SDMX structural
metadata. If the default mapping method (Basic) is applied, no
specification is needed.

A customized mapping can be defined through the `VtlMappingScheme` and
`VtlDataflowMapping` classes (see the section of the SDMX IM relevant to
the VTL). A `VtlDataflowMapping` allows specifying the mapping methods to
be used for a specific dataflow, both in the direction from SDMX to VTL
(`toVtlMappingMethod`) and from VTL to SDMX (`fromVtlMappingMethod`); in
fact a `VtlDataflowMapping` associates the structured URN that identifies
a SDMX `Dataflow` to its VTL alias and its mapping methods.

It is possible to specify the `toVtlMappingMethod` and
`fromVtlMappingMethod` also for the conventional `dataflow` called
"generic_dataflow": in this case the specified mapping methods are
intended to become the default ones, overriding the "Basic" methods. In
turn, the `toVtlMappingMethod` and `fromVtlMappingMethod` declared for a
specific `Dataflow` are intended to override the default ones for such a
`Dataflow`.

The `VtlMappingScheme` is a container for zero or more `VtlDataflowMapping`
(it may contain also mappings towards artefacts other than dataflows).

### Mapping dataflow subsets to distinct VTL Data Sets

!!! note
    The mapping of subsets of a SDMX `Dataflow` to distinct VTL Data Sets
    described in this paragraph, which uses the ordered concatenation
    notation and the `ToVtlSubspace`, `ToVtlSpaceKey`, `FromVtlSuperspace`
    and `FromVtlSpaceKey` classes, has been deprecated in SDMX 3.2; thus,
    in the direction from SDMX to VTL, the same SDMX artefact can be
    mapped to distinct input VTL Data Sets having distinct aliases, whose
    data are restricted to the desired subsets through the parameters of
    their `VtlDataExtraction` (e.g. a fixed `key`), and the Dimensions
    having a fixed value can be dropped through the VTL `sub` clause; in
    the direction from VTL to SDMX, the VTL `calc` and `union` operators
    can be used as explained below.

Until now it has been assumed to map one SMDX `Dataflow` to one VTL Data
Set and vice-versa. This mapping one-to-one is not mandatory according
to VTL because a VTL Data Set is meant to be a set of observations (data
points) on a logical plane, having the same logical data structure and
the same general meaning, independently of the possible physical
representation or storage (see VTL 2.0 User Manual page 24), therefore a
SDMX `Dataflow` can be seen either as a unique set of data observations
(corresponding to one VTL Data Set) or as the union of many sets of data
observations (each one corresponding to a distinct VTL Data Set).

As a matter of fact, in some cases it can be useful to define VTL
operations involving definite parts of a SDMX `Dataflow` instead than the
whole.[^23]

[^23]:
    A typical example of this kind is the validation, and more in
    general the manipulation, of individual time series belonging to the
    same `Dataflow`, identifiable through the `DimensionComponents` of the
    `Dataflow` except the `TimeDimension`. The coding of these kind of
    operations might be simplified by mapping distinct time series (i.e.
    different parts of a SDMX `Dataflow`) to distinct VTL Data Sets.

Therefore, in order to make the coding of VTL operations simpler when
applied on parts of SDMX `Dataflow`s, it is allowed to map distinct parts
of a SDMX `Dataflow` to distinct VTL Data Sets according to the following
rules and conventions. This kind of mapping is possible both from SDMX
to VTL and from VTL to SDMX, as better explained below.[^24]

[^24]:
    Please note that this kind of mapping is only an option at disposal
    of the definer of VTL Transformations; in fact it remains always
    possible to manipulate the needed parts of SDMX `Dataflow`s by means of
    VTL operators (e.g. “sub”, “filter”, “calc”, “union” …), maintaining a
    mapping one-to-one between SDMX `Dataflow`s and VTL Data Sets.

Given a SDMX `Dataflow` and some predefined `Dimensions` of its
`DataStructure`, it is allowed to map the subsets of observations that
have the same combination of values for such `Dimensions` to correspondent
VTL datasets.

For example, assuming that the SDMX `Dataflow` DF1(1.0.0) has the
`Dimensions` `INDICATOR`, `TIME_PERIOD` and `COUNTRY`, and that the user
declares the `Dimensions` `INDICATOR` and `COUNTRY` as basis for the mapping
(i.e. the mapping dimensions): the observations that have the same
values for `INDICATOR` and `COUNTRY` would be mapped to the same VTL dataset
(and vice-versa).

In practice, this kind mapping is obtained like follows:

- For a given SDMX `Dataflow`, the user (VTL definer) declares the
    `DimensionComponents` on which the mapping will be based, in a given
    order.[^25] Following the example above, imagine that the user
    declares the Dimensions INDICATOR and `COUNTRY`.
- The VTL Data Set is given a name using a special notation also
    called “ordered concatenation” and composed of the following parts:
    - The reference to the SDMX `Dataflow` (expressed according to the
        rules described in the previous paragraphs, i.e. URN,
        abbreviated URN or another alias); for example DF(1.0.0);
    - a slash (“/”) as a separator; [^26]
    - The reference to a specific part of the SDMX `Dataflow` above,
        expressed as the concatenation of the values that the SDMX
        `DimensionComponents` declared above must have, separated by dots
        (`“.”`) and written in the order in which these
        `DimensionComponents` are defined[^27]. For example POPULATION.USA
        would mean that such a VTL Data Set is mapped to the SDMX
        observations for which the dimension `INDICATOR` is equal to
        POPULATION and the dimension `COUNTRY` is equal to USA.

[^25]:
    This definition is made through the `ToVtlSubspace` and `ToVtlSpaceKey`
    classes and/or the `FromVtlSuperspace` and `FromVtlSpaceKey` classes,
    depending on the direction of the mapping (“key” means “dimension”). The
    mapping of `Dataflow` subsets can be applied independently in the two
    directions, also according to different Dimensions. When no Dimension is
    declared for a given direction, it is assumed that the option of mapping
    different parts of a SDMX `Dataflow` to different VTL Data Sets is not
    used.
[^26]:
    As a consequence of this formalism, a slash in the name of the VTL
    Data Set assumes the specific meaning of separator between the name of
    the `Dataflow` and the values of some of its Dimensions.
[^27]:
    This is the order in which the dimensions are defined in the
    `ToVtlSpaceKey` class or in the `FromVtlSpaceKey` class, depending on the
    direction of the mapping.

In the VTL Transformations, this kind of dataset name must be referenced
between single quotes because the slash (`“/”`) is not a regular character
according to the VTL rules.

Therefore, the generic name of this kind of VTL datasets would be:

```text
'DF(1.0.0)/INDICATORvalue.COUNTRYvalue'
```

Where `DF(1.0.0)` is the `Dataflow` and `INDICATORvalue` and `COUNTRYvalue`
are placeholders for one value of the `INDICATOR` and `COUNTRY` dimensions.

Instead the specific name of one of these VTL datasets would be:

```text
‘DF(1.0.0)/POPULATION.USA’
```

In particular, this is the VTL dataset that contains all the
observations of the `Dataflow` `DF(1.0.0)` for which `INDICATOR = POPULATION`
and `COUNTRY = USA`.

Let us now analyse the different meaning of this kind of mapping in the
two mapping directions, i.e. from SDMX to VTL and from VTL to SDMX.

As already said, the mapping from SDMX to VTL happens when the SDMX
`Dataflows` are operand of VTL Transformations, instead the mapping from
VTL to SDMX happens when the VTL Data Sets that is result of
Transformations[^28] need to be treated as SDMX objects. This kind of
mapping can be applied independently in the two directions and the
`Dimensions` on which the mapping is based can be different in the two
directions: these `Dimensions` are defined in the `ToVtlSpaceKey` and in the
`FromVtlSpaceKey` classes respectively.

[^28]:
    It should be remembered that, according to the VTL consistency
    rules, a given VTL dataset cannot be the result of more than one VTL
    Transformation.

First, let us see what happens in the **mapping direction from SDMX to VTL**,
i.e. when parts of a SDMX Dataflow (e.g. `DF1(1.0.0)`) need to be
mapped to distinct VTL Data Sets that are operand of some VTL
Transformations.

As already said, each VTL Data Set is assumed to contain all the
observations of the SDMX Dataflow having `INDICATOR=INDICATORvalue` and
`COUNTRY = COUNTRYvalue`. For example, the VTL dataset
`‘DF1(1.0.0)/POPULATION.USA’` would contain all the observations of
`DF1(1.0.0)` having `INDICATOR = POPULATION` and `COUNTRY = USA`.

In order to obtain the data structure of these VTL Data Sets from the
SDMX one, it is assumed that the SDMX `DimensionComponents` on which the
mapping is based are dropped, i.e. not maintained in the VTL data
structure; this is possible because their values are fixed for each one
of the invoked VTL Data Sets[^29]. After that, the mapping method from
SDMX to VTL specified for the Dataflow `DF1(1.0.0)` is applied (i.e.
basic, pivot …).

[^29]:
    If these `DimensionComponents` would not be dropped, the various VTL
    Data Sets resulting from this kind of mapping would have non-matching
    values for the Identifiers corresponding to the mapping Dimensions (e.g.
    `POPULATION` and `COUNTRY`). As a consequence, taking into account that the
    typical binary VTL operations at dataset level (`+`, `-`, `*`, `/` and so on)
    are executed on the observations having matching values for the
    identifiers, it would not be possible to compose the resulting VTL
    datasets one another (e.g. it would not be possible to calculate the
    population ratio between USA and CANADA).

In the example above, for all the datasets of the kind
`‘DF1(1.0.0)/INDICATORvalue.COUNTRYvalue’`, the dimensions `INDICATOR`
and COUNTRY would be dropped so that the data structure of all the
resulting VTL Data Sets would have the identifier `TIME_PERIOD` only.

It should be noted that the desired VTL Data Sets (i.e. of the kind
`‘DF1(1.0.0)/INDICATORvalue.COUNTRYvalue’`) can be obtained also by
applying the VTL operator “**sub**” (subspace) to the `Dataflow`
`DF1(1.0.0)`, like in the following VTL expression:

```text
‘DF1(1.0.0)/POPULATION.USA’ :=
DF1(1.0.0) [ sub INDICATOR=“POPULATION”, COUNTRY=“USA” ];

‘DF1(1.0.0)/POPULATION.CANADA’ :=
DF1(1.0.0) [ sub INDICATOR=“POPULATION”, COUNTRY=“CANADA” ];
… … …
```

In fact the VTL operator “sub” has exactly the same behaviour.
Therefore, mapping different parts of a SDMX `Dataflow` to different VTL
Data Sets in the direction from SDMX to VTL through the ordered
concatenation notation is equivalent to a proper use of the operator
`“sub”` on such a Dataflow. [^30]

[^30]:
    In case the ordered concatenation notation is used, the VTL
    Transformation described above, e.g. `‘DF1(1.0)/POPULATION.USA’ := DF1(1.0) [ sub INDICATOR=“POPULATION”, COUNTRY=“USA”]`,
    is implicitly
    executed. In order to test the overall compliance of the VTL program to
    the VTL consistency rules, it has to be considered as part of the VTL
    program even if it is not explicitly coded.

In the direction from SDMX to VTL it is allowed to omit the value of one
or more `DimensionComponents` on which the mapping is based, but
maintaining all the separating dots (therefore it may happen to find two
or more consecutive dots and dots in the beginning or in the end). The
absence of value means that for the corresponding Dimension all the
values are kept and the Dimension is not dropped.

For example, `‘DF(1.0.0)/POPULATION.’` (note the dot in the end of the
name) is the VTL dataset that contains all the observations of the
`Dataflow` `DF(1.0.0)` for which `INDICATOR = POPULATION` and `COUNTRY =` any
value.

This is equivalent to the application of the VTL `“sub”` operator only to
the identifier `INDICATOR`:

```text
‘DF1(1.0.0)/POPULATION.’ :=
DF1(1.0.0) [ sub INDICATOR=“POPULATION” ];
```

Therefore the VTL Data Set `‘DF1(1.0.0)/POPULATION.’` would have the
identifiers `COUNTRY` and `TIME_PERIOD`.

Heterogeneous invocations of the same Dataflow are allowed, i.e.
omitting different Dimensions in different invocations.

Let us now analyse **the mapping direction from VTL to SDMX**.

In this situation, distinct parts of a SDMX `Dataflow` are calculated as
distinct VTL datasets, under the constraint that they must have the same
VTL data structure.

For example, let us assume that the VTL programmer wants to calculate
the SDMX `Dataflow` `DF2(1.0.0)` having the Dimensions `TIME_PERIOD`,
`INDICATOR`, and `COUNTRY` and that such a programmer finds it convenient to
calculate separately the parts of `DF2(1.0.0)` that have different
combinations of values for `INDICATOR` and `COUNTRY`:

- each part is calculated as a VTL derived Data Set, result of a
    dedicated VTL Transformation; [^31]
- the data structure of all these VTL Data Sets has the `TIME_PERIOD`
    identifier and does not have the `INDICATOR` and `COUNTRY`
    identifiers.[^32]

[^31]:
    If the whole DF2(1.0) is calculated by means of just one VTL
    Transformation, then the mapping between the SDMX Dataflow and the
    corresponding VTL dataset is one-to-one and this kind of mapping (one
    SDMX Dataflow to many VTL datasets) does not apply.
[^32]:
    This is possible as each VTL dataset corresponds to one particular
    combination of values of INDICATOR and COUNTRY.

Under these hypothesis, such derived VTL Data Sets can be mapped to
`DF2(1.0.0)` by declaring the `DimensionComponents` `INDICATOR` and `COUNTRY` as
mapping dimensions[^33].

[^33]:
    The mapping dimensions are defined as `FromVtlSpaceKeys` of the
    `FromVtlSuperSpace` of the `VtlDataflowMapping` relevant to `DF2(1.0)`.

The corresponding VTL Transformations, assuming that the result needs to
be persistent, would be of this kind[^34]:

[^34]:
    the symbol of the VTL persistent assignment is used (`<-`)

```text
‘DF2(1.0.0)/INDICATORvalue.COUNTRYvalue’ <- expression
```

Some examples follow, for some specific values of `INDICATOR` and `COUNTRY`:

```text
‘DF2(1.0.0)/GDPPERCAPITA.USA’ <- expression11;
‘DF2(1.0.0)/GDPPERCAPITA.CANADA’ <- expression12;
… … …
‘DF2(1.0.0)/POPGROWTH.USA’ <- expression21;
‘DF2(1.0.0)/POPGROWTH.CANADA’ <- expression22;
… … …
```

As said, it is assumed that these VTL derived Data Sets have the
`TIME_PERIOD` as the only identifier. In the mapping from VTL to SMDX,
the Dimensions `INDICATOR` and `COUNTRY` are added to the VTL data structure
on order to obtain the SDMX one, with the following values respectively:

| VTL dataset | INDICATOR value | COUNTRY value |
| :---------- | :-------------- | :------------ |
| `‘DF2(1.0.0)/GDPPERCAPITA.USA’` | `GDPPERCAPITA` | `USA` |
| `‘DF2(1.0.0)/GDPPERCAPITA.CANADA’` | `GDPPERCAPITA` | `CANADA` |
| … | … | … |
| `‘DF2(1.0.0)/POPGROWTH.USA’` | `POPGROWTH` | `USA` | 
| `‘DF2(1.0.0)/POPGROWTH.CANADA’` | `POPGROWTH` | `CANADA` |
| … | … | … |

It should be noted that the application of this many-to-one mapping from
VTL to SDMX is equivalent to an appropriate sequence of VTL
Transformations. These use the VTL operator “calc” to add the proper VTL
identifiers (in the example, `INDICATOR` and `COUNTRY`) and to assign to
them the proper values and the operator “union” in order to obtain the
final VTL dataset (in the example `DF2(1.0.0)`), that can be mapped
one-to-one to the homonymous SDMX `Dataflow`. Following the same example,
these VTL Transformations would be:

```text
DF2bis_GDPPERCAPITA_USA := ‘DF2(1.0.0)/GDPPERCAPITA.USA’
            [calc identifier INDICATOR := ”GDPPERCAPITA”,
            identifier COUNTRY := ”USA”];

DF2bis_GDPPERCAPITA_CANADA := ‘DF2(1.0.0)/GDPPERCAPITA.CANADA’
            [calc identifier INDICATOR:=”GDPPERCAPITA”,
            identifier COUNTRY:=”CANADA”];
… … …
DF2bis_POPGROWTH_USA := ‘DF2(1.0.0)/POPGROWTH.USA’
            [calc identifier INDICATOR := ”POPGROWTH”, 
            identifier COUNTRY := ”USA”];

DF2bis_POPGROWTH_CANADA’ := ‘DF2(1.0.0)/POPGROWTH.CANADA’
            [calc identifier INDICATOR := ”POPGROWTH”, 
            identifier COUNTRY := ”CANADA”];
… … …
DF2(1.0) <- UNION (DF2bis_GDPPERCAPITA_USA’, 
    DF2bis_GDPPERCAPITA_CANADA’, … , 
    DF2bis_POPGROWTH_USA’, DF2bis_POPGROWTH_CANADA’ …);
```

In other words, starting from the datasets explicitly calculated through
VTL (in the example `‘DF2(1.0)/GDPPERCAPITA.USA’` and so on), the first
step consists in calculating other (non-persistent) VTL datasets (in the
example `DF2bis_GDPPERCAPITA_USA` and so on) by adding the identifiers
`INDICATOR` and `COUNTRY` with the desired values (`INDICATORvalue` and
`COUNTRYvalue`). Finally, all these non-persistent Data Sets are united
and give the final result `DF2(1.0)`[^35], which can be mapped one-to-one
to the homonymous SDMX `Dataflow` having the dimension components
`TIME_PERIOD`, `INDICATOR` and `COUNTRY`.

[^35]:
    The result is persistent in this example but it can be also non
    persistent if needed.

Therefore, mapping different VTL datasets having the same data structure
to different parts of a SDMX `Dataflow`, i.e. in the direction from VTL to
SDMX, through the ordered concatenation notation is equivalent to a
proper use of the operators “calc” and “union” on such datasets. [^36]

[^36]:
    In case the ordered concatenation notation from VTL to SDMX is
    used, the set of `Transformations` described above is implicitly
    performed; therefore, in order to test the overall compliance of the VTL
    program to the VTL consistency rules, these implicit `Transformations`
    have to be considered as part of the VTL program even if they are not
    explicitly coded.

It is worth noting that in the direction from VTL to SDMX it is
mandatory to specify the value for every Dimension on which the mapping
is based (in other word, in the name of the calculated VTL dataset is
**not** possible to omit the value of some of the Dimensions).

### Mapping variables and value domains between VTL and SDMX

With reference to the VTL “model for Variables and Value domains”, the
following additional mappings have to be considered:

| VTL | SDMX |
| :--- | :--- |
| Data Set Component | Although this abstraction exists in SDMX, it does not have an explicit definition and corresponds to a `Component` (either a `DimensionComponent` or a Measure or a `DataAttribute`) belonging to one specific Dataflow[^37] |
| Represented Variable | `Concept` with a definite Representation |
| Value Domain | `Representation` (see the Structure Pattern in the Base Package) |
| Enumerated Value Domain / Code List | `Codelist` |
| Code |`Code` (for enumerated `DimensionComponent`, Measure, `DataAttribute`) |
| Described Value Domain | non-enumerated `Representation` (having Facets / `ExtendedFacets`, see the Structure Pattern in the Base Package) |
| Value | Although this abstraction exists in SDMX, it does not have an explicit definition and corresponds to a `Code` of a Codelist (for enumerated Representations) or to a valid `value` (for non-enumerated Representations) |
| Value Domain Subset / Set | This abstraction does not exist in SDMX |
| Enumerated Value Domain Subset / Enumerated Set | This abstraction does not exist in SDMX |
| Described Value Domain Subset / Described Set | This abstraction does not exist in SDMX |
| Set list | This abstraction does not exist in SDMX |

[^37]: Through SDMX Constraints, it is possible to specify the values that a Component of a Dataflow can assume.

In the SDMX implementation of the VTL, the enumerated Value Domains are
mapped to SDMX `Codelists` through the `VtlCodelistMapping` (see the
paragraph
“[Mapping VTL Data Sets and Value Domains to SDMX artefacts](#mapping-vtl-data-sets-and-value-domains-to-sdmx-artefacts)”
above), while the Represented Variables correspond to the components
having the same names in the VTL Data Sets. The mapping of Represented
Variables to SDMX `Concepts` through the `VtlConceptMapping` has been
deprecated in SDMX 3.2.


The main difference between VTL and SDMX relies on the fact that the VTL
artefacts for defining subsets of Value Domains do not exist in SDMX,
therefore the VTL features for referring to predefined subsets are not
available in SDMX. These artefacts are the Value Domain Subset (or Set),
either enumerated or described, the Set List (list of values belonging
to enumerated subsets) and the Data Set Component (aimed at defining the
set of values that the Component of a Data Set can take, possibly a
subset of the codes of Value Domain).

Another difference consists in the fact that all Value Domains are
considered as identifiable objects in VTL either if enumerated or not,
while in SDMX the `Codelist` (corresponding to a VTL enumerated Value
Domain) is identifiable, while the SDMX non-enumerated `Representation`
(corresponding to a VTL non-enumerated Value Domain) is not
identifiable. As a consequence, the definition of the VTL Rulesets,
which in VTL can refer either to enumerated or non-enumerated value
domains, in SDMX can refer only to enumerated Value Domains (i.e. to
SDMX `Codelists`).

As for the mapping between VTL variables and SDMX `Concepts`, it should be
noted that these artefacts do not coincide perfectly. In fact, the VTL
variables are represented variables, defined always on the same Value
Domain (`“Representation”` in SDMX) independently of the data set / data
structure in which they appear[^38], while the SDMX `Concepts` can have
different `Representations` in different `DataStructures`.[^39] This means
that one SDMX `Concept` can correspond to many VTL Variables, one for each
representation the `Concept` has.

[^38]:
    By using represented variables, VTL can assume that data structures
    having the same variables as identifiers can be composed one another
    because the correspondent values can match.
[^39]:
    A `Concept` becomes a `Component` in a `DataStructureDefinition`, and
    `Components` can have different `LocalRepresentations` in different
    `DataStructureDefinitions`, also overriding the (possible) base
    representation of the Concept.

Therefore, it is important to be aware that some VTL operations (for
example the binary operations at data set level) are consistent only if
the components having the same names in the operated VTL Data Sets have
also the same representation (i.e. the same Value Domain as for VTL).
For example, it is possible to obtain correct results from the VTL
expression

```text
DS_c := DS_a + DS_b (where DS_a, DS_b, DS_c are VTL Data Sets)
```

if the matching components in `DS_a` and `DS_b` (e.g. ref_date,
geo_area, sector …) refer to the same general representation. In
simpler words, `DS_a` and `DS_b` must use the same values/codes (for
ref_date, geo_area, sector … ), otherwise the relevant values would
not match and the result of the operation would be wrong.

As mentioned, the property above is not enforced by construction in
SDMX, and different representations of the same `Concept` can be not
compatible one another (for example, it may happen that geo_area is
represented by ISO-alpha-3 codes in `DS_a` and by ISO alpha-2 codes in
`DS_b`). Therefore, it will be up to the definer of VTL Transformations
to ensure that the VTL expressions are consistent with the actual
representations of the correspondent SDMX `Concepts`.

It remains up to the SDMX-VTL definer also the assurance of the
consistency between a VTL Ruleset defined on Variables and the SDMX
`Components` on which the Ruleset is applied. In fact, a VTL Ruleset is
expressed by means of the values of the Variables (i.e. SDMX `Concepts`),
i.e. assuming definite representations for them (e.g. ISO-alpha-3 for
country). If the Ruleset is applied to SDMX `Components` that have the
same name of the `Concept` they refer to but different representations
(e.g. ISO-alpha-2 for country), the Ruleset cannot work properly.

## Mapping between SDMX and VTL Data Types

### VTL Data types

According to the VTL User Guide the possible operations in VTL depend on
the data types of the artefacts. For example, numbers can be multiplied
but text strings cannot. In the VTL Transformations, the compliance
between the operators and the data types of their operands is statically
checked, i.e., violations result in compile-time errors.

The VTL data types are sub-divided in scalar types (like integers,
strings, etc.), which are the types of the scalar values, and compound
types (like Data Sets, `Components`, Rulesets, etc.), which are the types
of the compound structures. See below the diagram of the VTL data types,
taken from the VTL User Manual:

![](media/image16.svg)
/// figure-caption | 22
VTL Data Types
///

The VTL scalar types are in turn subdivided in basic scalar types, which
are elementary (not defined in term of other data types) and Value
Domain and Set scalar types, which are defined in terms of the basic
scalar types.

The VTL basic scalar types are listed below and follow a hierarchical
structure in terms of supersets/subsets (e.g. "scalar" is the superset
of all the basic scalar types):

![](media/image17.svg)
/// figure-caption
VTL Basic Scalar Types
///

### VTL basic scalar types and SDMX data types

The VTL assumes that a basic scalar type has a unique internal
representation and can have more external representations.

The internal representation is the format used within a VTL system to
represent (and process) all the scalar values of a certain type. In
principle, this format is hidden and not necessarily known by users. The
external representations are instead the external formats of the values
of a certain basic scalar type, i.e. the formats known by the users. For
example, the internal representation of the dates can be an integer
counting the days since a predefined date (e.g. from 01/01/4713 BC up to
31/12/5874897 AD like in Postgres) while two possible external
representations are the formats `YYYY-MM-GG` and `MM-GG-YYYY` (e.g.
respectively 2010-12-31 and 12-31-2010).

The internal representation is the reference format that allows VTL to
operate on more values of the same type (for example on more dates) even
if such values have different external formats: these values are all
converted to the unique internal representation so that they can be
composed together (e.g. to find the more recent date, to find the time
span between these dates and so on).

The VTL assumes that a unique internal representation exists for each
basic scalar type but does not prescribe any particular format for it,
leaving the VTL systems free to using they preferred or already existing
internal format. By consequence, in VTL the basic scalar types are
abstractions not associated to a specific format.

SDMX data types are conceived instead to support the data exchange,
therefore they do have a format, which is known by the users and
correspond, in VTL terms, to external representations. Therefore, for
each VTL basic scalar type there can be more SDMX data types (the latter
are explained in the section "General Notes for Implementers" of this
document and are actually much more numerous than the former).

The following paragraphs describe the mapping between the SDMX data
types and the VTL basic scalar types. This mapping shall be presented in
the two directions of possible conversion, i.e. from SDMX to VTL and
vice-versa.

The conversion from SDMX to VTL happens when an SDMX artefact acts as
inputs of a VTL Transformation. As already said, in fact, at compile
time the VTL needs to know the VTL type of the operands in order to
check their compliance with the VTL operators and at runtime it must
convert the values from their external (SDMX) representations to the
corresponding internal (VTL) ones.

The opposite conversion, i.e. from VTL to SDMX, happens when a VTL
result, i.e. a VTL Data Set output of a Transformation, must become a
SDMX artefact (or part of it). The values of the VTL result must be
converted into the desired (SDMX) external representations (data types)
of the SDMX artefact.

### Mapping SDMX data types to VTL basic scalar types

The following table describes the default mapping for converting from
the SDMX data types to the VTL basic scalar types.

| SDMX data type (`BasicComponentDataType`) | Default VTL basic scalar type |
| :--- | :--- |
| `String` (string allowing any character) | `string` |
| `Alpha` (string which only allows A-z) | `string` |
| `AlphaNumeric` (string which only allows A-z and 0-9) | `string` |
| `Numeric` (string which only allows 0-9, but is not numeric so that it can have leading zeros) | `string` |
| `BigInteger` (corresponds to XML Schema `xs:integer` datatype; infinite set of integer values) | `integer` |
| `Integer` (corresponds to XML Schema `xs:int` datatype; between -2147483648 and +2147483647 (inclusive)) | `integer` |
| `Long` (corresponds to XML Schema `xs:long` datatype; between -9223372036854775808 and +9223372036854775807 (inclusive)) | `integer` |
| `Short` (corresponds to XML Schema `xs:short` datatype; between -32768 and +32767 (inclusive)) | `integer` |
| `Decimal` (corresponds to XML Schema `xs:decimal` datatype; subset of real numbers that can be represented as decimals) | `number` |
| `Float` (corresponds to XML Schema `xs:float` datatype; patterned after the IEEE single-precision 32-bit floating point type) | `number` |
| `Double` (corresponds to XML Schema `xs:double` datatype; patterned after the IEEE double-precision 64-bit floating point type) | `number` |
| `Boolean` (corresponds to the XML Schema `xs:boolean` datatype; supports the mathematical concept of binary-valued logic: {true, false}) | `boolean` |
| `URI` (corresponds to the XML Schema `xs:anyURI`; absolute or relative Uniform Resource Identifier Reference) | `string` |
| `Count` (an integer following a sequential pattern, increasing by 1 for each occurrence) | `integer` |
| `InclusiveValueRange` (decimal number within a closed interval, whose bounds are specified in the SDMX representation by the facets `minValue` and `maxValue`) | `number` |
| `ExclusiveValueRange` (decimal number within an open interval, whose bounds are specified in the SDMX representation by the facets `minValue` and `maxValue`) | `number` |
| `Incremental` (decimal number that increases by a specific interval, defined by the interval facet, typically enforced outside of the XML validation) | `number` |
| `ObservationalTimePeriod` (superset of `StandardTimePeriod` and `TimeRange`) | `time` |
| `StandardTimePeriod` (superset of `BasicTimePeriod` and `ReportingTimePeriod`) | `time` |
| `BasicTimePeriod` (superset of `GregorianTimePeriod` and `DateTime`) | `date` |
| `GregorianTimePeriod` (superset of `GregorianYear`, `GregorianYearMonth`, and `GregorianDay`) | `date` |
| `GregorianYear` (`YYYY`) | `date` |
| `GregorianYearMonth` / `GregorianMonth` (`YYYY-MM`) | `date` |
| `GregorianDay` (`YYYY-MM-DD`) | `date` |
| `ReportingTimePeriod` (superset of `ReportingYear`, `ReportingSemester`, `ReportingTrimester`, `ReportingQuarter`, `ReportingMonth`, `ReportingWeek`, `ReportingDay`) | `time_period` |
| `ReportingYear` (`YYYY-A1` – 1 year period) | `time_period` |
| `ReportingSemester` (`YYYY-Ss` – 6 month period) | `time_period` |
| `ReportingTrimester` (`YYYY-Tt` – 4 month period) | `time_period` |
| `ReportingQuarter` (`YYYY-Qq` – 3 month period) | `time_period` |
| `ReportingMonth` (`YYYY-Mmm` – 1 month period) | `time_period` |
| `ReportingWeek` (`YYYY-Www` – 7 day period; following ISO 8601 definition of a week in a year) | `time_period` |
| `ReportingDay` (`YYYY-Dddd` – 1 day period) | `time_period` |
| `DateTime` (`YYYY-MM-DDThh:mm:ss`) | `date` |
| `TimeRange` (`YYYY-MM-DD(Thh:mm:ss)?/<duration>`) | `time` |
| `Month` (`--MM`; specifies a month independent of a year) | `string` |
| `MonthDay` (`--MM-DD`; specifies a day within a month independent of a year) | `string` |
| `Day` (`---DD`; specifies a day independent of a month or year) | `string` |
| `Time` (`hh:mm:ss`; time independent of a date) | `string` |
| `Duration` (corresponds to XML Schema `xs:duration` datatype) | `duration` |
| `XHTML` | Metadata type – not applicable |
| `KeyValues` | Metadata type – not applicable |
| `IdentifiableReference` | Metadata type – not applicable |
| `DataSetReference` | Metadata type – not applicable |
/// figure-caption
Mappings from SDMX data types to VTL Basic Scalar Types
///

When VTL takes in input SDMX artefacts, it is assumed that a type
conversion according to the table above always happens. In case a
different VTL basic scalar type is desired, it can be achieved in the
VTL program taking in input the default VTL basic scalar type above and
applying to it the VTL type conversion features (see the implicit and
explicit type conversion and the "cast" operator in the VTL Reference
Manual).

### Mapping VTL basic scalar types to SDMX data types

The following table describes the default conversion from the VTL basic
scalar types to the SDMX data types .

| VTL basic scalar type | Default SDMX data type (`BasicComponentDataType`) | Default output format |
| :--- | :--- | :--- |
| `string` | `String` | Like XML (`xs:string`) |
| `number` | `Float` | Like XML (`xs:float`) |
| `integer` | `Integer` | Like XML (`xs:int`) |
| `date` | `DateTime` | `YYYY-MM-DDT00:00:00Z` |
| `time` | `StandardTimePeriod` | `<date>/<date>` (as defined above) |
| `time_period` | `ReportingTimePeriod` (`StandardReportingPeriod`) | `YYYY-Pppp` (according to SDMX) |
| `duration` | `Duration` | Like XML (`xs:duration`) `PnYnMnDTnHnMnS` |
| `boolean` | `Boolean` | Like XML (`xs:boolean`) with the values `"true"` or `"false"` |
/// figure-caption
Mappings from VTL Basic Scalar Types to SDMX data types
///

In case a different default conversion is desired, it can be achieved
through the `CustomTypeScheme` and `CustomType` artefacts (see also the
section Transformations and Expressions of the SDMX information model).

!!! note
    The custom conversions defined through the `CustomTypeScheme` and
    `CustomType` artefacts have been deprecated in SDMX 3.2; thus, the
    default conversion applies, unless the representation of the
    resulting SDMX artefact is specified in its `DataStructureDefinition`
    (see below), and explicit conversions can be expressed in the VTL
    program through the VTL `cast` operator.

The custom output formats can be specified by means of the VTL
formatting mask described in the section "Type Conversion and Formatting
Mask" of the VTL Reference Manual. Such a section describes the masks
for the VTL basic scalar types "number", "integer", "date", "time",
"time_period" and "duration" and gives examples. As for the types
"string" and "boolean" the VTL conventions are extended with some other
special characters as described in the following table.

VTL special characters for the formatting masks:

Number:

| VTL Special Character | Description |
| :---------- | :----------------------------------- |
| D | one numeric digit (if the scientific notation is adopted, D is only for the mantissa) |
| E | one numeric digit (for the exponent of the scientific notation) |
| . (dot) | possible separator between the integer and the decimal parts. |
| , (comma) | possible separator between the integer and the decimal parts. |

Time and duration: 

| VTL Special Character | Description |
| :---------- | :----------------------------------- |
| C | century |
| Y | year |
| S | semester |
| Q | quarter |
| M | month |
| W | week |
| D | day |
| h | hour digit (by default on 24 hours) |
| m | minute |
| s | second |
| d | decimal of second |
| P | period indicator (representation in one digit for the duration) |
| p | number of the periods specified in the period indicator |
| AM/PM | indicator of AM / PM (e.g. am/pm for "am" or "pm") |
| MONTH | uppercase textual representation of the month (e.g., JANUARY for January) |
| DAY | uppercase textual representation of the day (e.g., MONDAY for Monday) |
| month | lowercase textual representation of the month (e.g., january) |
| day | lowercase textual representation of the day (e.g., monday) |
| Month | First character uppercase, then lowercase textual representation of the month (e.g., January) |
| Day | First character uppercase, then lowercase textual representation of the day using (e.g. Monday) |


String:

| VTL Special Character | Description |
| :---------- | :----------------------------------- |
| X | any string character |
| Z | any string character from "A" to "z" |
| 9 | any string character from "0" to "9" |


Boolean:

| VTL Special Character | Description |
| :---------- | :----------------------------------- |
| B | Boolean using "true" for True and "false" for False |
| 1 | Boolean using "1" for True and "0" for False |
| 0 | Boolean using "0" for True and "1" for False |

Other qualifiers:

| VTL Special Character | Description |
| :---------- | :----------------------------------- |
| * | an arbitrary number of digits (of the preceding type) |
| + | at least one digit (of the preceding type) |
| ( ) | optional digits (specified within the brackets) |
| \ | prefix for the special characters that must appear in the mask |
| N | fixed number of digits used in the preceding textual representation of the month or the day |

The default conversion, either standard or customized, can be used to
deduce automatically the representation of the components of the result
of a VTL Transformation. In alternative, the representation of the
resulting SDMX Dataflow can be given explicitly by providing its
`DataStructureDefinition`. In other words, the representation specified in
the DSD, if available, overrides any default conversion[^40].

[^40]:
    The representation given in the DSD should obviously be compatible
    with the VTL data type.

### Null Values

In the conversions from SDMX to VTL it is assumed by default that a
missing value in SDMX becomes a NULL in VTL. After the conversion, the
NULLs can be manipulated through the proper VTL operators.

On the other side, the VTL programs can produce in output NULL values
for Measures and Attributes (Null values are not allowed in the
Identifiers). In the conversion from VTL to SDMX, it is assumed that a
NULL in VTL becomes a missing value in SDMX.

In the conversion from VTL to SDMX, the default assumption can be
overridden, separately for each VTL basic scalar type, by specifying
which the value that represents the NULL in SDMX is. This can be
specified in the attribute "`nullValue`" of the `CustomType` artefact (see
also the section Transformations and Expressions of the SDMX information
model). A `CustomType` belongs to a `CustomTypeScheme`, which can be
referenced by one or more `TransformationScheme` (i.e. VTL programs). The
overriding assumption is applied for all the SDMX Dataflows calculated
in the `TransformationScheme`.

!!! note
    Together with the `CustomTypeScheme`, the `nullValue` attribute of the
    `CustomType` has been deprecated in SDMX 3.2; thus, the default
    assumption applies: a NULL in VTL becomes a missing value in SDMX.

### Format of the literals used in VTL Transformations

The VTL programs can contain literals, i.e. specific values of certain
data types written directly in the VTL definitions or expressions. The
VTL does not prescribe a specific format for the literals and leave the
specific VTL systems and the definers of VTL Transformations free of
using their preferred formats.

Given this discretion, it is essential to know which are the external
representations adopted for the literals in a VTL program, in order to
interpret them correctly. For example, if the external format for the
dates is `YYYY-MM-DD` the date literal 2010-01-02 has the meaning of
2nd January 2010, instead if the external format for the
dates is `YYYY-DD-MM` the same literal has the meaning of 1st
February 2010.

Hereinafter, i.e. in the SDMX implementation of the VTL, it is assumed
that the literals are expressed according to the "default output format"
of the table of the previous paragraph ("Mapping VTL basic scalar types
to SDMX data types") unless otherwise specified.

A different format can be specified in the attribute "`vtlLiteralFormat`"
of the `CustomType` artefact (see also the section 
[Transformations and Expressions](../../information_model/information_model/14_Validation_and_Transformation_Language.md) 
of the SDMX information model).

Like in the case of the conversion of NULLs described in the previous
paragraph, the overriding assumption is applied, for a certain VTL basic
scalar type, if a value is found for the `vtlLiteralFormat` attribute of
the `CustomType` of such VTL basic scalar type. The overriding assumption
is applied for all the literals of a related VTL `TransformationScheme`.

!!! note
    Together with the `CustomTypeScheme`, the `vtlLiteralFormat` attribute
    of the `CustomType` has been deprecated in SDMX 3.2; thus, the
    literals are expressed according to the “default output format”
    mentioned above, unless a different format is specified in a VTL
    `cast` operation.

In case a literal is operand of a VTL Cast operation, the format
specified in the Cast overrides all the possible otherwise specified
formats.

## Retrieving the data of the input VTL Data Sets

### The VTL data extraction

The mappings between VTL and SDMX described above specify the data
structures of the VTL Data Sets used by a VTL program, i.e. *what* each
VTL Data Set is. In order to execute the program, the data of the input
VTL Data Sets are also needed. The `VtlDataExtraction` (see the section
of the SDMX IM relevant to the VTL) specifies *where and how* the data
of an input VTL Data Set can be obtained, typically through a query to a
web service compliant with the
[SDMX REST API](https://github.com/sdmx-twg/sdmx-rest), which returns
the SDMX data to be converted into the VTL Data Set. The query is driven
by name-value parameters, which can be fixed or overridable at run time,
so that the same `TransformationScheme` can be executed repeatedly, for
example for different periods, without changing its definition.

The `VtlDataExtraction` is optional, as it is needed neither for
defining nor for executing a VTL program: when it is not defined for an
input VTL Data Set, the data (or the information for retrieving them)
are provided to the VTL engine at run time. When it is defined, the VTL
engine can retrieve the data directly, without any additional run-time
argument (although the values of the non-fixed parameters can still be
overridden). Therefore, a `TransformationScheme` whose input VTL Data
Sets have a `VtlDataExtraction` can be executed by providing the VTL
engine only with the reference to the `TransformationScheme` and,
possibly, with the values of some parameters: the VTL engine obtains the
data structures from the SDMX artefacts referenced by the `VtlMapping`s
and the data from the `VtlDataExtraction`s.

While the mappings between VTL and SDMX are part of the public
definition of a VTL program, the `VtlDataExtraction` is rather an
execution configuration, which can be specific to an organisation or to
a system (e.g. the same data can be retrieved from different sources),
although it can refer to public web services as well.

The `VtlDataExtraction` applies only to the input VTL Data Sets, i.e. to
the `VtlDatasetMapping`s having `isInput` equal to `true`: the outputs are
produced by the VTL program and the storage of the persistent results is
up to the VTL engine. The Value Domains mapped through the
`VtlCodelistMapping` are structural metadata, whose values are obtained
from the referenced `Codelists`, therefore they do not need any
`VtlDataExtraction`.

The restriction of the data to the part of interest is expressed in the
query (e.g. through the key, the component filters or the time
parameters of the SDMX REST API), without referring to other SDMX
artefacts (e.g. `Constraints`). In this way, the `VtlDataExtraction`
replaces the deprecated mapping of parts of a `Dataflow` to distinct VTL
Data Sets (see the paragraph
“[Mapping dataflow subsets to distinct VTL Data Sets](#mapping-dataflow-subsets-to-distinct-vtl-data-sets)”
above).

### Query and URL extractions

A `VtlDataExtraction` belongs to one input `VtlDatasetMapping` and
contains zero or more `QueryParameter`s. It can take two forms, which can
be chosen for each input VTL Data Set depending on the source of its
data:

- The `QueryExtraction` is meant for web services compliant with the
    SDMX REST API. It specifies the entry point of the web service
    (`entryPoint`, e.g. `https://sdmx.example.org/rest`) and, optionally,
    the version of the SDMX REST API implemented by the entry point
    (`sdmxApiVersion`), written as major.minor (e.g. `1.5` or `2.1`),
    which determines the syntax of the query; if the `sdmxApiVersion` is
    not specified, the default version of the web service is assumed.
    The VTL engine builds the data query for the SDMX artefact referenced
    by the `sdmxUrn` of the `VtlDatasetMapping`, according to the syntax
    of the version of the SDMX REST API, by using the `QueryParameter`s:
    the parameter named `key`, if present, provides the key of the data
    query (i.e. the combination of the values of the `Dimensions`,
    possibly with wildcards), while the other parameters are added as
    query parameters (e.g. `startPeriod` and `endPeriod` in the version
    1.x of the SDMX REST API, or component filters like `c[TIME_PERIOD]`
    in the version 2.x). It should be noted that the data queries by
    `DataStructureDefinition` are defined only from the version 2.0 of
    the SDMX REST API.
- The `UrlExtraction` is meant for web services that are not (fully)
    compliant with the SDMX REST API, or for proxies. It specifies the
    complete URL of the query through a template (`urlTemplate`), whose
    tokens enclosed in curly braces (e.g. `{startPeriod}`) are replaced
    by the values of the `QueryParameter`s having the same names. Curly
    braces are used because they cannot be confused with the square
    brackets of the component filters of the SDMX REST API (e.g.
    `c[TIME_PERIOD]`), which can appear in the URL as well. Any part of
    the URL, including the entry point, can be a token.

### Query parameters and run-time values

A `QueryParameter` is a name-value pair (`name` and `value`), which can be
fixed or not (`isFixed`):

- a fixed parameter (`isFixed` equal to `true`) must have a `value`,
    which is always used as it is;
- a non-fixed parameter (`isFixed` equal to `false`) can have a `value`,
    which is a default that can be overridden at run time; a non-fixed
    parameter without `value` has no default, therefore its value must be
    provided at run time.

The names of the parameters are not predefined: they are the ones
expected by the web service (e.g. `key`, `startPeriod`, `c[TIME_PERIOD]`
or `updatedAfter`).

The values of the parameters are resolved as follows:

1. Declaration: the `VtlDataExtraction` of each input VTL Data Set lists
    its `QueryParameter`s, with their fixed values or defaults.
2. Execution: the VTL engine executes the `TransformationScheme`,
    possibly receiving at run time the values of some non-fixed
    parameters. These values are addressed to the input VTL Data Sets
    through their aliases: as the same SDMX artefact can be mapped to
    more VTL Data Sets, its URN does not identify a VTL Data Set
    univocally, while the alias does, and each `VtlDataExtraction`
    belongs to just one `VtlDatasetMapping`. How the values are passed to
    the VTL engine is not part of these specifications.
3. Resolution: the fixed parameters keep their values, while the
    non-fixed parameters take the values provided at run time or, if not
    provided, their defaults. Then, the VTL engine builds the query
    (`QueryExtraction`) or replaces the tokens of the URL template
    (`UrlExtraction`), and retrieves the data.

### Error conditions

The following error conditions are defined, distinguishing between the
ones detected when validating the definitions (i.e. on the basis of the
SDMX metadata) and the ones detected at run time (i.e. when the VTL
engine resolves the query):

| Condition | Detected at | Result |
| :--- | :--- | :--- |
| A `QueryParameter` having `isFixed` equal to `true` and no `value` | Validation | Invalid definition: a fixed parameter must have a value. |
| A `VtlDataExtraction` in a `VtlDatasetMapping` having `isInput` equal to `false` | Validation | Invalid definition: the data extractions apply only to the inputs. |
| A `VtlDatasetMapping` having `isInput` equal to `false` whose `vtlAlias` is not the result of a persistent `Transformation` | Validation | Invalid definition: the outputs must be persistent. |
| A `QueryExtraction` whose `sdmxApiVersion` is not a published version of the SDMX REST API | Validation | Invalid definition: the version of the SDMX REST API is unknown. |
| A non-fixed `QueryParameter` without `value`, whose value is not provided at run time | Run time | Error: the query cannot be built and the execution fails. |
| A token of the `urlTemplate` of a `UrlExtraction` having no `QueryParameter` with the same name | Run time | Error: the URL cannot be built and the execution fails. |

### Examples

#### Example 1: difference between two Dataflows

This example completes the `TransformationScheme` `OECD:TS_DIFF(1.0)`
described in the paragraph
“[Mapping VTL Data Sets and Value Domains to SDMX artefacts](#mapping-vtl-data-sets-and-value-domains-to-sdmx-artefacts)”.
Only the input VTL Data Sets (`ds_a` and `ds_b`) can have a
`VtlDataExtraction`; the one of `ds_a` is shown below in the two forms
(the one of `ds_b` is analogous).

As a `QueryExtraction`, assuming that the data are retrieved from a web
service implementing the version 1.5 of the SDMX REST API:

- `entryPoint`: `https://sdmx.example.org/rest`
- `sdmxApiVersion`: `1.5`
- `QueryParameter`s:

| `name` | `value` | `isFixed` |
| :--- | :--- | :--- |
| `key` | `A.USA.` | `true` |
| `startPeriod` | `2015` | `false` |
| `endPeriod` | (none) | `false` |

The fixed `key` `A.USA.` selects the annual data of the USA, for any
value of the third `Dimension` (which is wildcarded, according to the
version 1.x of the SDMX REST API, by omitting its value): the part of the
SDMX data to be processed is selected in the query, instead of through
the deprecated subspaces. The `startPeriod` has the default value `2015`,
which can be overridden at run time, while the `endPeriod` has no
default, therefore its value must be provided at run time.

As a `UrlExtraction`:

- `urlTemplate`:
    `https://sdmx.example.org/rest/data/OECD.SDD.NAD,DF_A,1.0/A.USA.?startPeriod={startPeriod}&endPeriod={endPeriod}`
- `QueryParameter`s: `startPeriod` (non-fixed, with default `2015`) and
    `endPeriod` (non-fixed, without default), which provide the values of
    the tokens having the same names; the key is already part of the URL.

The VTL engine is provided with the reference to the
`TransformationScheme` and with the following run-time values, addressed
to the input VTL Data Sets through their aliases:

| Alias | Run-time values |
| :--- | :--- |
| `ds_a` | `startPeriod` = `2020`, `endPeriod` = `2023` |
| `ds_b` | `startPeriod` = `2020`, `endPeriod` = `2023` |

For `ds_a`, the fixed `key` is kept, while the `startPeriod` and the
`endPeriod` take the values provided at run time (the former overriding
the default `2015`). Therefore, in both forms, the VTL engine retrieves
the data of `ds_a` through the following query:

```text
https://sdmx.example.org/rest/data/OECD.SDD.NAD,DF_A,1.0/A.USA.?startPeriod=2020&endPeriod=2023
```

Similarly, it retrieves the data of `ds_b`, then it calculates `diff`
and, as this is a persistent output (`isInput` equal to `false`), it
stores the result as data of the `Dataflow` `OECD.SDD.NAD:DF_DIFF(1.0)`.

#### Example 2: two VTL Data Sets mapped to the same Data Structure Definition

The following `TransformationScheme` `ESTAT:TS_POPRATIO(1.0)`, whose
`vtlVersion` is “2.1”, calculates the ratio between the male and the
female population:

```text
ratio <- pop_m [ sub SEX = "M" ] / pop_f [ sub SEX = "F" ];
```

The two input VTL Data Sets are mapped to the same
`DataStructureDefinition` `ESTAT:POP(1.0.0)`, having the `Dimensions`
`REF_AREA`, `SEX` and `AGE`, the `TimeDimension` `TIME_PERIOD` and the
`Measure` `OBS_VALUE`:

| `vtlAlias` | `sdmxUrn` | `isInput` |
| :--- | :--- | :--- |
| `pop_m` | `urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=ESTAT:POP(1.0.0)` | `true` |
| `pop_f` | `urn:sdmx:org.sdmx.infomodel.datastructure.DataStructure=ESTAT:POP(1.0.0)` | `true` |
| `ratio` | `urn:sdmx:org.sdmx.infomodel.datastructure.Dataflow=ESTAT:DF_POPRATIO(1.0.0)` | `false` |

This is allowed because the mapping is many-to-many and a
`VtlDatasetMapping` can reference a `DataStructureDefinition`: `pop_m` and
`pop_f` are distinct VTL Data Sets, distinguished only by their aliases.

Each input has a `QueryExtraction` on a web service implementing the
version 2.1 of the SDMX REST API (`entryPoint`
`https://sdmx.example.org/rest`, `sdmxApiVersion` `2.1`), with a
different fixed `key` and the same non-fixed component filter on the
time period:

| Alias | Fixed `key` | Part of the data | Non-fixed parameter |
| :--- | :--- | :--- | :--- |
| `pop_m` | `*.M.*` | the male population | `c[TIME_PERIOD]`, default `ge:2010` |
| `pop_f` | `*.F.*` | the female population | `c[TIME_PERIOD]`, default `ge:2010` |

The `sub` clauses drop the `SEX` Identifier, whose value is fixed in each
input by the key: without them, the division would not match any data
points, because VTL composes the data points having the same values for
all the Identifiers, while `SEX` is equal to `M` in `pop_m` and to `F` in
`pop_f`. The key restricts the data in the query, while `sub` removes the
Identifier in VTL: together, they achieve what the deprecated subspaces
did.

As the two inputs reference the same URN, the run-time values must be
addressed to them through their aliases, for example:

| Alias | Run-time values |
| :--- | :--- |
| `pop_m` | `c[TIME_PERIOD]` = `ge:2015` |
| `pop_f` | `c[TIME_PERIOD]` = `ge:2015` |

The VTL engine retrieves the data through the following queries, then
it calculates `ratio` and stores it as data of the `Dataflow`
`ESTAT:DF_POPRATIO(1.0.0)`, whose data structure has the `Dimensions`
`REF_AREA` and `AGE`, the `TimeDimension` `TIME_PERIOD` and the `Measure`
`OBS_VALUE`:

```text
https://sdmx.example.org/rest/data/datastructure/ESTAT/POP/1.0.0/*.M.*?c[TIME_PERIOD]=ge:2015
https://sdmx.example.org/rest/data/datastructure/ESTAT/POP/1.0.0/*.F.*?c[TIME_PERIOD]=ge:2015
```

## Conversion of definitions based on deprecated constructs

The constructs deprecated in SDMX 3.2 can still be found in existing
definitions, but they should not be used in new ones. The following
table describes how the information conveyed by the deprecated
constructs (SDMX 3.0 and 3.1 representation) is represented in the
simplified model (SDMX 3.2 representation):

| Deprecated construct (SDMX 3.0 and 3.1) | Representation in SDMX 3.2 |
| :--- | :--- |
| `VtlDataflowMapping` | A `VtlDatasetMapping` whose `sdmxUrn` is the URN of the `Dataflow`. The class of the mapping changes, and so does its URN. |
| `dataflowAlias`, `codelistAlias`, `conceptAlias` | The `vtlAlias` of the `VtlMapping`. |
| Direction of the `VtlDataflowMapping` | The `isInput` attribute of the `VtlDatasetMapping`: `false` if the alias is the result of a (persistent) `Transformation`, as indicated by a `fromVtlMappingMethod` if specified, `true` if it is only used as an operand, as indicated by a `toVtlMappingMethod` if specified. An alias used in both ways (e.g. by different `TransformationScheme`s sharing the same `VtlMappingScheme`) becomes two `VtlDatasetMapping`s with distinct aliases, and the VTL programs are adapted accordingly. |
| `toVtlMappingMethod`, `fromVtlMappingMethod` and the conventional "generic_dataflow" | No attribute: the Basic mapping always applies. Where a different method was specified, the corresponding restructuring is performed in the VTL program (e.g. through the `pivot`, `unpivot` or `calc` clauses). |
| `ToVtlSubspace` and `ToVtlSpaceKey` (ordered concatenation notation from SDMX to VTL) | A distinct input `VtlDatasetMapping` for each part of the `Dataflow`, with a user-defined alias. The part of the data is selected through the `QueryParameter`s of its `VtlDataExtraction` (e.g. a fixed `key` with the values of the mapping `Dimensions` and wildcards for the others) and the mapping `Dimensions` are dropped in the VTL program through the `sub` clause. |
| `FromVtlSuperspace` and `FromVtlSpaceKey` (ordered concatenation notation from VTL to SDMX) | The VTL program adds the mapping `Dimensions` to the VTL Data Sets through the `calc` clause and combines them through the `union` operator; the result is mapped to the `Dataflow` through a `VtlDatasetMapping` having `isInput` equal to `false`. |
| `VtlConceptMapping` | No mapping: the VTL Variables correspond to the components having the same names in the VTL Data Sets. |
| `NamePersonalisationScheme` and `NamePersonalisation` | The desired names are assigned in the VTL program (e.g. through the `rename` clause). |
| `CustomTypeScheme` and `CustomType` | The representation of an output is the one defined in the `DataStructureDefinition` of the referenced SDMX artefact; explicit conversions are expressed in the VTL program through the `cast` operator; the default rules apply to the NULLs and to the format of the literals. |
| A VTL scheme without `vtlVersion` | The `vtlVersion` is set to the version of the VTL in which its definitions are written. |
| References to SDMX artefacts through their URN or abbreviated URN in the VTL statements | User-defined aliases, mapped to the URNs of the SDMX artefacts through `VtlMapping`s. |
