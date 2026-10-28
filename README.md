# OceanQL

Hybrid metadata + vector search over underwater imagery (FathomNet).

**Status:** in progress (target: Dec 13, 2026)

- [x] Docker Compose stack (Postgres/pgvector, S3-compatible storage)
- [x] Catalog schema
- [ ] Ingestion pipeline
- [ ] CLIP embeddings
- [ ] Evaluation harness (exact-search baseline)
- [ ] Query planner + benchmarks

## Quickstart

cp .env.example .env

# edit .env and set your own passwords

docker compose up -d
