from typing import List

from sqlalchemy.orm import Session

from warehouse_management.domain.models import (
    Category,
    Customer,
    Order,
    Product,
    Role,
    Staff,
)
from warehouse_management.domain.repositories import (
    CategoryRepository,
    CustomerRepository,
    OrderRepository,
    ProductRepository,
    RoleRepository,
    StaffRepository,
)

from .orm import CategoryORM, CustomerORM, OrderORM, ProductORM, RoleORM, StaffORM


class SqlAlchemyProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: Product) -> None:
        product_orm = ProductORM(
            name=product.name,
            quantity=product.quantity,
            price=product.price,
            category=product.category,
        )
        self.session.add(product_orm)

    def get(self, product_id: int) -> Product:
        product_orm = self.session.query(ProductORM).filter_by(id=product_id).one()
        return Product(
            id=int(product_orm.id),
            name=str(product_orm.name),
            quantity=int(product_orm.quantity),
            price=float(product_orm.price),
            category=int(product_orm.category),
        )

    def list(self) -> List[Product]:
        products_orm = self.session.query(ProductORM).all()
        return [
            Product(
                id=int(p.id),
                name=str(p.name),
                quantity=int(p.quantity),
                price=float(p.price),
                category=int(p.category),
            )
            for p in products_orm
        ]


class SqlAlchemyOrderRepository(OrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, order: Order) -> None:
        order_orm = OrderORM()
        order_orm.products = [
            self.session.query(ProductORM).filter_by(id=p.id).one()
            for p in order.products
        ]
        self.session.add(order_orm)

    def get(self, order_id: int) -> Order:
        order_orm = self.session.query(OrderORM).filter_by(id=order_id).one()
        products = [
            Product(
                id=p.id,
                name=p.name,
                quantity=p.quantity,
                price=p.price,
                category=p.category,
            )
            for p in order_orm.products
        ]
        return Order(id=int(order_orm.id), products=products)

    def list(self) -> List[Order]:
        orders_orm = self.session.query(OrderORM).all()
        orders = []
        for order_orm in orders_orm:
            products = [
                Product(
                    id=p.id,
                    name=p.name,
                    quantity=p.quantity,
                    price=p.price,
                    category=p.category,
                )
                for p in order_orm.products
            ]
            orders.append(Order(id=int(order_orm.id), products=products))
        return orders


class SqlAlchemyCategoryRepository(CategoryRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, category: Category) -> None:
        category_orm = CategoryORM(name=category.name, description=category.description)
        category_orm.products = [
            self.session.query(ProductORM).filter_by(id=p.id).one()
            for p in category.products
        ]
        self.session.add(category_orm)

    def get(self, category_id: int) -> Category:
        category_orm = self.session.query(CategoryORM).filter_by(id=category_id).one()
        products = [
            Product(
                id=p.id,
                name=p.name,
                quantity=p.quantity,
                price=p.price,
                category=p.category,
            )
            for p in category_orm.products
        ]
        return Category(
            id=int(category_orm.id),
            products=products,
            name=category_orm.name,
            description=category_orm.description,
        )

    def list(self) -> List[Category]:
        categories_orm = self.session.query(CategoryORM).all()
        categories = []
        for category_orm in categories_orm:
            products = [
                Product(
                    id=p.id,
                    name=p.name,
                    quantity=p.quantity,
                    price=p.price,
                    category=p.category,
                )
                for p in category_orm.products
            ]
            categories.append(Order(id=int(category_orm.id), products=products))
        return categories


class SqlAlchemyCustomerRepository(CustomerRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, customer: Customer) -> None:
        customer_orm = CustomerORM(
            first_name=customer.first_name,
            last_name=customer.last_name,
            address=customer.address,
            phone=customer.phone,
            email=customer.email,
            staff_id=customer.staff_id,
        )
        self.session.add(customer_orm)

    def get(self, customer_id: int) -> Customer:
        customer_orm = self.session.query(CustomerORM).filter_by(id=customer_id).one()
        return Customer(
            id=int(customer_orm.id),
            first_name=str(customer_orm.first_name),
            last_name=str(customer_orm.last_name),
            address=str(customer_orm.address),
            phone=str(customer_orm.phone),
            email=str(customer_orm.email),
            staff_id=int(customer_orm.staff_id),
        )

    def list(self) -> List[Customer]:
        customer_orm = self.session.query(CustomerORM).all()
        return [
            Customer(
                id=int(p.id),
                first_name=str(p.first_name),
                last_name=str(p.last_name),
                address=str(p.address),
                phone=str(p.phone),
                email=str(p.email),
                staff_id=int(p.staff_id),
            )
            for p in customer_orm
        ]


