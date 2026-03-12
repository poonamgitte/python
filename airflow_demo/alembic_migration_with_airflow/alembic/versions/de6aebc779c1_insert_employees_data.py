"""insert employees data

Revision ID: de6aebc779c1
Revises: f120e122bccc
Create Date: 2026-03-04 11:30:52.513296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de6aebc779c1'
down_revision: Union[str, Sequence[str], None] = 'f120e122bccc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade():
    connection = op.get_bind()

    for i in range(1, 151):
        connection.execute(
            sa.text("INSERT INTO employees (name, salary) VALUES (:name, :salary)"),
            {"name": f"Employee {i}", "salary": 1000 + i},
        )

def downgrade():
    connection = op.get_bind()
    connection.execute(sa.text("DELETE FROM employees"))