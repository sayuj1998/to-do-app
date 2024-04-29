from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Todo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    description: Mapped[str]
    timestamp: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    due_date: Mapped[datetime] = mapped_column(default=lambda: datetime.now())
    checked = db.Column(db.Boolean, default=False)

