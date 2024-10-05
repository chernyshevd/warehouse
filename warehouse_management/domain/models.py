from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    quantity: int
    price: float
    category: int
    id: int = 0


@dataclass
class Category:
    name: str
    description: str
    products: List[Product] = field(default_factory=list)
    id: int = 0

    def add_product(self, product: Product) -> None:
        self.products.append(product)


@dataclass
class Order:
    id: int = 0
    products: List[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> None:
        self.products.append(product)


@dataclass
class Customer:
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str
    staff_id: int
    id: int = 0


@dataclass
class Staff:
    first_name: str
    last_name: str
    address: str
    phone: str
    email: str
    user_name: str
    role_id: int
    id: int = 0
    customers: List[Customer] = field(default_factory=list)


@dataclass
class Role:
    name: str
    description: str
    id: int = 0
    staffs: List[Staff] = field(default_factory=list)
