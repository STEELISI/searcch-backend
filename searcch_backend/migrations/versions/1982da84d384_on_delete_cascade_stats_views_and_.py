"""on delete cascade stats views and artifact tags

Revision ID: 1982da84d384
Revises: cc6a7492beea
Create Date: 2025-01-27 22:58:57.747482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1982da84d384'
down_revision = 'cc6a7492beea'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('artifact_tags_artifact_id_fkey', 'artifact_tags', type_='foreignkey')
    op.create_foreign_key('artifact_tags_artifact_id_fkey', 'artifact_tags', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('stats_views_artifact_group_id_fkey', 'stats_views', type_='foreignkey')
    op.create_foreign_key('stats_views_artifact_group_id_fkey', 'stats_views', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('artifact_tags_artifact_id_fkey', 'artifact_tags', type_='foreignkey')
    op.create_foreign_key('artifact_tags_artifact_id_fkey', 'artifact_tags', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('stats_views_artifact_group_id_fkey', 'stats_views', type_='foreignkey')
    op.create_foreign_key('stats_views_artifact_group_id_fkey', 'stats_views', 'artifact_groups', ['artifact_group_id'], ['id'])
    pass
