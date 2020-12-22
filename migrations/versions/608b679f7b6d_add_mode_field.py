"""add mode field

Revision ID: 608b679f7b6d
Revises: 95c8255a3057
Create Date: 2020-12-22 17:48:31.406612

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '608b679f7b6d'
down_revision = '95c8255a3057'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('server', sa.Column('mode', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('server', 'mode')
    # ### end Alembic commands ###
