"""Add user column on transformations table

Revision ID: bd13f63c0391
Revises: 2443e334a880
Create Date: 2022-09-08 23:03:46.766078

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, ForeignKey


# revision identifiers, used by Alembic.
revision = 'bd13f63c0391'
down_revision = '2443e334a880'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("transformations", Column("user", Integer, ForeignKey("users.id")))


def downgrade():
    pass