class SqlAlchemyRoleRepository(RoleRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, role: Role) -> None:
        role_orm = RoleORM(name=role.name, description=role.description)
        role_orm.staffs = [
            self.session.query(StaffORM).filter_by(id=p.id).one() for p in role.staffs
        ]
        self.session.add(role_orm)

    def get(self, role_id: int) -> Role:
        role_orm = self.session.query(RoleORM).filter_by(id=role_id).one()
        staffs = [
            Staff(
                id=p.id,
                first_name=p.first_name,
                last_name=p.last_name,
                address=p.address,
                phone=p.phone,
                email=p.email,
                user_name=p.user_name,
                role_id=p.role_id,
                customers=[
                    Customer(
                        id=int(c.id),
                        first_name=str(c.first_name),
                        last_name=str(c.last_name),
                        address=str(c.address),
                        phone=str(c.phone),
                        email=str(c.email),
                        staff_id=int(c.id),
                    )
                    for c in p.customers
                ],
            )
            for p in role_orm.staffs
        ]
        return Role(
            id=int(role_orm.id),
            name=str(role_orm.name),
            description=str(role_orm.description),
            staffs=staffs,
        )

    def list(self) -> List[Role]:
        roles_orm = self.session.query(RoleORM).all()
        roles = []
        for role_orm in roles_orm:
            staffs = [
                Staff(
                    id=p.id,
                    first_name=p.first_name,
                    last_name=p.last_name,
                    address=p.address,
                    phone=p.phone,
                    email=p.email,
                    user_name=p.user_name,
                    role_id=p.role_id,
                    customers=[
                        Customer(
                            id=int(c.id),
                            first_name=str(c.first_name),
                            last_name=str(c.last_name),
                            address=str(c.address),
                            phone=str(c.phone),
                            email=str(c.email),
                            staff_id=int(c.id),
                        )
                        for c in p.customers
                    ],
                )
                for p in role_orm.staffs
            ]
            roles.append(
                Role(
                    id=int(role_orm.id),
                    name=str(role_orm.name),
                    description=str(role_orm.description),
                    staffs=staffs,
                )
            )
        return roles


class SqlAlchemyStaffRepository(StaffRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, staff: Staff) -> None:
        staff_orm = StaffORM(
            first_name=staff.first_name,
            last_name=staff.last_name,
            address=staff.address,
            phone=staff.phone,
            email=staff.email,
            user_name=staff.user_name,
            role_id=staff.role_id,
        )
        staff_orm.customers = [
            self.session.query(CustomerORM).filter_by(id=p.id).one()
            for p in staff.customers
        ]
        self.session.add(staff_orm)

    def get(self, staff_id: int) -> Staff:
        staff_orm = self.session.query(StaffORM).filter_by(id=staff_id).one()
        customers = [
            Customer(
                id=int(p.id),
                first_name=str(p.first_name),
                last_name=str(p.last_name),
                address=str(p.address),
                phone=str(p.phone),
                email=str(p.email),
                staff_id=int(p.id),
            )
            for p in staff_orm.customers
        ]
        return Staff(
            id=int(staff_orm.id),
            first_name=str(staff_orm.first_name),
            last_name=str(staff_orm.last_name),
            address=str(staff_orm.address),
            phone=str(staff_orm.phone),
            email=str(staff_orm.email),
            user_name=str(staff_orm.user_name),
            role_id=int(staff_orm.role_id),
            customers=customers,
        )

    def list(self) -> List[Staff]:
        staffs_orm = self.session.query(StaffORM).all()
        staffs = []
        for staff_orm in staffs_orm:
            customers = [
                Customer(
                    id=int(p.id),
                    first_name=str(p.first_name),
                    last_name=str(p.last_name),
                    address=str(p.address),
                    phone=str(p.phone),
                    email=str(p.email),
                    staff_id=int(p.id),
                )
                for p in staff_orm.customers
            ]
            staffs.append(
                Staff(
                    id=int(staff_orm.id),
                    first_name=str(staff_orm.first_name),
                    last_name=str(staff_orm.last_name),
                    address=str(staff_orm.address),
                    phone=str(staff_orm.phone),
                    email=str(staff_orm.email),
                    user_name=str(staff_orm.user_name),
                    role_id=int(staff_orm.role_id),
                    customers=customers,
                )
            )
        return staffs
