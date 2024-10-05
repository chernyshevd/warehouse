from warehouse_management.domain.services import WarehouseService
from warehouse_management.infrastructure.orm import Base
from warehouse_management.infrastructure.repositories import SqlAlchemyOrderRepository, SqlAlchemyProductRepository
from warehouse_management.infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = r"sqlite:///warehouse.db"

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


def main() -> None:
    session = SessionFactory()
    product_repo = SqlAlchemyProductRepository(session)
    order_repo = SqlAlchemyOrderRepository(session)

    warehouse_service = WarehouseService(product_repo, order_repo)
    with SqlAlchemyUnitOfWork(session) as uow:
        new_product = warehouse_service.create_product(name="test1", quantity=1, price=100, category=10)
        uow.commit()
        _product = product_repo.get(4)
        print(_product)
        print(f"create product: {new_product}")
        # TODO add some actions


if __name__ == "__main__":
    main()

