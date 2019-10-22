"""Upgrade db

Revision ID: d65f9fbe93d2
Revises: a56e3d931382
Create Date: 2019-10-22 11:24:17.046123

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd65f9fbe93d2'
down_revision = 'a56e3d931382'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pitches', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pitches', type_='foreignkey')
    op.drop_column('pitches', 'user_id')
    # ### end Alembic commands ###