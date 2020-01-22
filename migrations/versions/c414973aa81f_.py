"""empty message

Revision ID: c414973aa81f
Revises: 54ba0f59df66
Create Date: 2020-01-14 13:13:08.987268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c414973aa81f'
down_revision = '54ba0f59df66'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('book_ibfk_1', 'book', type_='foreignkey')
    op.create_foreign_key(None, 'book', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('cart_ibfk_3', 'cart', type_='foreignkey')
    op.drop_constraint('cart_ibfk_2', 'cart', type_='foreignkey')
    op.create_foreign_key(None, 'cart', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'cart', 'book', ['book_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('payment_ibfk_1', 'payment', type_='foreignkey')
    op.create_foreign_key(None, 'payment', 'cart', ['cart_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payment', type_='foreignkey')
    op.create_foreign_key('payment_ibfk_1', 'payment', 'cart', ['cart_id'], ['id'])
    op.drop_constraint(None, 'cart', type_='foreignkey')
    op.drop_constraint(None, 'cart', type_='foreignkey')
    op.create_foreign_key('cart_ibfk_2', 'cart', 'user', ['user_id'], ['id'])
    op.create_foreign_key('cart_ibfk_3', 'cart', 'book', ['book_id'], ['id'])
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.create_foreign_key('book_ibfk_1', 'book', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
