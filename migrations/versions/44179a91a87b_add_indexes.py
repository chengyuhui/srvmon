"""add indexes

Revision ID: 44179a91a87b
Revises: ad1f704412f4
Create Date: 2020-12-27 20:49:17.726011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44179a91a87b'
down_revision = 'ad1f704412f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['server_id'], ['server.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_record_server_id'), 'record', ['server_id'], unique=False)
    op.create_index(op.f('ix_record_time'), 'record', ['time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_record_time'), table_name='record')
    op.drop_index(op.f('ix_record_server_id'), table_name='record')
    op.drop_table('notification')
    # ### end Alembic commands ###
