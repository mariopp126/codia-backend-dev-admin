from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Identity, Numeric, String, Text
from sqlalchemy.orm import relationship

from app.db.db import Base
from app.features.auth.models import Institution, User  # noqa: F401 — required for FK relationships


class Report(Base):
    """Citizen report — read-only from reporting schema."""

    __tablename__ = "reports"
    __table_args__ = {"schema": "reporting"}

    id = Column(BigInteger, Identity(always=False), primary_key=True)
    created_by = Column(BigInteger, ForeignKey("identity.users.id"), nullable=False)
    assigned_inspector_id = Column(BigInteger, ForeignKey("identity.users.id"), nullable=True)
    category = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship(User, foreign_keys=[created_by], lazy="joined")
    assigned_inspector = relationship(User, foreign_keys=[assigned_inspector_id], lazy="joined")
    location = relationship("ReportLocation", back_populates="report", uselist=False, lazy="joined")
    inspection = relationship("Inspection", back_populates="report", uselist=False)


class ReportLocation(Base):
    """Geolocation associated with a report — read-only."""

    __tablename__ = "report_locations"
    __table_args__ = {"schema": "reporting"}

    report_id = Column(BigInteger, ForeignKey("reporting.reports.id", ondelete="CASCADE"), primary_key=True)
    latitude = Column(Numeric(10, 7), nullable=False)
    longitude = Column(Numeric(10, 7), nullable=False)
    address = Column(String(500), nullable=False)

    report = relationship(Report, back_populates="location")


class Inspection(Base):
    """Inspection — read-only from inspector schema."""

    __tablename__ = "inspections"
    __table_args__ = {"schema": "inspector"}

    id = Column(BigInteger, Identity(always=False), primary_key=True)
    report_id = Column(BigInteger, ForeignKey("reporting.reports.id"), nullable=False)
    inspector_id = Column(BigInteger, ForeignKey("identity.users.id"), nullable=False)
    status = Column(String(50), nullable=False, default="PENDING")
    notes = Column(Text, nullable=True)
    assigned_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    resolved_at = Column(DateTime(timezone=True), nullable=True)

    report = relationship(Report, back_populates="inspection")
    inspector = relationship(User)


class MediaFile(Base):
    """Uploaded file — read-only from media schema."""

    __tablename__ = "files"
    __table_args__ = {"schema": "media"}

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    file_type = Column(String(10), nullable=False)
    original_name = Column(String(255), nullable=False)
    stored_name = Column(String(255), nullable=False)
    mime_type = Column(String(100), nullable=False)
    size_bytes = Column(BigInteger, nullable=False)
    storage_provider = Column(String(50), nullable=False)
    storage_path = Column(String(500), nullable=False)
    report_id = Column(BigInteger, ForeignKey("reporting.reports.id"), nullable=False)
    uploaded_by = Column(BigInteger, ForeignKey("identity.users.id"), nullable=False)
    uploaded_at = Column(DateTime(timezone=True), nullable=False)
