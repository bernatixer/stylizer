"""Rename Transformation table to plural

Revision ID: 8e50bd5cf23a
Revises: a7004ec77e5f
Create Date: 2022-08-10 15:18:21.431135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e50bd5cf23a'
down_revision = 'a7004ec77e5f'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table("transformation", "transformations")


def downgrade():
    pass
