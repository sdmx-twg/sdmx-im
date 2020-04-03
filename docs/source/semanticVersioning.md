SDMX 3.0(.0) - Semantic Versioning & Dependency Management
==========================================================

## Summary

Given a version number MAJOR.MINOR.PATCH, when updating an SDMX artefact increment the:  

1) MAJOR version when you make incompatible artefact changes,  
1) MINOR version when you add artefact elements in a backwards compatible manner, and  
1) PATCH version when you make backwards compatible artefact property changes.   
Additional labels for pre-release are available as extensions to the MAJOR.MINOR.PATCH format.

New flexible dependency specifications through wildcarding allow for easier data model maintenance and enhancements.

## Introduction

In the world of data modelling there exists a dreaded place called “dependency hell.” The bigger your data model through organisational, national or international harmonisation grows and the more artefacts you integrate into your modelling, the more likely you are to find yourself, one day, in this pit of despair.

In systems with many dependencies, releasing new artefact versions can quickly become a nightmare. If the dependency specifications are too tight, you are in danger of version lock (the inability to upgrade a artefact without having to release new versions of every dependent artefact). If dependencies are specified too loosely, you will inevitably be bitten by version promiscuity (assuming compatibility with more future versions than is reasonable). Dependency hell is where you are when version lock and/or version promiscuity prevent you from easily and safely moving your data modelling forward.

As a very successful solution to the similar problem in software development, “Semantic Versioning" [semver.org](https://semver.org/) proposes a simple set of rules and requirements that dictate how version numbers are assigned and incremented. These rules make also perfect sense in the world of data modelling, and help to solve the “dependency hell” encountered with previous versions of SDMX. SDMX 3.0.0 applies thus the Semantic Versioning rules on all SDMX artefacts. Once you release an SDMX artefact, you communicate changes to it with specific increments to your version number. Consider a version format of X.Y.Z (Major.Minor.Patch). Property changes not affecting the artefact compatibility increment the patch version, backwards compatible artefact element additions/changes increment the minor version, and backwards incompatible artefact changes increment the major version.

**This SDMX 3.0.0 specification inherits the original [semver.org](https://semver.org/) 2.0.0 wording (license: [Creative Commons - CC BY 3.0](http://creativecommons.org/licenses/by/3.0/)) and applies it to SDMX artefacts.** Under this scheme, version numbers and the way they change convey meaning about the underlying data structures and what has been modified from one version to the next.

## SDMX 3.0.0 Semantic Versioning Specification

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

1) All versionable SDMX artefacts MUST specify a version number.
1) A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.
1) Once a versioned artefact has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.
1) Major version zero (0.y.z) is for initial modelling. Anything MAY change at any time. The public artefact SHOULD NOT be considered stable.
1) Version 1.0.0 defines the public artefact. The way in which the version number is incremented after this release is dependent on this public artefact and how it changes.
1) Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible property changes are introduced. A property change is defined as an internal change that does not affect the relationship to other artefacts. These are changes in the artefact's or artefact element's names, descriptions and annotations that MUST NOT alter their meaning.
1) Minor version Y (x.Y.z | x > 0) MUST be incremented if a new, backwards compatible element is introduced to the public artefact. These are additional items in ItemScheme artefacts. <It MUST be incremented if any public artefact element is marked as deprecated.> It MAY be incremented if substantial new information is introduced within the artefact's properties. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.
1) Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public artefact. These often relate to deletions of items in ItemSchemes or to backwards incompatibility introduced due to changes in references to other artefacts. A major version change MAY also include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.
1) A public pre-release version MUST be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version (x.y.z-EXT). Identifiers MUST comprise only ASCII alphanumerics and hyphen [0-9A-Za-z-]. Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes. However, **to foster harmonisation and general comprehension it is generally recommended to use the standard extension "-draft".** Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples: 1.0.0-draft, 1.0.0-draft.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92.
1) Precedence refers to how versions are compared to each other when ordered. Precedence MUST be calculated by separating the version into major, minor, patch and pre-release identifiers in that order. Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: Major, minor, and patch versions are always compared numerically. Example: 1.0.0 < 2.0.0 < 2.1.0 < 2.1.1. When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version. Example: 1.0.0-draft < 1.0.0. Precedence for two pre-release versions with the same major, minor, and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows: identifiers consisting of only digits are compared numerically and identifiers with letters or hyphens are compared lexically in ASCII sort order. Numeric identifiers always have lower precedence than non-numeric identifiers. A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal. Example: 1.0.0-draft < 1.0.0-draft.1 < 1.0.0-draft.prerelease < 1.0.0-prerelease < 1.0.0-prerelease.2 < 1.0.0-prerelease.11 < 1.0.0-rc.1 < 1.0.0.
1) The reasons for version changes SHOULD be documented in an artefact's annotation of type "CHANGELOG".

