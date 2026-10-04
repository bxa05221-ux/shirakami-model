# Shirakami Matome YAML Traceability v0.1

Status: draft / review required  
Date: 2026-10-05  
Source artifact: `matome_yaml/shirakami-model-v3.2.yaml`

## Purpose

This document separates the existing Shirakami Model v3.2 Matome YAML into semantic classes so that the historical/collaboration model is not accidentally promoted into the normative Runtime Core.

The v3.2 artifact describes Landscape First, Protocol First, Human Context First, threads, Matome YAML, Presenter, asynchronous conference, optimization, rendering, education, organizational use, and the Observe → Compress → Conference → Optimize → Return cycle. fileciteturn89file0L2-L2

## 1. Classification

| v3.2 area | Classification | Canonical treatment |
|---|---|---|
| `metadata.title/type/purpose/status` | Descriptive | Keep as artifact metadata; not Core invariant |
| `subject.central_concept` | Core concept labels | Map to Canonical Model terminology |
| `core_question` | Philosophy / research question | Preserve; not normative execution rule |
| `architecture.landscape` | Core | Map to Landscape Contract |
| `architecture.thread` | Collaboration | Not a mandatory R0100 Runtime primitive |
| `architecture.matome_yaml` | Collaboration + representation | Map to Context/Handoff and Protocol representation contracts |
| `architecture.presenter` | Collaboration | Keep outside authority boundary |
| `asynchronous_conference` | Collaboration | Map to observation/comparison/re-observation loop |
| `resource_distribution` | Application / research | Not Core until a concrete normative requirement exists |
| `rpg` | Rendering / application | Not Core |
| `knowledge_rendering` | Rendering | Adapter/application layer |
| `protocol_chain.historical_flow` | Historical research record | Preserve as history; do not treat names as normative primitives |
| `education` | Application profile | Example deployment pattern |
| `organizational_application` | Application profile | Example deployment pattern |
| `external_rendering` | Adapter/rendering layer | Preserve model-independent rendering principle |
| `philosophy.not/is` | Philosophy | Explanatory layer, not Runtime contract |
| `final_state` | Conceptual mapping | Map selected entries to Core; keep roles descriptive |
| `core_loop` | Collaboration/Cognitive loop | Complementary to normative execution loop |
| `final_statement` | Philosophy | Explanatory statement |

## 2. Field-level semantic mapping

### `landscape`

**Class:** Core.

Existing v3.2 principles include preserving current state, not modifying reality through observation, and retaining unresolved state. fileciteturn89file0L2-L2

Map to:

```text
Landscape → Observation → Evidence / Candidate
```

### `thread`

**Class:** Collaboration.

A Thread is an independent observation/context stream. It is useful for multi-perspective work but should not be required by every Runtime execution.

### `matome_yaml`

**Class:** Representation mechanism with collaboration roots.

Its stated roles are state compression, result handoff, thread communication, and an intermediate representation between humans and AI. fileciteturn89file0L2-L2

Canonical semantic target:

```text
Context/Handoff Contract
        ↓
Matome YAML representation
        ↓
Protocol / Handoff / review artifact
```

The representation is not itself the authority boundary.

### `presenter`

**Class:** Collaboration mechanism.

The Presenter compares thread outputs and returns individualized Matome YAML. It must remain a coordinator/presenter, not a decision authority. This is consistent with the OS reviewer boundary, where multiple perspectives remain comparable and `decision` stays null. fileciteturn50file0L2-L2

### `asynchronous_conference`

**Class:** Collaboration loop.

The API draft explicitly models independent observation, preservation of uncertainty/unresolved items, conference, differences, contradictions, and individualized returns. fileciteturn95file0L2-L2

Important invariant:

```text
Comparison
  ≠
Consensus
  ≠
Authorization
```

### `core_loop`

The v3.2 loop is:

```text
Human Landscape
 → AI Observation
 → Thread divergence
 → Matome compression
 → Conference
 → Individualized return
 → Re-observation
 → Landscape change
 → Observe again
```

This should coexist with, rather than replace, the normative execution loop in the Canonical Model Map. fileciteturn60file0L2-L2

## 3. Critical distinction discovered in Runtime

The current OS Runtime does **not** treat every Matome YAML as a full Core Model object.

The Quickstart loader parses a deliberately small Protocol subset with:

- `matome` root;
- `title`;
- `version`;
- `statement`;
- `pipeline` containing `phase` and `action`.

It explicitly says it does not implement the full YAML specification. fileciteturn85file0L2-L2

The resulting `ProtocolIR` is a separate Runtime representation. This is strong evidence that the large v3.2 conceptual YAML and the executable Protocol representation should not be conflated.

## 4. Crystallization boundary

The OS can derive a deterministic temporary Protocol identifier from the exact Matome YAML bytes using a SHA-256-derived identifier and register it as a temporary Protocol. fileciteturn73file0L2-L2

Therefore:

```text
Matome YAML
   ↓ parse / validate
ProtocolIR
   ↓ crystallize
Temporary Protocol
   ↓ registry
Runtime selection / invocation
```

This is an implementation boundary, not an assertion that every conceptual v3.2 field is executable.

## 5. Lifecycle separation

The Protocol registry distinguishes `active`, `experimental`, and `archived` states and `default` versus `temporary` lifecycles. A default Protocol must remain active; archived Protocols cannot be selected as current. fileciteturn74file0L2-L2

This supports the broader Shirakami rule:

```text
Conceptual artifact
      ≠
Candidate
      ≠
Temporary Protocol
      ≠
Active Protocol
      ≠
Human authorization
```

## 6. Reviewer Matome YAML is another distinct role

The external-review schema requires `matome_yaml` as reviewer context and separately carries observations, evidence references, unresolved questions, falsifiable points, proposals, interpretation, and Human Gate state. It explicitly says review output is not accepted Evidence and does not grant authority. fileciteturn81file0L2-L2

Therefore `matome_yaml` is best understood as a **role-dependent semantic container**, not one universal authority-bearing object.

## 7. Canonical classification of v3.2

The current v3.2 artifact should be classified as:

**`conceptual-collaboration-architecture`**

not:

**`normative-runtime-schema`**.

That distinction removes a major source of model confusion.

## 8. What should become Core

Promote only these semantic properties from v3.2 into Core contracts:

1. Landscape is the field of observation.
2. Observation does not itself grant authority.
3. Context can be externalized and handed off.
4. Uncertainty and unresolved state should remain explicit.
5. Multiple observations can remain distinct.
6. Differences and contradictions must not be silently erased.
7. Re-observation can return to the changed Landscape.
8. Matome YAML can be a representation of handoff/context/protocol state.
9. Human Gate remains outside and above these representations.

## 9. What should remain outside Core

Keep these as collaboration/application/research material unless separately promoted:

- RPG mechanics;
- education-specific roles;
- organizational resource allocation;
- rendering formats;
- historical protocol names;
- Presenter implementation details;
- specific thread hierarchy metaphors;
- domain-specific resource distribution rules.

## 10. Current assessment

The v3.2 Matome YAML is valuable and should not be discarded. It is better understood as the **collaboration/cognitive architecture layer** that surrounds the smaller normative Core.

The Runtime evidence strengthens this interpretation: the executable Protocol loader intentionally consumes a much smaller subset, while reviewer and conference boundaries use Matome YAML as context/perspective rather than authority. fileciteturn85file0L2-L2 fileciteturn76file0L2-L2

## 11. Human Gate

Required: true  
Decision: pending  
Status: draft / review required
