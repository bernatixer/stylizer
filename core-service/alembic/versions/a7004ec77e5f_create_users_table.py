"""Create users table

Revision ID: a7004ec77e5f
Revises: abb931a5bddf
Create Date: 2022-08-06 16:55:12.227329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7004ec77e5f'
down_revision = 'abb931a5bddf'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    pass
