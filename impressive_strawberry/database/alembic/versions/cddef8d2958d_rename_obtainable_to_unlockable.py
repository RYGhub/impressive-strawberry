"""Rename obtainable to unlockable

Revision ID: cddef8d2958d
Revises: 28bba5deeda4
Create Date: 2022-10-25 10:10:41.000666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cddef8d2958d'
down_revision = '28bba5deeda4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("achievements", "obtainable", new_column_name="unlockable")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("achievements", "unlockable", new_column_name="obtainable")
    # ### end Alembic commands ###
