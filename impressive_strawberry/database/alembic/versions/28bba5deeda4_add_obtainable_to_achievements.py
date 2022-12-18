"""Add obtainable to achievements

Revision ID: 28bba5deeda4
Revises: b33f0ec71a4b
Create Date: 2022-10-25 10:06:44.192971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28bba5deeda4'
down_revision = 'b33f0ec71a4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('achievements', sa.Column('obtainable', sa.Boolean(), nullable=False, server_default="TRUE"))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('achievements', 'obtainable')
    # ### end Alembic commands ###
