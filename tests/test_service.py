import sys
import os
CUR_PATH = os.path.dirname(__file__)
sys.path.append(os.path.join(CUR_PATH, '..'))

from sqlalchemy.orm import Session

from warehouse_management.domain.services import WarehouseService
from warehouse_management.domain.models import (
    Category,
    Customer,
    Order,
    Product,
    Role,
    Staff,
)
from warehouse_management.infrastructure.repositories import (
    SqlAlchemyOrderRepository,
    SqlAlchemyProductRepository,
    SqlAlchemyRoleRepository,
    SqlAlchemyCustomerRepository,
    SqlAlchemyCategoryRepository,
    SqlAlchemyStaffRepository,
)
from warehouse_management.infrastructure.unit_of_work import SqlAlchemyUnitOfWork


def test_services_create_product(session: Session) -> None:
    product_repo = SqlAlchemyProductRepository(session)

    warehouse_service = WarehouseService(product_repo=product_repo)
    new_product = warehouse_service.create_product(
        name="test1",
        quantity=1,
        price=100,
        category=10,
    )
    assert isinstance(new_product, Product)


def test_services_create_order(session: Session) -> None:
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    warehouse_service = WarehouseService(
        product_repo=product_repo, order_repo=order_repo
    )
    with SqlAlchemyUnitOfWork(session) as uow:
        _ = warehouse_service.create_product(
            name="test1",
            quantity=1,
            price=100,
            category=10,
        )
        uow.commit()

    _product = product_repo.get(2)

    order = warehouse_service.create_order([_product])
    assert isinstance(order, Order)


def test_services_create_category(session: Session) -> None:
    product_repo = SqlAlchemyProductRepository(session)
    category_repo = SqlAlchemyCategoryRepository(session)
    warehouse_service = WarehouseService(
        product_repo=product_repo, category_repo=category_repo
    )

    with SqlAlchemyUnitOfWork(session) as uow:
        _ = warehouse_service.create_product(
            name="test1",
            quantity=1,
            price=100,
            category=10,
        )
        uow.commit()

    _product = product_repo.get(3)

    category = warehouse_service.create_category(
        name="clothes", description="some clothes", products=[_product]
    )
    assert isinstance(category, Category)


def test_services_create_customer(session: Session) -> None:
    customer_repo = SqlAlchemyCustomerRepository(session)
    warehouse_service = WarehouseService(customer_repo=customer_repo)

    customer = warehouse_service.create_customer(
        first_name="Dmitry",
        last_name="Chernyshev",
        address="street 1",
        phone="11111",
        email="dmitry@gmail.com",
        staff_id=1,
    )

    assert isinstance(customer, Customer)


def test_services_create_role(session: Session) -> None:
    role_repo = SqlAlchemyRoleRepository(session)
    staff_repo = SqlAlchemyStaffRepository(session)
    customer_repo = SqlAlchemyCustomerRepository(session)
    warehouse_service = WarehouseService(
        staff_repo=staff_repo, role_repo=role_repo, customer_repo=customer_repo
    )

    with SqlAlchemyUnitOfWork(session) as uow:
        _ = warehouse_service.create_customer(
            first_name="Dmitry",
            last_name="Chernyshev",
            address="street 1",
            phone="11111",
            email="dmitry@gmail.com",
            staff_id=1,
        )
        uow.commit()
        _customer = customer_repo.get(2)
        _ = warehouse_service.create_staff(
            first_name="Dmitry",
            last_name="Chernyshev",
            address="street 1",
            email="dmitry@gmail.com",
            phone="11111",
            user_name="dmitry.chernyshev",
            role_id=1,
            customers=[_customer],
        )
        uow.commit()

    _staff = staff_repo.get(1)

    role = warehouse_service.create_role(
        name="Super role", description="This role can do everything.", staffs=[_staff]
    )
    assert isinstance(role, Role)


def test_services_create_staff(session: Session) -> None:
    staff_repo = SqlAlchemyStaffRepository(session)

    customer_repo = SqlAlchemyCustomerRepository(session)
    warehouse_service = WarehouseService(
        staff_repo=staff_repo, customer_repo=customer_repo
    )

    with SqlAlchemyUnitOfWork(session) as uow:
        _ = warehouse_service.create_customer(
            first_name="Dmitry",
            last_name="Chernyshev",
            address="street 1",
            phone="11111",
            email="dmitry@gmail.com",
            staff_id=1,
        )
        uow.commit()
    _customer = customer_repo.get(3)

    staff = warehouse_service.create_staff(
        first_name="Dmitry",
        last_name="Chernyshev",
        address="street 1",
        phone="11111",
        email="dmitry@gmail.com",
        user_name="dmitry.chernyshev",
        role_id=1,
        customers=[_customer],
    )
    assert isinstance(staff, Staff)


def test_get_product(session: Session) -> None:
    product_repo = SqlAlchemyProductRepository(session)
    warehouse_service = WarehouseService(product_repo=product_repo)
    _product = warehouse_service.get_product(1)
    assert isinstance(_product, Product)


def test_get_order(session: Session) -> None:
    order_repo = SqlAlchemyOrderRepository(session)
    warehouse_service = WarehouseService(order_repo=order_repo)
    _order = warehouse_service.get_order(1)
    assert isinstance(_order, Order)


def test_get_category(session: Session) -> None:
    category_repo = SqlAlchemyCategoryRepository(session)
    warehouse_service = WarehouseService(category_repo=category_repo)
    _category = warehouse_service.get_category(1)
    assert isinstance(_category, Category)


def test_get_role(session: Session) -> None:
    role_repo = SqlAlchemyRoleRepository(session)
    warehouse_service = WarehouseService(role_repo=role_repo)
    _role = warehouse_service.get_role(1)
    assert isinstance(_role, Role)


def test_get_customer(session: Session) -> None:
    customer_repo = SqlAlchemyCustomerRepository(session)
    warehouse_service = WarehouseService(customer_repo=customer_repo)
    _customer = warehouse_service.get_customer(1)
    assert isinstance(_customer, Customer)


def test_get_staff(session: Session) -> None:
    staff_repo = SqlAlchemyStaffRepository(session)
    warehouse_service = WarehouseService(staff_repo=staff_repo)
    _staff = warehouse_service.get_staff(1)
    assert isinstance(_staff, Staff)
