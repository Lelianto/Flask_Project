"""empty message

Revision ID: b26ec7451363
Revises: 891e5e8362a9
Create Date: 2020-01-04 20:04:04.672033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b26ec7451363'
down_revision = '891e5e8362a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payment_confirm',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('total_biaya', sa.Integer(), nullable=False),
    sa.Column('nomor_pemesanan', sa.String(length=255), nullable=False),
    sa.Column('tanggal_pemesanan', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('payment_confirm')
    # ### end Alembic commands ###
