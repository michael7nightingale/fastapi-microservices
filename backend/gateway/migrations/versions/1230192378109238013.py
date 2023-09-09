"""empty message

Revision ID: 1230192378109238013
Revises:
Create Date: 2023-08-22 11:25:28.834276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1230192378109238013'
down_revision: Union[str, None] = "8cda4319137c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_unique_constraint("bg_uix_1", "basketgoods", ['good', 'basket'])


def downgrade() -> None:
    pass
