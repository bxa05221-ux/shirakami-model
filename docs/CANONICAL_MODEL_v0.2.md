# Shirakami Canonical Model v0.2

Status: draft / review required  
Date: 2026-10-05

## 1. Purpose

This document integrates the current Canonical Model Map, Evidence Contract, Protocol Contract, Context/Handoff Contract, and Matome YAML traceability work into one model-level reference.

It is intentionally a **reference model**, not a single implementation schema. Runtime, representation, and provider-specific details remain replaceable.

## 2. Core proposition

Shirakami is a human-authoritative AI architecture in which AI and Runtime components may observe, analyze, propose, execute authorized protocols, and verify results, while final authority remains outside those components at the Human Gate.

> AI may increase the quality of reasoning without acquiring the right to decide.

## 3. Canonical layers

### L0 — Human Authority

Final authority, approval, rejection, revision, and authorization.

### L1 — Landscape

The relevant external/internal situation from which observations are made. Landscape is not synonymous with model state.

### L2 — Observation

A bounded representation of what has been observed. Observation must remain distinguishable from interpretation and authority.

### L3 — Evidence

Immutable, non-authoritative records retained for verification, replay, audit, and reconstruction. Evidence can inform authority but cannot become authority.

### L4 — Context / Handoff

State required to interpret and continue work across loop boundaries. `ContextSnapshot` is an immutable runtime representation. Semantic Handoff transfers context while preserving provenance, uncertainty, assumptions, and unresolved meaning.

### L5 — Protocol Candidate

A structured proposal derived from observations/context. Candidate status is explicitly non-authoritative and non-executable until Human Gate authorization.

### L6 — Human Gate

The authority boundary. Candidate/Protocol information may be reviewed, rejected, revised, or approved. No lower layer may silently create authority.

### L7 — Authorized Protocol

A protocol explicitly authorized through the Human Gate. Authorization is distinct from structural validity and from eventual execution correctness.

### L8 — Runtime / Adapter

Executes authorized Protocols using replaceable runtime/provider components. Runtime must not manufacture Human authority.

### L9 — Verification

Checks observed execution/results against the relevant Protocol, Evidence, and Context. Verification may produce mismatch/uncertainty Evidence but does not itself authorize the next action.

## 4. Canonical loop

```text
Landscape
   ↓
Observation
   ↓
Evidence / Context
   ↓
Protocol Candidate
   ↓
Human Gate
   ├── reject / revise ──→ Observation / Context
   └── approve
          ↓
   Authorized Protocol
          ↓
       Runtime
          ↓
       Result
          ↓
     Verification
          ↓
       Evidence
          ↺
```

## 5. Authority invariant

The following components are non-authoritative by default:

- AI Runtime;
- Evidence;
- ContextSnapshot;
- Semantic Handoff;
- Protocol Candidate;
- structural validation;
- Replay;
- Verification;
- API success/failure state.

Only the defined Human Gate path may grant decision/execution authority.

## 6. Four-way separation

Shirakami explicitly separates:

```text
Structural validity
        ≠
Semantic truth
        ≠
Human authorization
        ≠
Verified outcome
```

A valid representation is not necessarily true. A plausible interpretation is not approval. An approved protocol is not a verified outcome.

## 7. Evidence contract

Currently modeled guarantees:

- immutability;
- non-authority;
- Human-gated promotion;
- replayability;
- deterministic replay for the same ordered sequence and rules;
- fingerprintability;
- mismatch externalization.

Not currently canonical guarantees:

- universal event identity;
- complete causal lineage;
- universal timestamp ordering;
- order independence of conflicting Evidence;
- automatic conflict resolution;
- concurrent merge semantics.

Those properties require concrete requirements, implementation, deterministic tests, and Human Gate review before promotion into the Core model.

## 8. Protocol contract

A Protocol Candidate must remain:

```text
status = CANDIDATE
authority = false
executable = false
```

Candidate generation must not silently:

- rank;
- select;
- prioritize;
- approve;
- promote;
- activate;
- mutate Landscape;
- invent domain facts;
- convert uncertainty into certainty.

## 9. Context and Handoff contract

Context carries the state required to interpret or continue work. A Semantic Handoff must preserve, where available:

- source identity;
- Observation/Evidence references;
- relevant Landscape context;
- Protocol/Candidate identity;
- execution state;
- uncertainty;
- provenance;
- labeled assumptions;
- unresolved questions.

Context does not grant authority.

## 10. Representation boundary

The semantic contract is authoritative over any particular serialization format.

```text
Canonical semantics
       ↓
representation contract
       ↓
的目YAML / Protocol IR / other representation
       ↓
Runtime implementation
```

