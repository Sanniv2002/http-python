"""init

Revision ID: 1a4d5f1c5171
Revises: 6b429fe9f0d9
Create Date: 2024-06-09 04:10:48.469686

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a4d5f1c5171'
down_revision: Union[str, None] = '6b429fe9f0d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
