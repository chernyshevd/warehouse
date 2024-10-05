from typing import List, Union

from .models import Category, Customer, Order, Product, Role, Staff
from .repositories import (
    CategoryRepository,
    CustomerRepository,
    OrderRepository,
    ProductRepository,
    RoleRepository,
    StaffRepository,
)


class WarehouseService:
    def __init__(
        self,
        product_repo: Union[ProductRepository, None] = None,
        order_repo: Union[OrderRepository, None] = None,
        category_repo: Union[CategoryRepository, None] = None,
        role_repo: Union[RoleRepository, None] = None,
        staff_repo: Union[StaffRepository, None] = None,
        customer_repo: Union[CustomerRepository, None] = None,
    ):
        self.product_repo = product_repo
        self.order_repo = order_repo
        self.category_repo = category_repo
        self.role_repo = role_repo
        self.staff_repo = staff_repo
        self.customer_repo = customer_repo

    def create_product(
        self, name: str, quantity: int, price: float, category: int
    ) -> Product:
        product = Product(name=name, quantity=quantity, price=price, category=category)
        if self.product_repo:
            self.product_repo.add(product)
        return product

    def create_order(self, products: List[Product]) -> Order:
        order = Order(products=products)
        if self.order_repo:
            self.order_repo.add(order)
        return order

    def create_category(
        self, name: str, description: str, products: List[Product]
    ) -> Category:
        category = Category(name=name, description=description, products=products)
        if self.category_repo:
            self.category_repo.add(category)
        return category

    def create_role(self, name: str, description: str, staffs: List[Staff]) -> Role:
        role = Role(name=name, description=description, staffs=staffs)
        if self.role_repo:
            self.role_repo.add(role)
        return role

    def create_staff(
        self,
        first_name: str,
        last_name: str,
        address: str,
        phone: str,
        email: str,
        user_name: str,
        role_id: int,
        customers: List[Customer],
    ) -> Staff:
        staff = Staff(
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            email=email,
            user_name=user_name,
            role_id=role_id,
            customers=customers,
        )
        if self.staff_repo:
            self.staff_repo.add(staff)
        return staff

    def create_customer(
        self,
        first_name: str,
        last_name: str,
        address: str,
        phone: str,
        email: str,
        staff_id: int,
    ) -> Customer:
        customer = Customer(
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,
            email=email,
            staff_id=staff_id,
        )
        if self.customer_repo:
            self.customer_repo.add(customer)
        return customer

    def get_product(self, product_id: int) -> Product:
        return self.product_repo.get(product_id)  # type: ignore

    def get_order(self, order_id: int) -> Order:
        return self.order_repo.get(order_id)  # type: ignore

    def get_category(self, category_id: int) -> Category:
        return self.category_repo.get(category_id)  # type: ignore

    def get_role(self, role_id: int) -> Role:
        return self.role_repo.get(role_id)  # type: ignore

    def get_customer(self, customer_id: int) -> Customer:
        return self.customer_repo.get(customer_id)  # type: ignore

    def get_staff(self, staff_id: int) -> Staff:
        return self.staff_repo.get(staff_id)  # type: ignore