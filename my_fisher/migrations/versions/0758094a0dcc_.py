"""empty message

Revision ID: 0758094a0dcc
Revises: 
Create Date: 2020-02-26 13:01:43.234949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0758094a0dcc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('author', sa.String(length=30), nullable=True),
    sa.Column('binding', sa.String(length=20), nullable=True),
    sa.Column('publisher', sa.String(length=50), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('pages', sa.Integer(), nullable=True),
    sa.Column('pubdate', sa.String(length=20), nullable=True),
    sa.Column('isbn', sa.String(length=15), nullable=False),
    sa.Column('summary', sa.String(length=1000), nullable=True),
    sa.Column('images', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('isbn')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###