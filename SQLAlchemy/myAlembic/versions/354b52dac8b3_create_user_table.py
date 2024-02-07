"""create user table

Revision ID: 354b52dac8b3
Revises: 
Create Date: 2024-02-07 17:33:20.523041

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '354b52dac8b3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'user',
        sa.Column("userID",sa.Integer,primary_key=True) ,
        sa.Column('userName',sa.String,nullable=False)
    )


def downgrade():
    op.drop_table('user')
