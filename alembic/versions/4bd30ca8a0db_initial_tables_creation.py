"""initial tables creation

Revision ID: 4bd30ca8a0db
Revises: 
Create Date: 2021-09-25 11:32:32.529981

"""
import datetime

import sqlalchemy as sa
from alembic import op

from src.domain.entities.class_plan import PeriodEnum

# revision identifiers, used by Alembic.
revision = '4bd30ca8a0db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tb_class_plan',
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('code', sa.VARCHAR(150), unique=True, nullable=False),
        sa.Column('date', sa.DATE, nullable=False, default=datetime.date.today()),
        sa.Column('period', sa.Enum(PeriodEnum), nullable=False),
        sa.Column('teacher_code', sa.VARCHAR(150), nullable=False),
        sa.Column('teacher_name', sa.VARCHAR(150), nullable=False),
        sa.Column('group_code', sa.VARCHAR(150), nullable=False),
        sa.Column('group_name', sa.VARCHAR(150), nullable=False),
        sa.Column('subject_code', sa.VARCHAR(150), nullable=False),
        sa.Column('subject_name', sa.VARCHAR(150), nullable=False),
        sa.Column('contents', sa.TEXT, nullable=False),
        sa.Column('evaluation', sa.TEXT, nullable=True)
    )

    op.create_table(
        'tb_class_plan_material',
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('description', sa.VARCHAR(150), nullable=False),
        sa.Column('class_plan_id', sa.INTEGER, sa.ForeignKey("tb_class_plan.id"), nullable=False)
    )

    op.create_table(
        'tb_class_plan_goal',
        sa.Column('id', sa.INTEGER, primary_key=True, autoincrement=True),
        sa.Column('description', sa.VARCHAR(150), nullable=False),
        sa.Column('class_plan_id', sa.INTEGER, sa.ForeignKey("tb_class_plan.id"), nullable=False)
    )


def downgrade():
    pass
