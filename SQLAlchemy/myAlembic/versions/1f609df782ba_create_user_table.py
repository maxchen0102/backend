"""create user table

Revision ID: 1f609df782ba
Revises: fdb35b469a7d
Create Date: 2024-02-15 13:25:56.726702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f609df782ba'
down_revision: Union[str, None] = 'fdb35b469a7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
