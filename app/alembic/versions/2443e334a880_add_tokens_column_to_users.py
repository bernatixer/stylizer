"""Add tokens column to users

Revision ID: 2443e334a880
Revises: e4ac368022e3
Create Date: 2022-08-10 16:43:52.341649

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2443e334a880'
down_revision = 'e4ac368022e3'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", sa.Column("tokens", sa.Integer(), nullable=False))


def downgrade():
    pass
