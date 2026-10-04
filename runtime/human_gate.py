from dataclasses import dataclass
from enum import Enum


class HumanGateStatus(str, Enum):
    AUDIT = "AUDIT"
    REVIEW_PENDING = "REVIEW_PENDING"
    APPROVED = "APPROVED"
    RETURNED = "RETURNED"
    REJECTED = "REJECTED"


@dataclass(frozen=True)
class HumanGateRecord:
    status: HumanGateStatus
    technical_audit: str
    core_promotion: bool
    decision: str | None = None
    scope: str | None = None
    conditions: str | None = None
    decision_maker: str | None = None
    decided_at: str | None = None


def review_pending(technical_audit: str = "PASS") -> HumanGateRecord:
    return HumanGateRecord(
        status=HumanGateStatus.REVIEW_PENDING,
        technical_audit=technical_audit,
        core_promotion=False,
    )


def approve(
    record: HumanGateRecord,
    *,
    decision_maker: str,
    decided_at: str,
    scope: str,
    conditions: str = "",
) -> HumanGateRecord:
    if record.status is not HumanGateStatus.REVIEW_PENDING:
        raise ValueError("Human Gate approval requires REVIEW_PENDING state")
    if not decision_maker or not decided_at or not scope:
        raise ValueError("Human Gate approval requires attributable decision, date, and scope")
    return HumanGateRecord(
        status=HumanGateStatus.APPROVED,
        technical_audit=record.technical_audit,
        core_promotion=True,
        decision="APPROVED",
        scope=scope,
        conditions=conditions,
        decision_maker=decision_maker,
        decided_at=decided_at,
    )


def automation_cannot_approve(record: HumanGateRecord) -> HumanGateRecord:
    if record.status is HumanGateStatus.REVIEW_PENDING:
        return record
    raise ValueError("Automation cannot create or alter Human Gate approval")
