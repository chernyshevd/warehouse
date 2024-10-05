from warehouse_management.domain.unit_of_work import UnitOfWork
from sqlalchemy.orm import Session


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session: Session):
        self.session = session

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        return self

    def __exit__(self, *args: object) -> None:
        self.close()

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def close(self) -> None:
        self.session.close()
