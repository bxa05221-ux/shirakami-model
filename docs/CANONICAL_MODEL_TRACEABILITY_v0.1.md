# Shirakami Canonical Model Traceability v0.1

Status: draft / audit baseline  
Date: 2026-10-05  
Parent: `docs/CANONICAL_MODEL_MAP_v0.1.md`

## Purpose

This document turns the Canonical Model Map into a file-level traceability baseline. It records what can currently be traced in the repositories and explicitly marks unresolved links instead of inferring them.

## Traceability matrix

| Concept | Model / Architecture | Specification | Runtime | Verification / Evidence | Assessment |
|---|---|---|---|---|---|
| Human Authority | `architecture/shirakami-architecture.yaml` | R0100 Human Review / invariants | Reviewer / Human Gate boundary in `shirakami-OS` | `CROSS_LAYER_AUDIT_2026-09-25.md` | 🟢 strong |
| Landscape | `architecture/` + v3.2 Matome YAML | R0100 observation context | `runtime/observation_candidate.py` | observation traces / audit | 🟢 strong |
| Observation | Architecture + v3.2 | R0100 Observation | `runtime/observation_candidate.py` | observation trace documents | 🟢 strong |
| Context | v3.2 Human Context First | R0100 Context Snapshot | `runtime/evolution_bridge.py` → `ContextSnapshot` | snapshot/lineage path | 🟢 strong |
| Evidence | Model Evidence concept | R0100 Evidence contract | `runtime/evolution_bridge.py` → `EvidenceRecord` | immutable Evidence / promotion audit | 🟢 strong |
| Protocol Candidate | Language Protocol / v3.2 | R0100 candidate state | `runtime/evolution_bridge.py` → `ProtocolCandidate`; `candidate_generation.py` | candidate tests / traces | 🟢 strong |
| Human Gate | Human Judgment / Human Authority | R0100 Human Review | reviewer / approval boundary | authority state remains ungranted until approval | 🟢 strong |
| Runtime | Runtime replaceable | R0100 Runtime/Execution boundary | `shirakami-OS` runtime and adapters | execution / observation | 🟢 strong |
| Verification | Revisit / observation loop | R0100 Verification | `runtime/evolution_pipeline.py` → `VerificationResult` | mismatch and verification evidence | 🟢 strong |
| Mismatch | Preserve uncertainty / Revisit | R0100 mismatch evidence | `runtime/evolution_bridge.py` → `MismatchEvidence` | converted to immutable EvidenceRecord | 🟢 strong |
| Provenance | Context / handoff continuity | R0100 lineage/provenance | Evidence and context structures | evidence IDs / transition records | 🟡 needs one canonical cross-repo reference |
| Uncertainty | Dark Layer / preserve uncertainty | R0100 inconclusive/uncertainty states | `VerificationResult.uncertainty` | mismatch/inconclusive evidence | 🟢 strong |
| Thread | v3.2 | not yet a core R0100 primitive | application/collaboration layer | ThreadRPG / related artifacts | 🟡 collaboration layer |
| 的目YAML | `matome_yaml/` v3.2 | Semantic Handoff / related contracts | OS handoff mechanisms | handoff artifacts | 🟡 needs canonical schema pointer |
| Semantic Handoff | v3.2 / OS architecture | related specification | OS handoff/runtime paths | audit/trace artifacts | 🟡 needs canonical source decision |
| Presenter / Conference | v3.2 | not core R0100 | collaboration/application layer | experimental/application evidence | 🟡 application/collaboration |
| Re-observation | Architecture / v3.2 | R0100 loop return | evolution pipeline | verification → evidence loop | 🟢 strong |
| Catch | Architecture | not a normative runtime primitive | human cognition/application layer | human judgment residue | 🟡 conceptual |
| Evolution Loop | v3.2 / Architecture | R0100 | `runtime/evolution_bridge.py`, `evolution_pipeline.py` | transition/evidence records + tests | 🟢 strong |

## Direct runtime evidence currently verified

### `runtime/evolution_bridge.py`

The Runtime explicitly defines:

- immutable `ContextSnapshot`;
- `ProtocolCandidate` awaiting Human Review;
- `VerificationResult` with explicit uncertainty;
- immutable `MismatchEvidence`;
- conversion of mismatch/transition/candidate objects into canonical `EvidenceRecord` objects;
- deterministic queries over Evidence records.

This is a direct Model → Runtime correspondence rather than a conceptual inference.

## Boundary evidence currently verified

The OS cross-layer audit records the review-path state as:

- `decision = null`
- `authority_granted = false`
- `decision_authorized = false`
- `human_gate_required = true`

It also states that Evidence promotion requires explicit Human Gate approval and resolves supplied Evidence IDs against already-recorded immutable EvidenceRecords.

## Observation → Candidate boundary

The OS contains a dedicated `runtime/observation_candidate.py` boundary described as `Landscape Observation -> Protocol Candidate`. A separate eligibility module explicitly limits itself to sufficiency checks and does not rank, select, approve, promote, activate, or interpret domain semantics.

This is an important canonical boundary:

```text
Landscape
  ↓
Observation
  ↓
Protocol Candidate
  ↓
Human Gate
```

Candidate generation must not silently become authorization.

## Remaining traceability gaps

1. Add exact canonical file paths for R0100 and its Human Review invariants.
2. Add an explicit canonical schema pointer for 的目YAML / Semantic Handoff.
3. Identify the exact test names proving each Human Gate invariant.
4. Link `shirakami-model-v3.2.yaml` concepts to their R0100 counterparts without collapsing collaboration concepts into normative Runtime primitives.
5. Decide the canonical terminology for `Context`, `ContextSnapshot`, `Matome YAML`, and `Semantic Handoff`.
6. Mark which concepts are stable Core versus research/application artifacts.

## Current conclusion

The traceability baseline demonstrates that the central Shirakami execution chain is already represented across Model, Specification, Runtime, and Evidence layers. The main remaining work is canonical source selection, terminology reconciliation, and test-level traceability—not invention of the basic control architecture.

## Human Gate

Required: true  
Decision: pending  
Status: draft / review required
