"""add site model

Revision ID: 36298ab7523b
Revises: 
Create Date: 2023-03-23 16:02:06.622538

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36298ab7523b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('multiplier', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.Column('delete_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_site_delete_time'), 'site', ['delete_time'], unique=False)
    op.create_index(op.f('ix_site_id'), 'site', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_site_id'), table_name='site')
    op.drop_index(op.f('ix_site_delete_time'), table_name='site')
    op.drop_table('site')
    # ### end Alembic commands ###
