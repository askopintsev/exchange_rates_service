"""migration

Revision ID: a6c6750d66c9
Revises: 
Create Date: 2022-05-22 12:52:11.953246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6c6750d66c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('currency',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('valute_id', sa.String(), nullable=True),
    sa.Column('num_code', sa.Integer(), nullable=True),
    sa.Column('char_code', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_currency_id'), 'currency', ['id'], unique=False)
    op.create_table('records',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('nominal', sa.Integer(), nullable=True),
    sa.Column('value', sa.Float(), nullable=True),
    sa.Column('currency_id', sa.String(), nullable=True),
    sa.Column('timestamp', sa.TIMESTAMP(), nullable=True),
    sa.ForeignKeyConstraint(['currency_id'], ['currency.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_records_id'), 'records', ['id'], unique=False)
    op.create_index(op.f('ix_records_value'), 'records', ['value'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_records_value'), table_name='records')
    op.drop_index(op.f('ix_records_id'), table_name='records')
    op.drop_table('records')
    op.drop_index(op.f('ix_currency_id'), table_name='currency')
    op.drop_table('currency')
    # ### end Alembic commands ###