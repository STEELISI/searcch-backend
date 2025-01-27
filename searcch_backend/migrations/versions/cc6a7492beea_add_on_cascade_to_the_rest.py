"""add on cascade to the rest

Revision ID: cc6a7492beea
Revises: 624fedc850d9
Create Date: 2025-01-27 22:36:00.714530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc6a7492beea'
down_revision = '624fedc850d9'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('artifact_files_artifact_id_fkey', 'artifact_files', type_='foreignkey')
    op.create_foreign_key('artifact_files_artifact_id_fkey', 'artifact_files', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_imports_artifact_id_fkey', 'artifact_imports', type_='foreignkey')
    op.create_foreign_key('artifact_imports_artifact_id_fkey', 'artifact_imports', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_metadata_artifact_id_fkey', 'artifact_metadata', type_='foreignkey')
    op.create_foreign_key('artifact_metadata_artifact_id_fkey', 'artifact_metadata', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_publications_artifact_id_fkey', 'artifact_publications', type_='foreignkey')
    op.create_foreign_key('artifact_publications_artifact_id_fkey', 'artifact_publications', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifacts_parent_id_fkey', 'artifacts', type_='foreignkey')
    op.create_foreign_key('artifacts_parent_id_fkey', 'artifacts', 'artifacts', ['parent_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_file_members_parent_file_id_fkey', 'artifact_file_members', type_='foreignkey')
    op.create_foreign_key('artifact_file_members_parent_file_id_fkey', 'artifact_file_members', 'artifact_files', ['parent_file_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_groups_publication_id_fkey', 'artifact_groups', type_='foreignkey')
    op.create_foreign_key('artifact_groups_publication_id_fkey', 'artifact_groups', 'artifact_publications', ['publication_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifacts_artifact_group_id_fkey', 'artifacts', type_='foreignkey')
    op.create_foreign_key('artifacts_artifact_group_id_fkey', 'artifacts', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')    
    pass


def downgrade():
    op.drop_constraint('artifact_files_artifact_id_fkey', 'artifact_files', type_='foreignkey')
    op.create_foreign_key('artifact_files_artifact_id_fkey', 'artifact_files', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_imports_artifact_id_fkey', 'artifact_imports', type_='foreignkey')
    op.create_foreign_key('artifact_imports_artifact_id_fkey', 'artifact_imports', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_metadata_artifact_id_fkey', 'artifact_metadata', type_='foreignkey')
    op.create_foreign_key('artifact_metadata_artifact_id_fkey', 'artifact_metadata', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_publications_artifact_id_fkey', 'artifact_publications', type_='foreignkey')
    op.create_foreign_key('artifact_publications_artifact_id_fkey', 'artifact_publications', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifacts_parent_id_fkey', 'artifacts', type_='foreignkey')
    op.create_foreign_key('artifacts_parent_id_fkey', 'artifacts', 'artifacts', ['parent_id'], ['id'])
    op.drop_constraint('artifact_file_members_parent_file_id_fkey', 'artifact_file_members', type_='foreignkey')
    op.create_foreign_key('artifact_file_members_parent_file_id_fkey', 'artifact_file_members', 'artifact_files', ['parent_file_id'], ['id'])
    op.drop_constraint('artifact_groups_publication_id_fkey', 'artifact_groups', type_='foreignkey')
    op.create_foreign_key('artifact_groups_publication_id_fkey', 'artifact_groups', 'artifact_publications', ['publication_id'], ['id'])
    op.drop_constraint('artifacts_artifact_group_id_fkey', 'artifacts', type_='foreignkey')
    op.create_foreign_key('artifacts_artifact_group_id_fkey', 'artifacts', 'artifact_groups', ['artifact_group_id'], ['id'])
    pass
