"""Added cuisine name

Revision ID: 98c35f8160fd
Revises: 42cf0b596af8
Create Date: 2024-01-11 00:00:51.756961

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '98c35f8160fd'
down_revision: Union[str, None] = '42cf0b596af8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cuisines', sa.Column('cuisine_name', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'cuisines', ['cuisine_name'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cuisines', type_='unique')
    op.drop_column('cuisines', 'cuisine_name')
    # ### end Alembic commands ###