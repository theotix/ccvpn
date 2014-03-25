"""add vpnsessions table

Revision ID: 12e8cae9c38
Revises: 25883baca06
Create Date: 2014-03-23 02:11:37.838134

"""

# revision identifiers, used by Alembic.
revision = '12e8cae9c38'
down_revision = '25883baca06'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vpnsessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gateway_id', sa.Integer(), nullable=False),
    sa.Column('gateway_version', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('connect_date', sa.DateTime(), nullable=False),
    sa.Column('disconnect_date', sa.DateTime(), nullable=True),
    sa.Column('remote_addr', sa.String(), nullable=False),
    sa.Column('bytes_up', sa.Integer(), nullable=True),
    sa.Column('bytes_down', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gateway_id'], ['gateways.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vpnsessions')
    ### end Alembic commands ###