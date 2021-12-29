"""add user table

Revision ID: 290adf41a720
Revises: 47c6a19c78e8
Create Date: 2021-12-28 18:01:18.416461

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '290adf41a720'
down_revision = '47c6a19c78e8'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
