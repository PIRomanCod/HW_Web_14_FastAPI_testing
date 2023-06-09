"""add comfirmed email 

Revision ID: 83494b65a6a6
Revises: eb096e492fb0
Create Date: 2023-04-19 17:41:46.686305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83494b65a6a6'
down_revision = 'eb096e492fb0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
