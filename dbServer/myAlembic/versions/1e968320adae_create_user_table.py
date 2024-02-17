"""create user table

Revision ID: 1e968320adae
Revises: 354b52dac8b3
Create Date: 2024-02-07 17:55:55.764350

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e968320adae'
down_revision: Union[str, None] = '354b52dac8b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('user',sa.Column('birthDay',sa.Date))

def downgrade():
    op.drop_column('user','birthDay')