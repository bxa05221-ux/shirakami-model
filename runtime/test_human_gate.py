from human_gate import HumanGateStatus, approve, automation_cannot_approve, review_pending


def test_ci_pass_does_not_promote_core():
    record = review_pending("PASS")
    assert record.status is HumanGateStatus.REVIEW_PENDING
    assert record.core_promotion is False


def test_automation_cannot_promote_review_pending():
    record = review_pending("PASS")
    result = automation_cannot_approve(record)
    assert result == record
    assert result.status is HumanGateStatus.REVIEW_PENDING
    assert result.core_promotion is False


def test_approval_requires_attributable_human_decision():
    record = review_pending("PASS")

    try:
        approve(record, decision_maker="", decided_at="2026-10-05", scope="C-01..C-10")
    except ValueError:
        pass
    else:
        raise AssertionError("approval must require an attributable decision maker")


def test_approval_is_distinct_from_technical_audit():
    record = review_pending("PASS")
    approved = approve(
        record,
        decision_maker="HUMAN_GATE",
        decided_at="2026-10-05",
        scope="C-01..C-10",
    )
    assert approved.technical_audit == "PASS"
    assert approved.status is HumanGateStatus.APPROVED
    assert approved.core_promotion is True