## Backus–Naur Form Grammar for Valid SDMX 3.0.0 Semantic Versions

```
<valid semver> ::= <version core>
                 | <version core> "-" <pre-release>

<version core> ::= <major> "." <minor> "." <patch>

<major> ::= <numeric identifier>

<minor> ::= <numeric identifier>

<patch> ::= <numeric identifier>

<pre-release> ::= <dot-separated pre-release identifiers>

<dot-separated pre-release identifiers> ::= <pre-release identifier>
                                          | <pre-release identifier> "." <dot-separated pre-release identifiers>

<pre-release identifier> ::= <alphanumeric identifier>
                           | <numeric identifier>

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

<letter> ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "I" | "J"
           | "K" | "L" | "M" | "N" | "O" | "P" | "Q" | "R" | "S" | "T"
           | "U" | "V" | "W" | "X" | "Y" | "Z" | "a" | "b" | "c" | "d"
           | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n"
           | "o" | "p" | "q" | "r" | "s" | "t" | "u" | "v" | "w" | "x"
           | "y" | "z"
```

## Dependency Management in SDMX 3.0.0:

1) MAJOR, MINOR or PATCH version parts in artefact references CAN be wildcarded using “+” as extension:  
   - X+.Y.Z means the currently latest available version >= X.Y.Z  
        *Example*: “2+.3.1” means the currently latest available version >= “2.3.1” (even if not backwards compatible)  
        *Typical use case*: references in SDMX Categorisations
   - X.Y+.Z means the currently latest available backwards compatible version >= X.Y.Z  
        *Example*: “2.3+.1” means the currently latest available version >= “2.3.1” and < "3.0.0" (all backwards compatible versions >= "2.3.1")  
        *Typical use case*: references in SDMX DSD  
   - X.Y.Z+ means the currently latest available forwards and backwards compatible version >= X.Y.Z  
        *Example*: “2.3.1+” means the currently latest available version >= “2.3.1” and < "2.4.0" (all forwards and backwards compatible versions >= "2.3.1")  
        *Typical use case*: tbd  

1) Publicly released artefacts MUST NOT reference pre-release artefacts, they MUST only reference other released artefacts. Wildcarded references in a release artefact thus implicitly target only future released versions of the referenced artefacts within the defined wildcard scope.  
        *Example*: The reference to "AGENCY_ID:CODELIST_ID(1.3+.2)" in an artefact "AGENCY_ID:DSD_ID(2.1.1)” resolves to artefact "AGENCY_ID:CODELIST_ID(1.4.1)" if that was currently the latest available released version.

1) Pre-release artefacts MAY reference other released or pre-release artefacts. Wildcarded references in a pre-release artefact thus implicitly target future released and pre-release versions of the referenced artefacts within the defined wildcard scope.  
        *Example*: The reference to "AGENCY_ID:CODELIST_ID(1.3+.2)" in an artefact "AGENCY_ID:DSD_ID(2.1.1-draft)” resolves to artefact "AGENCY_ID:CODELIST_ID(1.5.0-draft)" if that was currently the latest available version.

## SDMX 3.0 Rest API queries for wildcarded artefact versions

In order to resolve wildcarded dependencies, the SDMX 3.0 Rest API supports retrievals of wildcarded artefact versions.  

1) Artefact queries for a specific version X.Y.Z or X.Y.Z-EXT MUST return the exact specified version. This type of queries MUST be used for resolving fixed version references.  
        *Example*: Querying for 1.3.2 will return version 1.3.2. Querying for 1.3.2-draft will return version 1.3.2-draft.

