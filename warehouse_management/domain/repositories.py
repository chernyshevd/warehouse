from abc import ABC, abstractmethod
from typing import List

from .models import Category, Customer, Order, Product, Role, Staff


class ProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def get(self, product_id: int) -> Product:
        pass

    @abstractmethod
    def list(self) -> List[Product]:
        pass


class OrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order) -> None:
        pass

    @abstractmethod
    def get(self, order_id: int) -> Order:
        pass

    @abstractmethod
    def list(self) -> List[Order]:
        pass


class CategoryRepository(ABC):
    @abstractmethod
    def add(self, category: Category) -> None:
        pass

    @abstractmethod
    def get(self, category_id: int) -> Category:
        pass

    @abstractmethod
    def list(self) -> List[Category]:
        pass


class CustomerRepository(ABC):
    @abstractmethod
    def add(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get(self, customer_id: int) -> Customer:
        pass

    @abstractmethod
    def list(self) -> List[Customer]:
        pass


class RoleRepository(ABC):
    @abstractmethod
    def add(self, role: Role) -> None:
        pass

    @abstractmethod
    def get(self, role_id: int) -> Role:
        pass

    @abstractmethod
    def list(self) -> List[Role]:
        pass


class StaffRepository(ABC):
    @abstractmethod
    def add(self, staff: Staff) -> None:
        pass

    @abstractmethod
    def get(self, staff_id: int) -> Staff:
        pass

    @abstractmethod
    def list(self) -> List[Staff]:
        pass