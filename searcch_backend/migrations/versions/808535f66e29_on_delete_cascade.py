"""on delete cascade

Revision ID: 808535f66e29
Revises: e19bc43b8023
Create Date: 2025-01-26 23:50:45.955363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '808535f66e29'
down_revision = 'e19bc43b8023'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('artifact_affiliations', 'artifact_id', sa.ForeignKey('artifacts.id', ondelete='CASCADE'))
    op.alter_column('artifact_files', 'artifact_id', sa.ForeignKey('artifacts.id', ondelete='CASCADE'))
    op.alter_column('artifact_file_members', 'parent_file_id', sa.ForeignKey('artifact_files.id', ondelete='CASCADE'))
    op.alter_column('artifact_imports', 'artifact_id', sa.ForeignKey('artifacts.id', ondelete='CASCADE'))
    op.alter_column('artifact_metadata', 'artifact_id', sa.ForeignKey('artifacts.id', ondelete='CASCADE'))
    op.alter_column('artifact_tags', 'artifact_id', sa.ForeignKey('artifacts.id', ondelete='CASCADE'))
    pass


def downgrade():
    op.drop_contraint('artifact_affiliations', 'artifact_id')
    op.drop_contraint('artifact_files', 'artifact_id')
    op.drop_contraint('artifact_file_members', 'parent.file_id')
    op.drop_contraint('artifact_imports', 'artifact_id')
    op.drop_contraint('artifact_metadata', 'artifact_id')
    op.drop_contraint('artifact_tags', 'artifact_id')
    pass
