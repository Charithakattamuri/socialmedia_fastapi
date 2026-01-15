"""add fk to posts table

Revision ID: ae792a87042e
Revises: 47dec74743df
Create Date: 2026-01-14 23:28:32.542886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ae792a87042e'
down_revision: Union[str, Sequence[str], None] = '47dec74743df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', source_table='posts')
    op.drop_column('posts', 'owner_id') 
    pass