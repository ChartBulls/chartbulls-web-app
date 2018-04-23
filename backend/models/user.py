#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    backend.models.user
    ~~~~~~~~~~~~~~~~~~~

    This module implements the user model.
"""

from datetime import datetime

from backend import db


class User(db.Model):
    __tablename__  = 'users'    
    id             = db.Column(db.Integer, primary_key=True)
    email          = db.Column(db.String(50), nullable=False, unique=True)
    username       = db.Column(db.String(50), nullable=False, unique=True)
    password       = db.Column(db.String, nullable=False)
    date_signed_up = db.Column(db.TIMESTAMP, nullable=False)

    def __init__(self, email, username, password):
        """This function initializes a user."""
        self.email        = email
        self.username     = username
        # Protecting password using a one-way hash function
        self.password     = bcrypt.generate_password_hash(password)
        self.date_created = datetime.now()

    def check_password(self, password):
        """This function checks if passwords match."""
        return bcrypt.check_password_hash(self.password, password)