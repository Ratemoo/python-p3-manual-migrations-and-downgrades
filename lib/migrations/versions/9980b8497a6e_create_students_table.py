"""Create students table

Revision ID: 9980b8497a6e
Revises: 791279dd0760
Create Date: 2024-09-15 14:17:51.760231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9980b8497a6e'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('student_name', sa.String(), nullable=True))
    op.drop_index('ix_students_name', table_name='students')
    op.create_index(op.f('ix_students_student_name'), 'students', ['student_name'], unique=False)
    op.drop_column('students', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('name', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_students_student_name'), table_name='students')
    op.create_index('ix_students_name', 'students', ['name'], unique=False)
    op.drop_column('students', 'student_name')
    # ### end Alembic commands ###