1) Artefact queries where MAJOR, MINOR or PATCH version parts are extended with “+” (X+.Y.Z, X.Y+.Z or X.Y.Z+) MUST return the latest available released version within the wildcard scope. Such wildcarded queries MUST NOT specify a specific pre-release version extension. This type of queries MUST be used for resolving wildcarded version references in released artefacts.  
        *Example*: Querying for 1.3+.2 will return version 1.4.1 if that is the latest released version.

1) Artefact queries where the version is extended using “\*” (X.Y.Z\*, X+.Y.Z\*, X.Y+.Z\* or X.Y.Z+\*) MUST return the latest available pre-released or released version within the wildcard scope. Such queries MUST NOT specify a specific pre-release version extension. This type of queries MUST be used for resolving wildcarded version references in pre-released artefacts.  
        *Example*: Querying for 1.3.2\* will return version 1.3.2-draft.6 if that is the latest version of all pre-released or released versions within this wildcard scope. Querying for 1.3+.2\* will return version 1.5.0-draft if that is the latest version of all pre-released or released versions within this wildcard scope.

1) Artefact queries where the lastest (or all) version parts in X.Y.Z are replaced by the “all” keyword MUST return all available pre-released or released versions within the wildcard scope. Such queries MUST NOT specify a specific pre-release version extension:  
   - “all” means all versions  
   - “X.all” means all versions >= “X.0.0” and < “X+1.0.0" (all backwards compatible versions >= “X.0.0")  
   - “X.Y.all” means all versions >= “X.Y.0” and < “X.Y+1.0" (all forwards and backwards compatible versions >= “X.Y.0")  
   
[*Note*: “+” and "\*" are safe characters in HTTP queries.]

## Why Use SDMX 3.0 Semantic Versioning?

Without compliance to some sort of formal specification, version numbers are essentially useless for dependency management. By applying the ideas and rules of SemVer to SDMX 3.0 artefacts, it becomes easy to communicate your intentions to the users of your data models. Once these intentions are clear, flexible (but not too flexible) dependency specifications can finally be made.

A simple example will demonstrate how Semantic Versioning can make dependency hell a thing of the past. Consider a DSD called “MyDataStructure” It requires a Semantically Versioned Codelist named “Indicators” At the time that MyDataStructure is created, Indicators is at version 3.1.0. Since MyDataStructure uses some Codes that were first introduced in 3.1.0, you can safely specify the Indicators dependency as greater than or equal to 3.1.0 but less than 4.0.0 (using the wildcard syntax 3.1+.0). Now, when Indicators version 3.1.1 with some corrected names and 3.2.0 with some new Codes become available, you can release them to your SDMX artefact registry and know that they will be compatible with existing dependent data structures.

As a responsible data modeller you will, of course, want to verify that any artefact upgrades function as advertised. The real world is a messy place; there’s nothing we can do about that but be vigilant. What you can do is let SDMX 3.0 Semantic Versioning provide you with a sane way to release and upgrade artefacts without having to roll new versions of dependent artefacts, saving you time and hassle.

## Upgrade and conversions of artefacts defined with previous SDMX standard versions

To convert SDMX artefacts created previously to SDMX 3.0.0:

1) Incomplete artefact version numbers MUST be complemented with 0s for the missing parts to build valid semantic version numbers.  
        *Example*: Version 2 becomes version 2.0.0 and version 1.0 becomes version 1.0.0.

1) The "isFinal=false" property is replaced by the pre-release version extensions "-draft" (or alternatively "-unstable" depending on the use case).  
        *Example*: Version 1.3 isFinal=true becomes version 1.3.0 and version 1.3 isFinal=false becomes version 1.3.0-draft.

## FAQ

**How should I deal with revisions in the 0.y.z initial modelling phase?**  
The simplest thing to do is start your initial modelling release at 0.1.0 and then increment the minor version for each subsequent release.

**How do I know when to release 1.0.0?**  
If your data model is being used in production, it should probably already be 1.0.0. If you have a stable artefact on which users have come to depend, you should be 1.0.0. If you’re worrying a lot about backwards compatibility, you should probably already be 1.0.0.

