"""Add email column for users

Revision ID: e4ac368022e3
Revises: 8e50bd5cf23a
Create Date: 2022-08-10 16:23:28.310165

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, String


# revision identifiers, used by Alembic.
revision = 'e4ac368022e3'
down_revision = '8e50bd5cf23a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("users", Column("email", String(), nullable=False))


def downgrade():
    pass
