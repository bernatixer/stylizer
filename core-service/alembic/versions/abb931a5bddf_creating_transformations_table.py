"""Creating transformations table

Revision ID: abb931a5bddf
Revises:
Create Date: 2022-06-06 20:08:48.483696

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "abb931a5bddf"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "transformation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("style", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("transformation")
