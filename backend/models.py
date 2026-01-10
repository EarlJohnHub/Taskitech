from sqlalchemy import String, DateTime, ForeignKey, func
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from .repository import Base


class User(Base):
    __tablename__ = "user_accounts"
    user_id : Mapped[int] = mapped_column(primary_key=True) 
    fullname: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(128))
    

class Task(Base):
    __tablename__ = "user_tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str | None] = mapped_column(String(500))
    status: Mapped[bool] = mapped_column(default=False)
    priority: Mapped[int] = mapped_column(default=1)

    due_date: Mapped[datetime | None] = mapped_column(DateTime)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    owner_id: Mapped[int] = mapped_column(ForeignKey("user_accounts.user_id"))
