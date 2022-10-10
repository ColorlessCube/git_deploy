"""add project status

Revision ID: 3e1d2131616e
Revises: aa48b640af41
Create Date: 2022-09-20 09:57:32.585117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e1d2131616e'
down_revision = 'aa48b640af41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('last_trig', sa.DateTime(), nullable=True))
    op.add_column('vm', sa.Column('status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('vm', 'status')
    op.drop_column('project', 'last_trig')
    # ### end Alembic commands ###