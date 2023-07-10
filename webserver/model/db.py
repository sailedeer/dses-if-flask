"""Utilities related to the global database instance."""

from typing import TypeAlias

from flask_sqlalchemy import SQLAlchemy

_db: SQLAlchemy = SQLAlchemy()

Model = TypeAlias[_db.Model]


def get_db() -> SQLAlchemy:
    """Returns a reference to the global database."""
    return _db


def create_db_columns() -> None:
    """Creates database columns which don't exist."""
    _db.create_all()
