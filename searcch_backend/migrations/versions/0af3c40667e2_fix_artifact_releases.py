"""fix artifact releases

Revision ID: 0af3c40667e2
Revises: 1982da84d384
Create Date: 2025-01-29 22:28:02.380388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0af3c40667e2'
down_revision = '1982da84d384'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_constraint('artifact_releases_artifact_id_fkey', 'artifact_releases', type_='foreignkey')
    op.create_foreign_key('artifact_releases_artifact_id_fkey', 'artifact_releases', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_badges_artifact_id_fkey', 'artifact_badges', type_='foreignkey')
    op.create_foreign_key('artifact_badges_artifact_id_fkey', 'artifact_badges', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_curations_artifact_id_fkey', 'artifact_curations', type_='foreignkey')
    op.create_foreign_key('artifact_curations_artifact_id_fkey', 'artifact_curations', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_favorites_artifact_id_fkey', 'artifact_favorites', type_='foreignkey')
    op.create_foreign_key('artifact_favorites_artifact_id_fkey', 'artifact_favorites', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_favorites_artifact_group_id_fkey', 'artifact_favorites', type_='foreignkey')
    op.create_foreign_key('artifact_favorites_artifact_group_id_fkey', 'artifact_favorites', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_funding_artifact_id_fkey', 'artifact_funding', type_='foreignkey')
    op.create_foreign_key('artifact_funding_artifact_id_fkey', 'artifact_funding', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_owner_request_artifact_group_id_fkey', 'artifact_owner_request', type_='foreignkey')
    op.create_foreign_key('artifact_owner_request_artifact_group_id_fkey', 'artifact_owner_request', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_ratings_artifact_group_id_fkey', 'artifact_ratings', type_='foreignkey')
    op.create_foreign_key('artifact_ratings_artifact_group_id_fkey', 'artifact_ratings', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_ratings_artifact_id_fkey', 'artifact_ratings', type_='foreignkey')
    op.create_foreign_key('artifact_ratings_artifact_id_fkey', 'artifact_ratings', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_reviews_artifact_group_id_fkey', 'artifact_reviews', type_='foreignkey')
    op.create_foreign_key('artifact_reviews_artifact_group_id_fkey', 'artifact_reviews', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_reviews_artifact_group_id_fkey1', 'artifact_reviews', type_='foreignkey')
    op.drop_constraint('artifact_venues_artifact_id_fkey', 'artifact_venues', type_='foreignkey')
    op.create_foreign_key('artifact_venues_artifact_id_fkey', 'artifact_venues', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_reviews_artifact_group_id_fkey', 'artifact_reviews', type_='foreignkey')
    op.drop_constraint('artifact_relationships_artifact_group_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_artifact_group_id_fkey', 'artifact_relationships', 'artifact_groups', ['artifact_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_relationships_artifact_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_artifact_id_fkey', 'artifact_relationships', 'artifacts', ['artifact_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_relationships_related_artifact_group_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_related_artifact_group_id_fkey', 'artifact_relationships', 'artifact_groups', ['related_artifact_group_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('artifact_relationships_related_artifact_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_related_artifact_id_fkey', 'artifact_relationships', 'artifacts', ['related_artifact_id'], ['id'], ondelete='CASCADE')    
    pass


def downgrade():
    op.drop_constraint('artifact_releases_artifact_id_fkey', 'artifact_releases', type_='foreignkey')
    op.create_foreign_key('artifact_releases_artifact_id_fkey', 'artifact_releases', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_badges_artifact_id_fkey', 'artifact_badges', type_='foreignkey')
    op.create_foreign_key('artifact_badges_artifact_id_fkey', 'artifact_badges', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_curations_artifact_id_fkey', 'artifact_curations', type_='foreignkey')
    op.create_foreign_key('artifact_curations_artifact_id_fkey', 'artifact_curations', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_favorites_artifact_id_fkey', 'artifact_favorites', type_='foreignkey')
    op.create_foreign_key('artifact_favorites_artifact_id_fkey', 'artifact_favorites', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_favorites_artifact_group_id_fkey', 'artifact_favorites', type_='foreignkey')
    op.create_foreign_key('artifact_favorites_artifact_group_id_fkey', 'artifact_favorites', 'artifact_groups', ['artifact_group_id'], ['id'])
    op.drop_constraint('artifact_funding_artifact_id_fkey', 'artifact_funding', type_='foreignkey')
    op.create_foreign_key('artifact_funding_artifact_id_fkey', 'artifact_funding', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_owner_request_artifact_group_id_fkey', 'artifact_owner_request', type_='foreignkey')
    op.create_foreign_key('artifact_owner_request_artifact_group_id_fkey', 'artifact_owner_request', 'artifact_groups', ['artifact_group_id'], ['id'])
    op.drop_constraint('artifact_ratings_artifact_group_id_fkey', 'artifact_ratings', type_='foreignkey')
    op.create_foreign_key('artifact_ratings_artifact_group_id_fkey', 'artifact_ratings', 'artifact_groups', ['artifact_group_id'], ['id'])
    op.drop_constraint('artifact_ratings_artifact_id_fkey', 'artifact_ratings', type_='foreignkey')
    op.create_foreign_key('artifact_ratings_artifact_id_fkey', 'artifact_ratings', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_reviews_artifact_group_id_fkey', 'artifact_reviews', type_='foreignkey')
    op.create_foreign_key('artifact_reviews_artifact_group_id_fkey', 'artifact_reviews', 'artifact_groups', ['artifact_group_id'], ['id'])
    op.drop_constraint('artifact_venues_artifact_id_fkey', 'artifact_venues', type_='foreignkey')
    op.create_foreign_key('artifact_venues_artifact_id_fkey', 'artifact_venues', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_reviews_artifact_group_id_fkey', 'artifact_reviews', type_='foreignkey')
    op.drop_constraint('artifact_relationships_artifact_group_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_artifact_group_id_fkey', 'artifact_relationships', 'artifact_groups', ['artifact_group_id'], ['id'])
    op.drop_constraint('artifact_relationships_artifact_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_artifact_id_fkey', 'artifact_relationships', 'artifacts', ['artifact_id'], ['id'])
    op.drop_constraint('artifact_relationships_related_artifact_group_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_related_artifact_group_id_fkey', 'artifact_relationships', 'artifact_groups', ['related_artifact_group_id'], ['id'])
    op.drop_constraint('artifact_relationships_related_artifact_id_fkey', 'artifact_relationships', type_='foreignkey')
    op.create_foreign_key('artifact_relationships_related_artifact_id_fkey', 'artifact_relationships', 'artifacts', ['related_artifact_id'], ['id'])
    pass