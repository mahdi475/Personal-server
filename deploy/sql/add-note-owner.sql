-- One-time change for databases created before authentication was added.
-- Every note now belongs to a user. Old test notes have no owner, so they are removed.
BEGIN;
DELETE FROM notes;
ALTER TABLE notes ADD COLUMN user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE;
CREATE INDEX ix_notes_user_id ON notes (user_id);
COMMIT;
