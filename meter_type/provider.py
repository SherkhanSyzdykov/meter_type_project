from sqlalchemy.orm import Session
from database import engine

from .models import MeterType


class MeterTypeProvider:
    def create(self, **kwargs):
        with Session(engine) as session:
            session.add(MeterType(**kwargs))

    def update(self, meter_type_id):
        with Session(engine) as session:
            pass
