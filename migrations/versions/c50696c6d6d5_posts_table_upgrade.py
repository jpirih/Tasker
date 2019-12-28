"""Posts table upgrade

Revision ID: c50696c6d6d5
Revises: 580210a97519
Create Date: 2019-12-26 17:57:40.295420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c50696c6d6d5'
down_revision = '580210a97519'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('deleted', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'deleted')
    # ### end Alembic commands ###
