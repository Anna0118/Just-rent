"""add status column to reservation model

Revision ID: beca58e78f20
Revises: 7b2654c4c0b2
Create Date: 2024-04-28 03:04:23.942144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beca58e78f20'
down_revision = '7b2654c4c0b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservations', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###
