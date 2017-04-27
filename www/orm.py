#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio, logging
import aiomysql

def log(sql, args=()):
    logging.info('SQL: %s' % sql)

async def create_pool(loop, **kw):
    pass

async def select(sql, args, size=None):
    pass

async def execute(sql, args, autocommit=True):
    pass

def create_args_string(num):
    pass

class Field(object):
    pass

class StringField(Field):
    pass

class BooleanField(Field):
    pass

class IntegerField(Field):
    pass

class FloatField(Field):
    pass

class TextField(Field):
    pass

class ModelMetaclass(type):
    pass

class Modal(dict, metaclass=ModelMetaclass):
    pass
