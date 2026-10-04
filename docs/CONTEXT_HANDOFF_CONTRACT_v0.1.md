# Shirakami Context & Handoff Contract v0.1

Status: draft / review required  
Date: 2026-10-05  
Parent: `docs/CANONICAL_MODEL_MAP_v0.1.md`

## Purpose

Define how Shirakami carries execution context across loop boundaries without silently converting context into authority or losing the provenance of the state being handed off.

## 1. Core definition

**Context** is the state needed to interpret an Observation, Candidate, Protocol, Runtime result, or Verification within its relevant Landscape and execution history.

**ContextSnapshot** is an immutable capture of execution context at a loop boundary.

The current Runtime implements `ContextSnapshot` as an immutable structure containing `landscape`, `protocol_id`, `runtime_state`, and `metadata`. fileciteturn47file0L2-L2

## 2. Context is not authority

Context may inform interpretation and execution, but it does not itself grant:

- Human authority;
- Protocol approval;
- execution authorization;
- semantic truth;
- promotion of Evidence.

A context snapshot records state; it does not decide what should happen next.

## 3. Handoff principle

A Semantic Handoff transfers enough structured context for the receiving participant or Runtime to continue work without silently inventing missing meaning.

A valid handoff should preserve, where available:

- source identity;
- source Observation or Evidence references;
- relevant Landscape context;
- current Protocol/Candidate identity;
- execution state;
- explicit uncertainty;
- provenance;
- assumptions, clearly labeled;
- unresolved questions or missing semantics.

## 4. Handoff boundary

```text
Source Context
    │
    ▼
Semantic Handoff
    │
    ├── provenance preserved
    ├── uncertainty preserved
    ├── assumptions labeled
    ├── missing semantics remain explicit
    │
    ▼
Receiving Context
    │
    ▼
Observation / Analysis / Candidate
```

The receiving side must not interpret successful receipt of a Handoff as Human approval or as proof of domain truth.

## 5. ContextSnapshot requirements

A ContextSnapshot should be:

- immutable after capture;
- attributable to a loop boundary;
- distinguishable from live mutable Runtime state;
- sufficient to explain the relevant Protocol/Runtime state;
- serializable without silently dropping uncertainty or provenance.

The current Runtime structure satisfies the first property directly through `frozen=True`. fileciteturn47file0L2-L2

## 6. What a Handoff must not do

A Handoff must not:

- create approval;
- create activation authority;
- promote Evidence;
- invent missing domain facts;
- turn assumptions into observations;
- turn uncertainty into certainty;
- silently overwrite the receiving Landscape;
- erase provenance to simplify presentation.

## 7. Relationship to 的目YAML

的目YAML may serve as a semantic handoff artifact, but this Contract does not yet freeze one universal YAML schema.

The distinction is intentional:

```text
Context Contract
      ↓
defines required semantic properties
      ↓
的目YAML / other representation
      ↓
implements the handoff representation
```

The representation may evolve while the semantic contract remains stable.

## 8. Relationship to Evidence

Context and Evidence are related but not identical.

```text
ContextSnapshot
  = state needed to interpret/continue work

EvidenceRecord
  = immutable record retained for verification/replay/audit
```

A ContextSnapshot may reference Evidence. Evidence may contain contextual information. Neither relationship grants authority.

## 9. Relationship to Protocol Candidate

A Protocol Candidate may carry ContextSnapshot-derived information, but Candidate status remains:

```text
authority = false
executable = false
```

Context cannot bypass the Human Gate.

## 10. Open questions

1. Freeze canonical provenance fields across ContextSnapshot, EvidenceRecord, and 的目YAML.
2. Define the minimum context required for cross-runtime/provider handoff.
3. Define merge/conflict semantics when two ContextSnapshots describe overlapping state.
4. Decide whether Landscape versioning is required for causal reconstruction.
5. Map every existing 的目YAML field to this semantic contract before declaring a canonical schema.

## 11. Verification matrix

| Property | Current status |
|---|---|
| Immutable ContextSnapshot | 🟢 implemented |
| Landscape carried | 🟢 implemented |
| Protocol identity carried | 🟢 implemented |
| Runtime state carried | 🟢 implemented |
| Metadata carried | 🟢 implemented |
| Authority separation | 🟢 model invariant |
| Provenance preservation | 🟡 contract / schema reconciliation needed |
| Uncertainty preservation | 🟡 contract / schema reconciliation needed |
| Cross-runtime handoff | 🟡 requires explicit tests |
| Merge/conflict semantics | 🟡 open |
| Canonical 的目YAML schema | 🟡 open |

## 12. Promotion criteria

A future Context/Handoff revision should require:

1. an observed handoff requirement;
2. explicit semantic fields;
3. representation mapping;
4. runtime implementation;
5. round-trip / losslessness tests where applicable;
6. Human Gate review.

## 13. Human Gate

Required: true  
Decision: pending  
Status: draft / review required
