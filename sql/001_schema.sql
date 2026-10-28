CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE IF NOT EXISTS media_objects (
    object_id         BIGSERIAL PRIMARY KEY,
    media_type        TEXT NOT NULL CHECK (media_type IN ('image','video')),
    physical_location TEXT NOT NULL,
    size_bytes        BIGINT,
    ts                TIMESTAMPTZ,
    metadata          JSONB NOT NULL DEFAULT '{}',
    embedding         VECTOR(512),
    UNIQUE (physical_location)
);