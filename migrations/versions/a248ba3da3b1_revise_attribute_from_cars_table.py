"""revise attribute from  cars table

Revision ID: a248ba3da3b1
Revises: 969b7419735c
Create Date: 2024-04-08 18:10:42.934730

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a248ba3da3b1'
down_revision = '969b7419735c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.alter_column('brand',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('year',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.alter_column('model',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('door',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('seat',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cars', schema=None) as batch_op:
        batch_op.alter_column('seat',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('door',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(),
               existing_nullable=False)
        batch_op.alter_column('model',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('year',
               existing_type=sa.Integer(),
               type_=mysql.VARCHAR(length=255),
               existing_nullable=False)
        batch_op.alter_column('brand',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###
