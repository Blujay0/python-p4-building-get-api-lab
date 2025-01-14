"""<data>

Revision ID: c2ff7c9a0dff
Revises: 7a1a2a353d2e
Create Date: 2023-06-25 07:46:56.585897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2ff7c9a0dff'
down_revision = '7a1a2a353d2e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.Integer(), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('bakery_id')
        batch_op.drop_column('price')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('price', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('bakery_id', sa.INTEGER(), nullable=False))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('baked_goods', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.drop_column('price')

    # ### end Alembic commands ###
