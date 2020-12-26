"""add last_checked

Revision ID: c7d8b1ffb496
Revises: 608b679f7b6d
Create Date: 2020-12-26 16:27:18.081099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7d8b1ffb496'
down_revision = '608b679f7b6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('record', sa.Column('latency', sa.Integer(), nullable=True))
    op.add_column('record', sa.Column('online', sa.Boolean(), nullable=False))
    op.add_column('record', sa.Column('time', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('record', 'time')
    op.drop_column('record', 'online')
    op.drop_column('record', 'latency')
    # ### end Alembic commands ###