# Shirakami Core Invariant Coverage Matrix v0.1

Status: reviewed Core scope approved / supporting principles retained  
Date: 2026-10-05

This matrix separates model claims from implementation evidence. A PASS means deterministic implementation/test evidence exists. Human Gate status is tracked separately from technical PASS.

| ID | Invariant | Normative statement | Implementation/test evidence | CI evidence | Technical status | Human Gate classification |
|---|---|---|---|---|---|---|
| C-01 | Human Authority | AI/Runtime cannot independently acquire final authority. | `api/test_boundary.py::test_human_gate_cannot_be_disabled`; `runtime/test_evolution_loop.py::test_human_gate_blocks_without_approval`; `runtime/test_api.py::test_human_gate_requires_explicit_authorization` | Unified CI Run 37232354912: **48 passed** | PASS | **Reviewed Core** |
| C-02 | Evidence Non-Authority | Evidence informs authority but cannot become authority. | `runtime/test_evidence.py`; `runtime/test_execution_evidence_projection.py`; `runtime/test_evidence_landscape_boundary.py`; `reviewer/test_evidence_promotion.py` | Unified CI Run 37232354912: **48 passed** | PASS | **Reviewed Core** |
| C-03 | Candidate Non-Authority | Candidate remains proposal, not approval/execution authority. | `tests/test_observation_candidate.py::test_candidate_is_not_authorized_or_executable`; `tests/test_oppai_candidate_discovery.py::test_candidate_discovery_does_not_activate_a_protocol`; `tests/test_approval_envelope_provenance.py` | Unified CI Run 37232354912: **48 passed** | PASS | **Reviewed Core** |
| C-04 | Context Non-Authority | Context/Handoff carries state but does not grant authority. | `runtime/test_core_invariants.py`: serialization, absent authority attributes, immutability | Unified CI Run 37232354912: **48 passed** | PASS | **Reviewed Core** |
| C-05 | Uncertainty Preservation | Unresolved semantics remain explicit. | `runtime/test_evolution_bridge.py`: uncertainty preservation/non-authority | Unified CI Run 37232354912: **48 passed**; independent 9 passed | PASS | **Reviewed Core** |
| C-06 | Structural/Semantic Separation | Structural validity does not establish domain truth. | `tests/test_structural_validation_human_gate.py`; `tests/test_pipeline_runner.py`; `runtime/test_evidence_landscape_boundary.py` | Unified CI Run 37232354912: **48 passed** | PASS | **Core Supporting Principle** |
| C-07 | Verification Non-Authority | Verification does not authorize subsequent action. | `runtime/test_agent_activity_verification.py`; `runtime/test_trace.py`; `tests/test_pipeline_runner.py` | Unified CI Run 37232354912: **48 passed** | PASS | **Reviewed Core** |
| C-08 | Runtime Replaceability | Runtime/provider is replaceable and cannot redefine authority semantics. | `runtime/test_runtime_replaceability.py`, including EvidenceDrivenRuntime alternate runtime path | Unified CI Run 37232354912: **48 passed**; independent 3 passed | PASS | **Core Supporting Principle** |
| C-09 | Evidence Replayability | Evidence remains usable for defined replay/reconstruction. | `runtime/test_landscape_replay_determinism.py::test_evidence_replay_reconstructs_identical_landscape`; `runtime/evidence_replay.py`; `runtime/replay.py`; `runtime/evidence_checkpoint.py` | Unified CI Run 37232354912: **48 passed** | PASS | **Core Supporting Principle** |
| C-10 | Human Gate for Promotion | Promotion to authorized state requires Human Gate. | `reviewer/test_evidence_promotion.py`; `runtime/test_approval_envelope_human_gate.py`; `runtime/test_api.py::test_human_gate_requires_explicit_authorization` | Unified CI Run 37232354912: **48 passed** | PASS | **Reviewed Core** |

## Evidence levels

- **PASS**: implementation and deterministic test evidence identified.
- **PARTIAL**: implementation or tests exist, but the deterministic evidence chain is incomplete.
- **GAP**: normative claim exists without sufficient implementation/test evidence.
- **HUMAN REVIEW**: technical evidence exists and the model decision is awaiting Human Gate.

## Current assessment

Technical coverage of C-01 through C-10 is **PASS for implementation/test evidence** based on the unified audit record.

The 2026-10-05 Human Gate decision is now complete within a defined scope:

### Reviewed Core

- C-01 Human Authority
- C-02 Evidence Non-Authority
- C-03 Candidate Non-Authority
- C-04 Context Non-Authority
- C-05 Uncertainty Preservation
- C-07 Verification Non-Authority
- C-10 Human Gate for Promotion

### Core Supporting Principles

- C-06 Structural/Semantic Separation
- C-08 Runtime Replaceability
- C-09 Evidence Replayability

The supporting principles remain normative supporting constraints but are not treated as equivalent to the seven Reviewed Core invariants.

## What the decision does not claim

This decision is deliberately not equivalent to:

- semantic truth;
- production readiness;
- security certification;
- external validation;
- patentability;
- universal interoperability.

## Promotion rule

An invariant should be promoted from audit evidence to Core status only after:

1. normative wording is explicit;
2. implementation behavior is identified;
3. deterministic test is identified;
4. CI/evidence artifact is recorded;
5. Human Gate review is completed.

For the 2026-10-05 decision, the seven Reviewed Core invariants satisfy this promotion rule within the stated scope. The three Supporting Principles remain independently revisable.

Human Gate decision: **APPROVED WITH SCOPE**.
Decision record: `docs/HUMAN_GATE_DECISION_RECORD_v0.1.md`.
