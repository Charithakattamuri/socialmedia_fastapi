"""add content col to posts table

Revision ID: 49d028788161
Revises: 3ea6c7a9066e
Create Date: 2026-01-14 23:00:52.197942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '49d028788161'
down_revision: Union[str, Sequence[str], None] = '3ea6c7a9066e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
