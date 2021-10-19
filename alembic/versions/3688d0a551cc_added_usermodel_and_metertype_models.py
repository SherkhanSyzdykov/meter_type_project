"""Added UserModel and MeterType models

Revision ID: 3688d0a551cc
Revises: 
Create Date: 2021-10-19 14:16:32.244490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3688d0a551cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meter_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=300), nullable=False),
    sa.Column('coefficient', sa.Float(), nullable=True),
    sa.Column('unit_of_measure', sa.String(), nullable=True),
    sa.Column('init_indicator_multiplier', sa.Float(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_meter_type_association',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('meter_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['meter_type_id'], ['meter_type.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_model.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'meter_type_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_meter_type_association')
    op.drop_table('user_model')
    op.drop_table('meter_type')
    # ### end Alembic commands ###