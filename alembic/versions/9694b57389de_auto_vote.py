"""auto-vote

Revision ID: 9694b57389de
Revises: d935e03f6f80
Create Date: 2021-12-28 21:34:14.690668

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9694b57389de'
down_revision = 'd935e03f6f80'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###     COMMAND TO GENERATE AUTO CODE: alembic revision --autogenerate -m "auto-vote" 
    op.create_table('votes',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('user_id', 'post_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    # ### end Alembic commands ###
