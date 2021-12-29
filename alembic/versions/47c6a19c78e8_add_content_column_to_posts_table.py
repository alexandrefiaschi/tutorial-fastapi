"""add content column to posts table

Revision ID: 47c6a19c78e8
Revises: e0ed3ccdbc27
Create Date: 2021-12-28 17:50:17.691932

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c6a19c78e8'
down_revision = 'e0ed3ccdbc27'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
