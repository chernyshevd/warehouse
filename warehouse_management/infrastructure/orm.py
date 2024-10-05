from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class ProductORM(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    quantity = Column(Integer)
    price = Column(Float)
    category = Column(Integer)


order_product_assocoations = Table(
    "order_product_assocoations",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id")),
    Column("product_id", ForeignKey("products.id")),
)


class OrderORM(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    products = relationship("ProductORM", secondary=order_product_assocoations)


product_category_assocoations = Table(
    "product_category_assocoations",
    Base.metadata,
    Column("product_id", ForeignKey("products.id")),
    Column("category_id", ForeignKey("category.id")),
)


class CategoryORM(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    products = relationship("ProductORM", secondary=product_category_assocoations)


role_staff_assocoations = Table(
    "role_staff_assocoations",
    Base.metadata,
    Column("role_id", ForeignKey("role.id")),
    Column("staff_id", ForeignKey("staff.id")),
)


class RoleORM(Base):
    __tablename__ = "role"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    staffs = relationship("StaffORM", secondary=role_staff_assocoations)


class CustomerORM(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    staff_id = Column(Integer, ForeignKey("staff.id"))


staff_customer_assocoations = Table(
    "staff_customer_assocoations",
    Base.metadata,
    Column("staff_id", ForeignKey("staff.id")),
    Column("customer_id", ForeignKey("customer.id")),
)


class StaffORM(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String)
    user_name = Column(String)
    role_id = Column(Integer, ForeignKey("role.id"))
    customers = relationship("CustomerORM", secondary=staff_customer_assocoations)
