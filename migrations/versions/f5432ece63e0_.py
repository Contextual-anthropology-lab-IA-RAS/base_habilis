"""empty message

Revision ID: f5432ece63e0
Revises: 81a1b74cec67
Create Date: 2024-12-13 14:57:09.986957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5432ece63e0'
down_revision = '81a1b74cec67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('individs', schema=None) as batch_op:
        batch_op.add_column(sa.Column('comment_temp', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('individs', schema=None) as batch_op:
        batch_op.drop_column('comment_temp')

    # ### end Alembic commands ###
