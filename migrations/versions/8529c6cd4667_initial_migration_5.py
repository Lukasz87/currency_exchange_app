"""Initial migration 5

Revision ID: 8529c6cd4667
Revises: 925df592f74e
Create Date: 2021-11-23 10:59:35.347209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8529c6cd4667'
down_revision = '925df592f74e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('currency_symbol_key', 'currency', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('currency_symbol_key', 'currency', ['symbol'])
    # ### end Alembic commands ###