"""first revision

Revision ID: a26e88900a38
Revises: 
Create Date: 2023-07-29 16:21:46.064359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a26e88900a38'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_profile_image_id', table_name='profile_image')
    op.drop_table('profile_image')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    op.drop_index('ix_otp_email', table_name='otp')
    op.drop_index('ix_otp_id', table_name='otp')
    op.drop_table('otp')
    op.drop_index('ix_bussines_account_id', table_name='bussines_account')
    op.drop_table('bussines_account')
    op.drop_index('ix_address_id', table_name='address')
    op.drop_table('address')
    op.drop_index('ix_product_image_id', table_name='product_image')
    op.drop_table('product_image')
    op.drop_index('ix_products_id', table_name='products')
    op.drop_table('products')
    op.drop_table('invoices')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('invoices',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('userid', sa.INTEGER(), nullable=True),
    sa.Column('invno', sa.INTEGER(), nullable=True),
    sa.Column('amount', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('product_name', sa.VARCHAR(), nullable=True),
    sa.Column('company_name', sa.VARCHAR(), nullable=True),
    sa.Column('batch_No', sa.VARCHAR(), nullable=True),
    sa.Column('selling_price', sa.FLOAT(), nullable=True),
    sa.Column('list_price', sa.FLOAT(), nullable=True),
    sa.Column('discount_price', sa.VARCHAR(), nullable=True),
    sa.Column('product_size', sa.VARCHAR(), nullable=True),
    sa.Column('product_color', sa.VARCHAR(), nullable=True),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_products_id', 'products', ['id'], unique=False)
    op.create_table('product_image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('product_image_path', sa.VARCHAR(), nullable=True),
    sa.Column('product_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product_image.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_product_image_id', 'product_image', ['id'], unique=False)
    op.create_table('address',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('mobile_number', sa.VARCHAR(), nullable=False),
    sa.Column('address_line_1', sa.VARCHAR(), nullable=False),
    sa.Column('address_line_2', sa.VARCHAR(), nullable=False),
    sa.Column('country_name', sa.VARCHAR(), nullable=False),
    sa.Column('state', sa.VARCHAR(), nullable=False),
    sa.Column('district', sa.VARCHAR(), nullable=False),
    sa.Column('zipcode', sa.VARCHAR(), nullable=False),
    sa.Column('is_home', sa.BOOLEAN(), nullable=False),
    sa.Column('is_office', sa.BOOLEAN(), nullable=False),
    sa.Column('is_order', sa.BOOLEAN(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_address_id', 'address', ['id'], unique=False)
    op.create_table('bussines_account',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('shop_name', sa.VARCHAR(), nullable=False),
    sa.Column('registration_no', sa.VARCHAR(), nullable=False),
    sa.Column('gst_no', sa.VARCHAR(), nullable=True),
    sa.Column('address_line_1', sa.VARCHAR(), nullable=False),
    sa.Column('address_line_2', sa.VARCHAR(), nullable=False),
    sa.Column('country_name', sa.VARCHAR(), nullable=False),
    sa.Column('state_name', sa.VARCHAR(), nullable=False),
    sa.Column('city_name', sa.VARCHAR(), nullable=False),
    sa.Column('zip_code', sa.VARCHAR(), nullable=False),
    sa.Column('userid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_bussines_account_id', 'bussines_account', ['id'], unique=False)
    op.create_table('otp',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('otp', sa.VARCHAR(), nullable=False),
    sa.Column('status', sa.VARCHAR(), nullable=False),
    sa.Column('exp_time', sa.FLOAT(), nullable=False),
    sa.Column('count_otp', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_otp_id', 'otp', ['id'], unique=False)
    op.create_index('ix_otp_email', 'otp', ['email'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(), nullable=True),
    sa.Column('email', sa.VARCHAR(), nullable=True),
    sa.Column('password', sa.VARCHAR(), nullable=True),
    sa.Column('is_admin', sa.BOOLEAN(), nullable=True),
    sa.Column('is_user', sa.BOOLEAN(), nullable=True),
    sa.Column('is_shopkeeper', sa.BOOLEAN(), nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_table('profile_image',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('image_name', sa.VARCHAR(), nullable=False),
    sa.Column('image_page', sa.VARCHAR(), nullable=False),
    sa.Column('userid', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['userid'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_profile_image_id', 'profile_image', ['id'], unique=False)
    # ### end Alembic commands ###