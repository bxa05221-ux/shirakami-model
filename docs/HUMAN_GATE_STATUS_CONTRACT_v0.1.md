# Human Gate Status Contract v0.1

Status: draft / review required
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

## 5. Current state

For C-01 through C-10:

    technical_audit: PASS
    human_gate_status: REVIEW_PENDING
    core_promotion: false

The unified audit result is evidence for technical_audit, not a value for human_gate_status.

## 6. Approval record

An approval is valid only when a human records:

- decision;
- scope;
- conditions or limitations, if any;
- date;
- identity/signature appropriate to the governing process.

Until these fields exist, core_promotion remains false.

## 7. Change control

A revision to any normative Core invariant after approval requires a new review decision if the change alters authority semantics, Evidence semantics, Context/Handoff semantics, Candidate semantics, Human Gate behavior, Runtime authority boundaries, or Verification authority boundaries.

## 8. Non-self-authorization invariant

The following implication is normative:

    CI_PASS != HUMAN_GATE_APPROVED

More strongly: technical evidence may satisfy a review prerequisite but can never satisfy the authorization event itself.

## 9. Relationship to canonical model

This contract operationalizes C-01 Human Authority, C-10 Human Gate for Promotion, and the four-way separation between structural validity, semantic truth, human authorization, and verified outcome.

It does not itself approve C-01 through C-10.
