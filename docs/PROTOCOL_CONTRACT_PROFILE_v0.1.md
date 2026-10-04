# Shirakami Protocol Contract Profile v0.1

Status: draft / review required  
Date: 2026-10-05  
Parent: `docs/CANONICAL_MODEL_MAP_v0.1.md`  
Related: `docs/EVIDENCE_CONTRACT_PROFILE_v0.1.md`

## Purpose

Define the boundary between Evidence/Observation, Protocol Candidate, Human authorization, and Runtime execution.

The central rule is simple:

> A Protocol Candidate is a structured proposal, not a decision, approval, or executable authority.

## 1. Core definition

A **Protocol** is a structured expression of intended action, constraints, verification, and related execution semantics.

A **Protocol Candidate** is a proposed Protocol representation derived from observed material and awaiting Human Review. It is non-authoritative and non-executable until the defined Human Gate path authorizes it.

## 2. Protocol Candidate guarantees

A Candidate must preserve, where available:

- candidate identity;
- originating Observation identity;
- source/provenance;
- observed context and state;
- uncertainty;
- explicit assumptions, clearly labeled;
- explicit inputs, steps, outputs, constraints, stop conditions, and evidence plans only when supported by the source Observation.

The current OS boundary explicitly defines Candidate output as `status=CANDIDATE`, `authority=false`, and `executable=false`. fileciteturn43file0L2-L2

## 3. Boundary rules

### P-01 — Eligibility is not generation

Passing Candidate Eligibility permits an Observation to cross into candidate generation. It does not select or authorize a Protocol.

### P-02 — Generation is not selection

Candidate generation must not rank, prioritize, or select among alternatives.

### P-03 — Generation is not authorization

Candidate generation must never create or imply Human approval.

### P-04 — Candidate is non-executable

A Candidate is not an executable Runtime instruction until the Human Gate path authorizes the corresponding Protocol.

### P-05 — Observation remains distinguishable from interpretation

The generator may structure observed material but may not silently create domain facts, priorities, rankings, or semantic conclusions absent from the originating Observation.

### P-06 — Uncertainty is preserved

Missing semantics remain missing. Uncertainty must not be silently converted into certainty.

### P-07 — Provenance follows the Candidate

The Candidate must remain traceable to its originating Observation and source context.

## 4. Canonical flow

```text
Landscape
  ↓
Observation
  ↓
Candidate Eligibility
  ↓
Protocol Candidate
  │
  │ authority=false
  │ executable=false
  ↓
Human Gate
  │
  ├── reject / revise
  │
  └── approve
        ↓
Authorized Protocol
        ↓
Runtime / Adapter
        ↓
Observation / Result
        ↓
Verification
        ↓
Evidence
```

## 5. Forbidden transitions

The following are not valid Protocol Candidate transitions:

```text
Candidate → automatic selection
Candidate → automatic approval
Candidate → automatic promotion
Candidate → automatic activation
Candidate → Landscape mutation
Candidate → domain-truth conclusion
Candidate → certainty by omission
```

The current candidate-generation boundary explicitly forbids ranking, selection, priority assignment, approval creation, promotion, activation, Landscape mutation, domain-truth inference, and silent completion of missing semantics. fileciteturn43file0L2-L2

## 6. Runtime correspondence

The OS currently contains:

- immutable `ProtocolCandidate` awaiting Human Review;
- `ProtocolCandidateArtifact` derived from Observation;
- Candidate eligibility boundary;
- Candidate generation boundary;
- structural validation boundary;
- tests for Observation/Candidate and Candidate validation.

The runtime bridge also converts Candidate-related state into the canonical immutable Evidence shape rather than granting execution authority. fileciteturn42file0L2-L2

## 7. Validation versus truth

Structural validation may establish properties about representation, such as required fields and explicit status. It must not establish:

- domain truth;
- Human approval;
- execution authority;
- semantic correctness merely from structural conformity.

This separation is a Core boundary:

```text
Structural validity
        ≠
Semantic truth
        ≠
Human authorization
        ≠
Verified outcome
```

## 8. Verification matrix

| Property | Current assessment |
|---|---|
| Candidate is explicit | Guaranteed by runtime artifact |
| Candidate is non-authoritative | Guaranteed by boundary definition |
| Candidate is non-executable | Guaranteed by boundary definition |
| Origin Observation preserved | Required by boundary |
| Provenance preserved | Required by boundary |
| Uncertainty preserved | Required by boundary |
| No automatic ranking | Forbidden |
| No automatic selection | Forbidden |
| No automatic approval | Forbidden |
| No automatic promotion | Forbidden |
| No automatic activation | Forbidden |
| No invented domain semantics | Forbidden |
| Human Gate before authorization | Core invariant |
| Structural validation separate from truth | Core invariant |

## 9. Open questions

1. Canonical schema for the full Protocol object remains to be frozen across model/specification/runtime repositories.
2. The exact approval envelope and authorized Protocol representation should be traced to the normative specification.
3. Candidate revision/rejection semantics should be mapped explicitly to Evidence and provenance.
4. Provider-specific execution details remain Runtime/Adapter concerns and should not leak into the Core Protocol definition.

## 10. Promotion criteria

A future Protocol Contract revision should require:

1. a concrete observed requirement;
2. an explicit normative rule;
3. implementation correspondence;
4. deterministic tests;
5. Evidence of the boundary in operation;
6. Human Gate review.

## 11. Human Gate

Required: true  
Decision: pending  
Status: draft / review required
