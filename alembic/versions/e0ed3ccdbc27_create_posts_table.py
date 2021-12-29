"""create posts table

Revision ID: e0ed3ccdbc27
Revises: 
Create Date: 2021-12-28 17:32:23.040301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0ed3ccdbc27'
down_revision = None
branch_labels = None
depends_on = None

# logic for command to make changes that you want to do
def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(), nullable=False))

    pass

# logic to handle roll back
def downgrade():
    op.drop_table('posts')
    pass
