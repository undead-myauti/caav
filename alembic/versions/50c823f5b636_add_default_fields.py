"""add_default_fields

Revision ID: 50c823f5b636
Revises: 
Create Date: 2025-06-16 09:02:39.728357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '50c823f5b636'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'incomes',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('value', sa.Float(), nullable=False),
    )

    op.execute("INSERT INTO incomes (value) VALUES (0)")

    op.create_table(
        'expenses',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('value', sa.Float(), nullable=False),
    )

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('incomes')
    op.drop_table('expenses')
