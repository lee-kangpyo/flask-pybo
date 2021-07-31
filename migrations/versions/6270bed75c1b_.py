"""empty message

Revision ID: 6270bed75c1b
Revises: cb4abc76cdd4
Create Date: 2021-01-11 15:52:27.619408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6270bed75c1b'
down_revision = 'cb4abc76cdd4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text("'1'"))

    # ### end Alembic commands ###