The current Matome YAML implementation is a compact Protocol IR and must not be mistaken for the complete v3.2 conceptual model.

## 11. Model v3.2 relationship

`shirakami-model-v3.2.yaml` remains valuable as the broader conceptual/collaboration architecture. Its Thread, Presenter, Conference, Optimization, RPG, education, organizational, and rendering concepts should not automatically become Core Runtime primitives.

The v0.2 Canonical Model therefore distinguishes:

- **Core:** authority, Landscape, Observation, Evidence, Context, Protocol Candidate, Human Gate, Authorized Protocol, Runtime, Verification;
- **Collaboration:** Thread, Presenter, Conference, optimization and related coordination constructs;
- **Application:** education, organization, RPG and domain profiles;
- **Representation:** 的目YAML and other serializations;
- **Research:** unresolved temporal, causal, conflict, concurrency, and provider-specific questions.

## 12. Traceability requirement

Every Core concept should eventually map to:

```text
Model definition
   ↓
Normative specification
   ↓
Runtime implementation
   ↓
Deterministic test
   ↓
Evidence / audit artifact
```

Missing links are reported as gaps rather than inferred.

## 13. Core invariants proposed for review

### C-01 — Human Authority

AI/Runtime components cannot independently acquire final decision authority.

### C-02 — Evidence Non-Authority

Evidence may inform authority but cannot become authority.

### C-03 — Candidate Non-Authority

A Protocol Candidate is a proposal, not approval or execution authority.

### C-04 — Context Non-Authority

Context and Semantic Handoff carry state but do not grant authority.

### C-04 — Context Non-Authority

Context and Semantic Handoff carry state but do not grant decision power.

**Verification status: PASS (implementation evidence).**

- OS test: runtime/test_core_invariants.py
- CI workflow: .github/workflows/core-invariants.yml
- CI run: 37231397388
- CI result: 12 passed in 0.17s
- Verified PR: #566
- Verified head: 01974bfaf75bdd23e7d15e2b8446d6ec5a28117a
- Tests cover non-promotion of authority-like metadata, absence of decision attributes, and ContextSnapshot immutability.

This is implementation/test evidence, not model approval.

### C-05 — Uncertainty Preservation

Missing or unresolved semantics must remain explicit rather than silently becoming certainty.

**Verification status: PASS (implementation evidence).**

- OS test: `runtime/test_evolution_bridge.py`
- CI workflow: `.github/workflows/core-invariants.yml`
- CI result: **9 passed**
- Verified commit: `2540777a332792a1f1eccbfe9cad86d9fd5e321f`
- `VerificationResult.as_mapping()` preserves the explicit uncertainty field.
- Deterministic tests verify that uncertainty values such as `high` and `unresolved` are not dropped or converted into authority/decision fields.

This is implementation/test evidence, not Human Gate approval of the Core model.

### C-06 — Structural/semantic separation

Structural validation cannot establish domain truth.

### C-07 — Verification Non-Authority

Verification may establish evidence about results but does not itself authorize subsequent action.

### C-08 — Runtime Replaceability

Runtime/provider implementation is replaceable and must not redefine Core authority semantics.

**Verification status: PASS (implementation evidence).**

- OS test: `runtime/test_runtime_replaceability.py`
- CI workflow: `.github/workflows/core-invariants.yml`
- CI result: **3 passed**
- Verified commit: `80a9ca239130965f1cd8feb117872910df357be2`
- The test exercises both direct Runtime replacement and an `EvidenceDrivenRuntime(runtime=...)` composition boundary.
- The test also executes the full EvidenceDrivenRuntime path through the alternate Runtime and verifies successful verification without `authority_granted` or `decision_authorized`.

This is implementation/test evidence, not Human Gate approval of the Core model.

### C-09 — Evidence Replayability

Recorded Evidence must remain usable for the defined replay/reconstruction path.

### C-10 — Human Gate for Promotion

Promotion from candidate/review state to authorized state requires the defined Human Gate path.

## 14. Open model questions

1. Canonical provenance fields across Evidence, ContextSnapshot, and Semantic Handoff.
2. Canonical 的目YAML schema, if one is ultimately required.
3. Temporal ordering and causal lineage semantics.
4. Conflict and concurrent merge semantics.
5. Exact normative mapping of all Core invariants to R0100/tests.
6. Criteria for moving a collaboration/application concept into Core.

## 15. Promotion rule

No unresolved research question becomes a Core invariant merely because it appears useful. Promotion requires:

1. observed requirement;
2. explicit normative statement;
3. minimal implementation;
4. deterministic test;
5. Evidence/audit artifact;
6. Human Gate review.

## 16. Human Gate

Required: true  
Decision: pending  
Status: draft / review required
