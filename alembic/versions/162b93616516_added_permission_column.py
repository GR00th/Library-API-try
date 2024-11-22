"""added permission column

Revision ID: 162b93616516
Revises: cdda1358fd54
Create Date: 2024-04-02 04:49:23.854304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '162b93616516'
down_revision: Union[str, None] = 'cdda1358fd54'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('roles', sa.Column('permission', sa.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('roles', 'permission')
    # ### end Alembic commands ###
