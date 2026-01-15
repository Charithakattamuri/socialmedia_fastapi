"""add last few cols to posts table

Revision ID: 552b27ebb259
Revises: ae792a87042e
Create Date: 2026-01-14 23:36:21.231737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '552b27ebb259'
down_revision: Union[str, Sequence[str], None] = 'ae792a87042e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
     op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False))
     op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))  

     pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
