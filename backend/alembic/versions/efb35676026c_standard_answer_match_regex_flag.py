"""standard answer match_regex flag

Revision ID: efb35676026c
Revises: 0ebb1d516877
Create Date: 2024-09-11 13:55:46.101149

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "efb35676026c"
down_revision = "0ebb1d516877"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "standard_answer",
        sa.Column(
            "match_regex", sa.Boolean(), nullable=False, server_default=sa.false()
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("standard_answer", "match_regex")
    # ### end Alembic commands ###
