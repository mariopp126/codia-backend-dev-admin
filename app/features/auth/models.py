from datetime import datetime

from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Identity, Integer, String
from sqlalchemy.orm import relationship

from app.db.db import Base


class Institution(Base):
    """Institution — Management API owns this table."""

    __tablename__ = "institutions"
    __table_args__ = {"schema": "management"}

    id = Column(BigInteger, Identity(always=False), primary_key=True)
    name = Column(String(255), nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class User(Base):
    """User account — read-only copy of identity.users."""

    __tablename__ = "users"
    __table_args__ = {"schema": "identity"}

    id = Column(BigInteger, Identity(always=False), primary_key=True)
    citizen_id = Column(String(13), unique=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)
    is_email_verified = Column(Boolean, default=False, nullable=False)

    failed_login_attempts = Column(Integer, default=0, nullable=False)
    profile_image_path = Column(String(500), nullable=True)
    last_login_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    user_type = Column(String(50), nullable=False)
    institution_id = Column(BigInteger, ForeignKey("management.institutions.id"), nullable=True)

    institution = relationship("Institution", lazy="joined")

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email={self.email}, user_type={self.user_type})>"
