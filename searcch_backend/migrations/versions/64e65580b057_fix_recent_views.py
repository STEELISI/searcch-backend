"""fix recent views

Revision ID: 64e65580b057
Revises: 0af3c40667e2
Create Date: 2025-01-31 18:52:04.931736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64e65580b057'
down_revision = '0af3c40667e2'
branch_labels = None
depends_on = None


def upgrade():
   op.drop_constraint('recent_views_artifact_group_id_fkey', 'recent_views', type_='foreignkey')
   op.create_foreign_key('recent_views_artifact_group_id_fkey', 'recent_views', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')
   pass


def downgrade():
    op.drop_constraint('recent_views_artifact_group_id_fkey', 'recent_views', type_='foreignkey')
    op.create_foreign_key('recent_views_artifact_group_id_fkey', 'recent_views', 'artifact_groups', ['artifact_group_id'], ['id'])
    pass
