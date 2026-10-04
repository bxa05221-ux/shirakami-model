# Human Gate Status Contract v0.1

Status: approved within the 2026-10-05 Human Gate decision scope
Date: 2026-10-05

## 1. Purpose

This contract defines the boundary between technical audit evidence and Human Gate authorization.

The purpose is to prevent a successful test suite, CI workflow, AI analysis, or Runtime execution from silently promoting a model invariant into approved Core status.

## 2. State machine

AUDIT -> REVIEW_PENDING -> APPROVED / RETURNED / REJECTED

RETURNED may lead to a revised AUDIT and a new review cycle.

## 3. Authority of states

| State | Meaning | Who/what may establish it |
|---|---|---|
| AUDIT | Technical evidence is being collected | implementation/CI |
| REVIEW_PENDING | Evidence is ready for human review | explicit model/review workflow |
| APPROVED | Human Gate accepted the proposal within stated scope | Human Gate only |
| RETURNED | Human Gate requires revision or additional evidence | Human Gate only |
| REJECTED | Human Gate declined the proposal | Human Gate only |

## 4. Forbidden promotion paths

The following must never imply APPROVED:

- CI success;
- test PASS;
- workflow success;
- AI-generated recommendation;
- Runtime execution success;
- structural validation;
- Evidence creation;
- Verification success;
- API success;
- pull-request approval by automation.

## 5. Current decision state

The 2026-10-05 Human Gate decision approved only the selected Reviewed Core set:

    technical_audit: PASS
    human_gate_status: APPROVED
    core_promotion: true

Reviewed Core:
- C-01
- C-02
- C-03
- C-04
- C-05
- C-07
- C-10

Supporting Core Principles:
- C-06
- C-08
- C-09

This does not approve the three supporting principles as equivalent Reviewed Core invariants.

## 6. Approval record

An approval is valid only when a human records:

- decision;
- scope;
- conditions or limitations, if any;
- date;
- identity/signature appropriate to the governing process.

The approval record is docs/HUMAN_GATE_DECISION_RECORD_v0.1.md.

## 7. Change control

A revision to any normative Core invariant after approval requires a new review decision if the change alters authority semantics, Evidence semantics, Context/Handoff semantics, Candidate semantics, Human Gate behavior, Runtime authority boundaries, or Verification authority boundaries.

## 8. Non-self-authorization invariant

The following implication is normative:

    CI_PASS != HUMAN_GATE_APPROVED

Technical evidence may satisfy a review prerequisite but can never satisfy the authorization event itself.

## 9. Relationship to canonical model

This contract operationalizes C-01 Human Authority, C-10 Human Gate for Promotion, and the four-way separation between structural validity, semantic truth, human authorization, and verified outcome.

The 2026-10-05 decision promotes the seven selected invariants within the stated scope and conditions.
