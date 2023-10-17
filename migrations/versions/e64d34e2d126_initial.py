"""initial

Revision ID: e64d34e2d126
Revises: 3b67ab1df379
Create Date: 2023-10-17 16:48:46.193065

"""
from pathlib import Path
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision: str = 'e64d34e2d126'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    dump_path = Path('../azuko.dump')

    with open(dump_path, 'r') as sql_reader:
        op.execute(text(sql_reader.read()))

    op.execute(text('SET search_path = public'))


def downgrade() -> None:
    pass


