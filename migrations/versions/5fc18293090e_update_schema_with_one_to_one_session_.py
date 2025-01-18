"""Update schema with one-to-one session-interaction
Revision ID: 5fc18293090e
Revises: 964a6420d6b9
Create Date: 2025-01-18 02:33:36.471637
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision: str = '5fc18293090e'
down_revision: Union[str, None] = '964a6420d6b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('new_id', UUID(as_uuid=True), nullable=False, server_default=sa.text('gen_random_uuid()')))
    op.drop_column('users', 'id')
    op.alter_column('users', 'new_id', new_column_name='id')
    op.create_primary_key("pk_users", "users", ["id"])


def downgrade() -> None:
    op.add_column('users', sa.Column('old_id', sa.Integer(), nullable=False, autoincrement=True))
    op.drop_column('users', 'id')
    op.alter_column('users', 'old_id', new_column_name='id')
    op.create_primary_key("pk_users", "users", ["id"])