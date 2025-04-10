"""refactor Client table

Revision ID: e78ed6c021ea
Revises: 15155f22b76b
Create Date: 2025-04-05 15:02:17.125674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e78ed6c021ea'
down_revision: Union[str, None] = '15155f22b76b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('phone', sa.String(length=12), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients')
    # ### end Alembic commands ###
