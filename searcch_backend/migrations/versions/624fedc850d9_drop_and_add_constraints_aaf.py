"""drop and add constraints aaf

Revision ID: 624fedc850d9
Revises: 808535f66e29
Create Date: 2025-01-27 21:33:08.732976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '624fedc850d9'
down_revision = '808535f66e29'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('artifact_affiliations_artifact_id_fkey', 'artifact_affiliations', type_='foreignkey')
    op.create_foreign_key('artifact_affiliations_artifact_id_fkey', 'artifact_affiliations', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('artifact_affiliations_artifact_id_fkey', 'artifact_affiliations', type_='foreignkey')
    op.create_foreign_key('artifact_affiliations_artifact_id_fkey', 'artifact_affiliations', 'artifacts', ['artifact_id'], ['id'])
    pass
