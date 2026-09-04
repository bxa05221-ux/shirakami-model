# SHBB-API v0.1

**Shirakami High School Brass Band API**

白神高校ブラスバンド部を「7人のキャラクターAI」としてではなく、未確定な問いをLandscapeへ投入し、観測・蓄積・再観測するためのインターフェースとして実装する最小仕様。

## Core endpoints

- `POST /observe` — 観測開始
- `GET /landscape` — Landscape取得
- `GET /dark-layer` — 未解決問い取得
- `POST /revisit` — 再観測
- `POST /catch` — ユーザーの再発見を記録

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

## Boundary

このAPIは「回答API」ではない。問いが別の問い・観測・Landscapeと接続できる状態を維持することを中心機能とする。

## Narrative / Physical interface

SHBB-APIは、白神高校ブラスバンド部という同一Landscapeに対するMachine Interfaceである。小説はHuman/Narrative Interface、将来的な部員証・カード等のノベルティはPhysical Interfaceとして接続できる。

## Status

v0.1 / implementation-oriented draft
