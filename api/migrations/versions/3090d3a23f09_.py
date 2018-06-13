"""empty message

Revision ID: 3090d3a23f09
Revises: 
Create Date: 2018-06-02 22:02:24.342829

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3090d3a23f09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('password_salt', sa.Text(), nullable=False),
    sa.Column('password_hash', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_User_username'), 'User', ['username'], unique=True)
    op.create_table('Picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['User.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Picture')
    op.drop_index(op.f('ix_User_username'), table_name='User')
    op.drop_table('User')
    # ### end Alembic commands ###
