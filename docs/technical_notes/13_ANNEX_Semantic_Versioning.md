# ANNEX Semantic Versioning

## Introduction to Semantic Versioning

In the world of versioned data modelling exists a dreaded place called
"dependency hell." The bigger your data model through organisational,
national or international harmonisation grows and the more artefacts you
integrate into your modelling, the more likely you are to find yourself,
one day, in this pit of despair.

In systems with many dependencies, releasing new artefact versions can
quickly become a nightmare. If the dependency specifications are too
tight, you are in danger of version lock (the inability to upgrade an
artefact without having to release new versions of every dependent
artefact). If dependencies are specified too loosely, you will
inevitably be bitten by version promiscuity (assuming compatibility with
more future versions than is reasonable). Dependency hell is where you
are when version lock and/or version promiscuity prevent you from easily
and safely moving your data modelling forward.

As a very successful solution to the similar problem in software
development, "Semantic Versioning" [semver.org](http://semver.org/)
proposes a simple set of rules and requirements that dictate how version
numbers are assigned and incremented. These rules make also perfect
sense in the world of versioned data modelling and help to solve the
"dependency hell" encountered with previous versions of SDMX. SDMX 3.0
applies thus the Semantic Versioning rules on all versioned SDMX
artefacts. Once you release a versioned SDMX artefact, you communicate
changes to it with specific increments to your version number.

**This SDMX 3.0(.0) specification inherits the original
[semver.org](https://semver.org/) 2.0.0 wording (license: [Creative
Commons - CC BY 3.0](http://creativecommons.org/licenses/by/3.0/)) and
applies it to versioned SDMX structural artefacts.** Under this scheme,
version numbers and the way they change convey meaning about the
underlying data structures and what has been modified from one version
to the next.

## Semantic Versioning Specification for SDMX 3.0(.0)

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this
document are to be interpreted as described in RFC 2119.

In the following, "versioned" artefacts are understood to be
semantically versioned SDMX structural artefacts, and X, Y, Z and EXT
are understood as placeholders for the version parts MAJOR, MINOR,
PATCH, and EXTENSION, as defined in chapter 4.3.

The following rules apply to versioned artefacts:

- All versioned SDMX artefacts MUST specify a version number.
- The version number of immutable versioned SDMX artefacts MUST take
    the form `X.Y.Z` where `X`, `Y`, and `Z` are non-negative integers and MUST
    NOT contain leading zeroes. `X` is the MAJOR version, `Y` is the MINOR
    version, and `Z` is the PATCH version. Each element MUST increase
    numerically. For instance: `1.9.0 → 1.10.0 → 1.11.0`.
- Once an SDMX artefact with an `X.Y.Z` version has been shared
    externally or publicly released, the contents of that version MUST
    NOT be modified. That artefact version is considered stable. Any
    modifications MUST be released as a new version.
- MAJOR version zero `(0.y.z)` is for initial modelling. Anything MAY
    change at any time. The externally released or public artefact
    SHOULD NOT be considered stable.
- Version `1.0.0` defines the first stable artefact. The way in which
    the version number is incremented after this release is dependent on
    how this externally released or public artefact changes.
- PATCH version `Z` `(x.y.Z | x > 0)` MUST be incremented if only
    backwards compatible property changes are introduced. A property
    change is defined as an internal change that does not affect the
    relationship to other artefacts. These are changes in the artefact's
    or artefact element's names, descriptions and annotations that MUST
    NOT alter their meaning.
- MINOR version `Y` `(x.Y.z | x > 0)` MUST be incremented if a new,
    backwards compatible element is introduced to a stable artefact.
    These are additional items in ItemScheme artefacts. It MAY be
    incremented if substantial new information is introduced within the
    artefact's properties. It MAY include PATCH level changes. PATCH
    version MUST be reset to 0 when MINOR version is incremented.
- MAJOR version `X` `(X.y.z | X > 0)` MUST be incremented if any
    backwards incompatible changes are introduced to a stable artefact.
    These often relate to deletions of items in ItemSchemes or to
    backwards incompatibility introduced due to changes in references to
    other artefacts. A MAJOR version change MAY also include MINOR and
    PATCH level changes. PATCH and MINOR version MUST be reset to 0 when
    MAJOR version is incremented.
- A mutable version, e.g. used for externally released or public
    drafts or as pre-release, MUST be denoted by appending an EXTENSION
    that consists of a hyphen and a series of dot separated identifiers
    immediately following the PATCH version `(x.y.z-EXT)`. Identifiers
    MUST comprise only ASCII alphanumerics and hyphen `[0-9A-Za-z-]`.
    Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include
    leading zeroes. However, to foster harmonisation and general
    comprehension it is generally recommended to use the standard
    EXTENSION `-draft`. Extended versions have a lower precedence
    than the associated stable version. An extended version indicates
    that the version is unstable and it might not satisfy the intended
    compatibility requirements as denoted by its associated stable
    version. When making changes to an SDMX artefact with an extended
    version number then one is not required to increment the version if
    those changes are kept within the allowed scope of the version
    increment from the previous version (if that existed), otherwise
    also here the before mentioned version increment rules for `X.Y.Z`
    apply. Concretely, a version X.0.0-EXT will allow for any changes, a
    version `X.Y.0-EXT` will allow only for MINOR changes and a version
    `X.Y.Z-EXT` will allow only for any PATCH changes, as defined above.
    EXTENSION examples: `1.0.0-draft`, `1.0.0-draft.1`, `1.0.0-0.3.7`,
    `1.0.0-x.7.z.92`.
- Precedence refers to how versions are compared to each other when
    ordered. Precedence MUST be calculated by separating the version
    into MAJOR, MINOR, PATCH and EXTENSION identifiers in that order.
    Precedence is determined by the first difference when comparing each
    of these identifiers from left to right as follows: MAJOR, MINOR,
    and PATCH versions are always compared numerically. Example: 
    `1.0.0 < 2.0.0 < 2.1.0 < 2.1.1`. When MAJOR, MINOR, and PATCH are
    equal, an extended version has lower precedence than a stable
    version. Example: `1.0.0-draft < 1.0.0`. Precedence for two
    extended versions with the same MAJOR, MINOR, and PATCH version MUST
    be determined by comparing each dot separated identifier from left
    to right until a difference is found as follows: identifiers
    consisting of only digits are compared numerically and identifiers
    with letters or hyphens are compared lexically in ASCII sort order.
    Numeric identifiers always have lower precedence than non-numeric
    identifiers. A larger set of EXTENSION fields has a higher
    precedence than a smaller set, if all of the preceding identifiers
    are equal. Example: 
    `1.0.0-draft < 1.0.0-draft.1 < 1.0.0-draft.prerelease < 1.0.0-prerelease < 1.0.0-prerelease.2 < 1.0.0-prerelease.11 < 1.0.0-rc.1 < 1.0.0`.
- The reasons for version changes MAY be documented in brief form in
    an artefact's annotation of type "CHANGELOG".

## Backus–Naur Form Grammar for Valid SDMX 3.0(.0) Semantic Versions

```xml
<valid semver> ::= <version core>
                 | <version core> "-" <extension>

<version core> ::= <major> "." <minor> "." <patch>

<major> ::= <numeric identifier>
<minor> ::= <numeric identifier>
<patch> ::= <numeric identifier>

<extension> ::= <dot-separated extension identifiers>

<dot-separated extension identifiers> ::= <extension identifier>
                                        | <extension identifier> "." <dot-separated extension identifiers>

<extension identifier> ::= <alphanumeric identifier>
                         | <numeric identifier>**

<alphanumeric identifier> ::= <non-digit>
                            | <non-digit> <identifier characters>
                            | <identifier characters> <non-digit>
                            | <identifier characters> <non-digit> <identifier characters>
                            
<numeric identifier> ::= "0"
                       | <positive digit>
                       | <positive digit> <digits>

<identifier characters> ::= <identifier character>
                          | <identifier character> <identifier characters>

<identifier character> ::= <digit>
                         | <non-digit>

<non-digit> ::= <letter>
              | "-"

<digits> ::= <digit>
           | <digit> <digits>

<digit> ::= "0"
          | <positive digit>

<positive digit> ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"

<letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J" | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T" | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n" | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x" | "y" | "z"
```

## Dependency Management in SDMX 3.0(.0)

MAJOR, MINOR or PATCH version parts in SDMX 3.0 artefact references CAN
be wildcarded using "+" as extension:

- `X+.Y.Z` means the currently latest available version `>= X.Y.Z`
    - Example: `2+.3.1` means the currently latest available version
        `>= 2.3.1` (even if not backwards compatible)
    - Typical use case: references in SDMX Categorisations
- `X.Y+.Z` means the currently latest available backwards compatible
    version `>= X.Y.Z`
    - Example: `2.3+.1` means the currently latest available version
        `>= 2.3.1 and 3.0.0` (all backwards compatible
        versions `>= 2.3.1`)
    - Typical use case: references in SDMX DSD

- `X.Y.Z+` means the currently latest available forwards and backwards
    compatible version `>= X.Y.Z`
    - Example: `2.3.1+` means the currently latest available version
        `>= 2.3.1 and < 2.4.0` (all forwards and backwards
        compatible versions `>= 2.3.1`)

- Non-versioned and 2-digit version SDMX structural artefacts CAN
    reference any other non-versioned or versioned (whether SemVer or
    not) SDMX structural artefacts.
- Semantically versioned artefacts MUST only reference other
    semantically versioned artefacts.
- Wildcarded references in a stable artefact implicitly target only
    future stable versions of the referenced artefacts within the
    defined wildcard scope.
    - Example: The reference to `AGENCY_ID:CODELIST_ID(2.3+.1)` in
        an artefact `AGENCY_ID:DSD_ID(2.2.1)` resolves to artefact
        `AGENCY_ID:CODELIST_ID(2.4.3)` if that was currently the
        latest available stable version.

- Wildcarded references in a version-extended artefact implicitly
    target future stable and version-extended versions of the referenced
    artefacts within the defined wildcard scope.
    - Example: The reference to `AGENCY_ID:CODELIST_ID(2.3+.1)` in
        an artefact `AGENCY_ID:DSD_ID(2.2.1-draft)` resolves to
        artefact `AGENCY_ID:CODELIST_ID(2.5.0-draft)` if that was
        currently the latest available version.

- References to specific version-extended artefacts MAY be used, but those cannot be combined with a wildcard.
    - Example: The reference to `AGENCY_ID:CODELIST_ID(2.5.0-draft)`
        in an artefact `AGENCY_ID:DSD_ID(2.2.1)` resolves to artefact
        `AGENCY_ID:CODELIST_ID(2.5.0-draft)`, which might be subject
        to continued backwards compatible changes.

Because both, wildcarded references and references to version-extended
artefacts, allow for changes in the referenced artefacts, care needs to
be taken when choosing the appropriate references in order to achieve
the required limitation in the allowed scope of changes.

For references to non-dependent artefacts, MAJOR, MINOR or PATCH version
parts in SDMX 3.0 artefact references CAN alternatively be wildcarded
using "\*" as replacement:

\* means all available versions

## Upgrade and conversions of artefacts defined with previous SDMX standard versions to Semantic Versioning

Because SDMX standardises the interactions between statistical systems,
which cannot all be upgraded at the same time, the new versioning rules
cannot be applied to existing artefacts in EDIFACT, SDMX 1.0, 2.0 or
2.1. SemVer can only be applied to structural artefacts that are newly
modelled with the SDMX 3.0 Information Model. Migrating to SemVer means
migrating to the SDMX 3.0 Information Model, to its new API version and
new versions of its exchange message formats.

To migrate SDMX structural artefacts created previously to SDMX 3.0.0:

If the artefacts do not need versioning, then the new artefacts based on
the SDMX 3.0 Information Model SHOULD remain as-is, e.g., a previous
artefact with the non-final version 1.0 and that doesn't need versioning
becomes non-versioned, i.e., keeps version 1.0. This will be the case
for all AgencyScheme artefacts.

If artefact versioning is required and SDMX 3.0.0 Semantic Versioning is
available within the tools and processes used, then it is recommended to
switch to Semantic Versioning with the following steps:

1. Complement the missing version parts with 0s to make the version
    number SemVer-compliant using the MAJOR.MINOR.PATCH-EXTENSION syntax:

    Example: Version 2 becomes version 2.0.0 and version 3.1 becomes
    version 3.1.0.

2. Replace the "isFinal=false" property by the version extensions
    "-draft" (or alternatively "-unstable" or "-nonfinal" depending on
    the use case).

    Example: Version 1.3 with isFinal=true becomes version 1.3.0 and
    version 1.3 with isFinal=false becomes version 1.3.0-draft.

If artefact versioning is required but semantic versioning cannot be
applied, then version strings used in previous versions of the Standard
(e.g., version=1.2) may continue to be used.

Note: Like for other not fully backwards compatible SDMX 3.0 features,
also some cases of semantically versioned SDMX 3.0 artefacts cannot be
converted back to earlier SDMX versions. This is the case when one or
more extensions have been created in parallel to the corresponding
stable version. In this case, only the stable version SHOULD be
converted to a final version (e.g., 3.2.1 becomes 3.2.1 final, and
3.2.1-draft cannot be converted back).

## FAQ for Semantic Versioning

**My organisation is new to SDMX and starts to implement 3.0 or starts
to implement a new process fully based on SDMX 3.0. Which versioning
scheme should be used?**

If all counterparts involved in the process and all tools used for its
implementation are SDMX 3.0-ready, then it is recommended to:

- in general, use semantic versioning;
- exceptionally, do not use versioning for artefacts that do not
    require it, e.g. artefacts that never change, that are only used
    internally or for which communication on changes with external
    parties or systems is not required.

**How should I deal with revisions in the 0.y.z initial modelling
phase?**

The simplest thing to do is start your initial modelling release at
0.1.0 and then increment the minor version for each subsequent release.

**How do I know when to release 1.0.0?**

If your data model is being used in production, it should probably
already be 1.0.0. If you have a stable artefact on which users have come
to depend, you should be 1.0.0. If you're worrying a lot about backwards
compatibility, you should probably already be 1.0.0.

**Doesn't this discourage rapid modelling and fast iteration?**

Major version zero is all about rapid modelling. If you're changing the
artefact every day you should either still be in version 0.y.z or on the
next (minor or) major version for a separate modelling.

**If even the tiniest backwards incompatible changes to the public
artefact require a major version bump, won't I end up at version 42.0.0
very rapidly?**

This is a question of responsible modelling and foresight. Incompatible
changes should not be introduced lightly to a data model that has a lot
of dependencies. The cost that must be incurred to upgrade can be
significant. Having to bump major versions to release incompatible
changes means you will think through the impact of your changes, and
evaluate the cost/benefit ratio involved.

**Documenting the version changes in an artefact's annotation of type
"CHANGELOG" is too much work!**

It is your responsibility as a professional modeller to properly
document the artefacts that are intended for use by others. Managing
data model complexity is a hugely important part of keeping a project
efficient, and that's hard to do if nobody knows how to use your data
model, or what artefacts are safe to reuse. In the long run, SDMX 3.0
Semantic Versioning can keep everyone and everything running smoothly.

However, refrain from overdoing. Nobody can and will read too long lists
of changes. Thus, keep it to the absolute essence, and mainly use it for
short announcements. You can even skip the changelog if the change is
impact-less. For all complete reports, a new API feature could be more
useful to automatically generate a log of differences between two
versions.

**What do I do if I accidentally release a backwards incompatible change
as a minor version?**

As soon as you realise that you've broken the SDMX 3.0 Semantic
Versioning specification, fix the problem and release a new minor
version that corrects the problem and restores backwards compatibility.
Even under this circumstance, it is unacceptable to modify versioned
releases. If it's appropriate, document the offending version and inform
your users of the problem so that they are aware of the offending
version.

**What if I inadvertently alter the public artefact in a way that is not
compliant with the version number change (i.e. the modification
incorrectly introduces a major breaking change in a patch release)?**

Use your best judgement. If you have a huge audience that will be
drastically impacted by changing the behaviour back to what the public
artefact intended, then it may be best to perform a major version
release, even though the property change could strictly be considered a
patch release. Remember, SDMX 3.0.0 Semantic Versioning is all about
conveying meaning by how the version number changes. If these changes
are important to your users, use the version number to inform them.

**How should I handle deprecating elements?**

Deprecating existing elements is a normal part of data modelling and is
often required to make forward progress or follow history (changing
classifications, evolving reference areas). When you deprecate part of
your stable artefact, you should issue a new minor version with the
deprecation in place (e.g. add the new country code but still keep the
old country code) and with a "CHANGELOG" annotation announcing the
deprecation (e.g. the intention to remove the old country code in a
future version) . Before you completely remove the functionality in a
new major release there should be at least one minor release that
contains the deprecation so that users can smoothly transition to the
new artefact.

**Does SDMX 3.0.0 Semantic Versioning have a size limit on the version
string?**

No, but use good judgement. A 255 character version string is probably
overkill, for example. In addition, specific SDMX implementations may
impose their own limits on the size of the string. Remember, it is
generally recommended to use the standard extension "-draft".

**Is "v1.2.3" a semantic version?**

No, `v1.2.3` is not a semantic version. The semantic version is `1.2.3`.

**Is there a suggested regular expression (RegEx) to check an SDMX 3.0.0
Semantic Versioning string?**

There are two:

One with named groups for those systems that support them (PCRE \[Perl
Compatible Regular Expressions, i.e. Perl, PHP and R\], Python and Go).

Reduced version (without original SemVer "build metadata") from:
<https://regex101.com/r/Ly7O1x/3/>

```xml
^(?P&lt;major>0|\[1-9\]\d\*)\\(?P&lt;minor>0|\[1-9\]\d\*)\\(?P&lt;patch>0|\[1-9\]\d\*)(?:-(?P&lt;extension>(?:0|\[1-9\]\d\*|\d\*\[a-zA-Z-\]\[0-9a-zA-Z-\]\*)(?:\\(?:0|\[1-9\]\d\*|\d\*\[a-zA-Z-\]\[0-9a-zA-Z-\]\*))\*))?$
```

And one with numbered capture groups instead (so cg1 = major, cg2 =
minor, cg3 = patch and cg4 = extension) that is compatible with ECMA
Script (JavaScript), PCRE (Perl Compatible Regular Expressions, i.e.
Perl, PHP and R), Python and Go.

Reduced version (without original SemVer "build metadata") from:
<https://regex101.com/r/vkijKf/1/>

```xml
^(0|\[1-9\]\d\*)\\(0|\[1-9\]\d\*)\\(0|\[1-9\]\d\*)(?:-((?:0|\[1-9\]\d\*|\d\*\[a-zA-Z-\]\[0-9a-zA-Z-\]\*)(?:\\(?:0|\[1-9\]\d\*|\d\*\[a-zA-Z-\]\[0-9a-zA-Z-\]\*))\*))?$
```

**Must I adopt semantic versioning rules when switching to SDMX 3.0?**

No. If backwards compatibility with pre-existing tools and processes is
required, then it is possible to continue using the previous versioning
scheme (with up to two version parts MAJOR.MINOR). Semantic versioning
is indicated only for those use cases where a proper artefact versioning
is required. If versioning does not apply to some or all of your
artefacts, then rather migrate to non-versioned SDMX 3.0 artefacts.

**May I mix artefacts that follow semantic versioning with artefacts
that don't?**

Artefacts that are not (semantically) versioned may reference artefacts
that are semantically versioned, but those are fully safe to use only
when not extended. However, the reverse is not true:
non-semantically-versioned artefacts do not offer change guarantees,
and, therefore, should not be referenced by semantically versioned
artefacts.

**I have plenty of artefacts. I'm happy with my current versioning
policy and I don't want to use SemVer! Can I still migrate to SDMX 3.0,
and if so, what do I need to do?**

Yes, of course, you can. The introduction of semantic versioning is done
in a way which is largely backward compatible with previous versions of
the standard, so you can keep your existing 2-digit version numbers
(1.0, 1.1, 2.0, etc.) if that is required by your current tools and
processes. However, if not using SemVer then pre-SDMX 3.0 final
artefacts will be migrated as non-final and mutable in SDMX 3.0. There
are also many good reasons to move to SemVer, and the migration is
encouraged. Be assured that there will be tools out there that will
assist you doing this in an efficient and convenient way.

**I have plenty of artefacts versioned `X.Y`. I want to make some of
them immutable, and enjoy the benefits provided by semantic versioning.
Some other artefacts however must remain mutable (i.e. non final).
However, in both cases, I'd like adopt the semantic versioning. What do
I need to do?**

For artefacts that will be made immutable and are therefore safe to use,
simply append a '.0' to the current version (use `X.Y.0`) when migrating
to Semantic Versioning. E.g., if the version of your artefact is
currently 1.10, then migrate to 1.10.0.

For artefacts that remain mutable, and therefore do not bring the
guarantees of semantic versioning, if you want to benefit from the
advantages of semantic versioning, then simply append `.0-notfinal` to
the version string. So, if the version of your artefact is currently
`1.10`, use `1.10.0-notfinal` instead. Indeed, other extensions can be used
depending on your use case.

**I have adopted SDMX 3.0 with the semantic versioning conventions for
the version strings of all my artefacts, regardless of whether these are
stable (e.g. `1.0.0`) or unstable (e.g. `1.0.0-notfinal`, `1.0.0-draft`,
etc.). However, I still receive artefacts from organizations that have
not yet adopted SemVer conventions for the version strings. How should I
treat these?**

The only artefacts that are safe to use, are those that are semantically
versioned. Starting with SDMX 3.0, these artefacts MUST use the SEMVER
version string to indicate this fact and the version string of these
artefacts MUST be expressed as `X.Y.Z` (e.g. `2.1.0`). Extended versions
bring some limited guarantees for changes.

All other artefacts are in principle unsafe. They might be safe in
practice but the SDMX standard does not bring any guarantees in that
respect, and these artefacts may change in unpredictable ways.

In practice, the migration approach will often mirror the way in which
organisations have migrated between earlier SDMX versions. Rarely, the
new data models used mixed SDMX standard versions in their dependencies,
and if they did then standard conversions were put in place. A typical
method is to first migrate the re-used artefacts from the previous SDMX
version to SDMX 3.0 and while doing so to apply the appropriate new
semantic version string. From that point onwards, you can enjoy the
advantages of the new SDMX versioning features for all those artefacts
that require appropriate versioning.
