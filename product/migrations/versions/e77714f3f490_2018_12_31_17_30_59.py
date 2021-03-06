"""2018.12.31-17.30.59

Revision ID: e77714f3f490
Revises: 9bd1d1bd6a6d
Create Date: 2018-12-31 17:31:00.392248

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e77714f3f490'
down_revision = '9bd1d1bd6a6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_model', 'neu')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_model', sa.Column('neu', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
