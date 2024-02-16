"""init

Revision ID: 74b5be8ced9f
Revises: 
Create Date: 2024-02-16 18:00:38.018386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74b5be8ced9f'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_models'))
    )
    op.create_index('my_index', 'models', ['name'], unique=True, mysql_length=255)
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('my_index', table_name='models', mysql_length=255)
    op.drop_table('models')
    # ### end Alembic commands ###