**Doesn’t this discourage rapid modelling and fast iteration?**  
Major version zero is all about rapid modelling. If you’re changing the artefact every day you should either still be in version 0.y.z or on the next (minor or) major version for a separate modelling.

**If even the tiniest backwards incompatible changes to the public artefact require a major version bump, won’t I end up at version 42.0.0 very rapidly?**  
This is a question of responsible modelling and foresight. Incompatible changes should not be introduced lightly to a data model that has a lot of dependencies. The cost that must be incurred to upgrade can be significant. Having to bump major versions to release incompatible changes means you’ll think through the impact of your changes, and evaluate the cost/benefit ratio involved.

**Documenting the version changes in an artefact's annotation of type "CHANGELOG" is too much work!**  
It is your responsibility as a professional modeller to properly document the artefacts that are intended for use by others. Managing data model complexity is a hugely important part of keeping a project efficient, and that’s hard to do if nobody knows how to use your data model, or what artefacts are safe to reuse. In the long run, SDMX 3.0 Semantic Versioning can keep everyone and everything running smoothly.

**What do I do if I accidentally release a backwards incompatible change as a minor version?**  
As soon as you realise that you’ve broken the SDMX 3.0 Semantic Versioning specification, fix the problem and release a new minor version that corrects the problem and restores backwards compatibility. Even under this circumstance, it is unacceptable to modify versioned releases. If it’s appropriate, document the offending version and inform your users of the problem so that they are aware of the offending version.

**What should I do if I update my own dependencies without changing the public artefact?**  
That would be considered compatible since it does not affect the public artefact. Artefacts that explicitly depend on the same dependencies as your artefact should have their own dependency specifications and the author will notice any conflicts. Determining whether the change is a patch level or minor level modification depends on whether you updated your dependencies in order to change a property or introduce new backwards compatible items. For the latter instance, one would obviously expect a minor level increment.

**What if I inadvertently alter the public artefact in a way that is not compliant with the version number change (i.e. the modification incorrectly introduces a major breaking change in a patch release)?**  
Use your best judgement. If you have a huge audience that will be drastically impacted by changing the behaviour back to what the public artefact intended, then it may be best to perform a major version release, even though the property change could strictly be considered a patch release. Remember, SDMX 3.0.0 Semantic Versioning is all about conveying meaning by how the version number changes. If these changes are important to your users, use the version number to inform them.

**How should I handle deprecating elements?**  
Deprecating existing elements is a normal part of data modelling and is often required to make forward progress or follow history (changing classifications, evolving reference areas). When you deprecate part of your public artefact, you should do two things: (1) update your documentation ("CHANGELOG" annotation) to let users know about the change, (2) issue a new minor release with the deprecation in place. Before you completely remove the functionality in a new major release there should be at least one minor release that contains the deprecation so that users can smoothly transition to the new artefact.

**Does SDMX 3.0.0 Semantic Versioning have a size limit on the version string?**  
No, but use good judgement. A 255 character version string is probably overkill, for example. Also, specific SDMX implementations may impose their own limits on the size of the string. Remember, it is generally recommended to use the standard extension "-draft".  

**Is “v1.2.3” a semantic version?**  
No, “v1.2.3” is not a semantic version. The semantic version is “1.2.3”.

**Is there a suggested regular expression (RegEx) to check an SDMX 3.0.0 Semantic Versioning string?**  
There are two. One with named groups for those systems that support them (PCRE [Perl Compatible Regular Expressions, i.e. Perl, PHP and R], Python and Go).  

Reduced version (without SemVer "build metadata") from: https://regex101.com/r/Ly7O1x/3/  

`^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?$`  

And one with numbered capture groups instead (so cg1 = major, cg2 = minor, cg3 = patch, cg4 = prerelease and cg5 = buildmetadata) that is compatible with ECMA Script (JavaScript), PCRE (Perl Compatible Regular Expressions, i.e. Perl, PHP and R), Python and Go.  

Reduced version (without SemVer "build metadata") from: https://regex101.com/r/vkijKf/1/  

`^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?$`
