# SHBB API

**Shirakami High School Brass Band API** — runnable reference implementation.

SHBB is not a seven-character chatbot. It is an interface for placing unresolved questions into a shared Landscape, observing them from multiple viewpoints, revisiting them, and recording the user's own Catch.

## Run locally

```bash
cd shbb-api
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn src.app:app --reload
```

Then open `http://127.0.0.1:8000/docs` for the interactive API documentation.

## Endpoints

- `GET /health` — runtime health check
- `POST /observe` — place an input into observation
- `GET /landscape` — inspect the current Landscape snapshot
- `GET /dark-layer` — inspect unresolved questions and revisits
- `POST /revisit` — return to an unresolved question
- `POST /catch` — record the user's Catch

## Runtime boundary

The current implementation is intentionally provider-neutral and in-memory. It proves the HTTP contract and Landscape flow without requiring an LLM. A future Model Provider adapter can enrich `/observe` and `/revisit` while preserving the public SHBB interface.

This is **v0.1 runnable reference**, not a production deployment or durable storage layer.

## Design rules

1. answer-firstではなく observation-first
2. 7人は固定専門Roleではなく観測点
3. 同一Landscapeを共有する
4. 不確実性・矛盾・未完成な問いを保持する
5. Dark Layerを「今は答えなくてよい問い」の保留域として扱う
6. Catchの主体はユーザー
7. LLM Providerは交換可能
8. RuntimeはEvidenceをRecord and Preserveする

## Modes

`normal`: 通常の観測。

`rainwater`: Dark Layerの活動を高め、問いの再観測・接続を促進するBoost Mode。強制解決は行わない。
