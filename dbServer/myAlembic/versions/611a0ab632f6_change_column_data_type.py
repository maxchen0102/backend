"""Change column data type

Revision ID: 611a0ab632f6
Revises: 01da5cf82d0e, 15cb4e61dde3, 1e968320adae, 683cff919fe2, 6ecb92515efe
Create Date: 2024-02-17 14:48:38.165508

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '611a0ab632f6'
down_revision: Union[str, None] = ('01da5cf82d0e', '15cb4e61dde3', '1e968320adae', '683cff919fe2', '6ecb92515efe')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alldata', sa.Column('title2222', sa.String(length=100), nullable=True))
    op.drop_column('alldata', 'title')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alldata', sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=True))
    op.drop_column('alldata', 'title2222')
    # ### end Alembic commands ###
