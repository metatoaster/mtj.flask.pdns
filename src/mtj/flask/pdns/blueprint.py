import os
import socket
import logging

from sqlalchemy import create_engine
from sqlalchemy.sql import table, column, select, update
from sqlalchemy.exc import OperationalError
from flask import Blueprint, Response, request, abort


logger = logging.getLogger(__name__)
mtj_pdns = Blueprint('mtj_pdns', __name__)

records = table(
    'records',
    column('domain_id'), column('name'), column('type'), column('content')
)
db_src = os.environ.get('MTJ_PDNS_DB', 'sqlite://')
engine = create_engine(db_src)


def update_record(domain_id, record_type, name, content):
    try:
        engine.execute(update(records).where(
            (records.c.domain_id == domain_id) &
            (records.c.type == record_type) &
            (records.c.name == name)
        ).values(content=content))
    except OperationalError:
        logger.exception('DB Failure')
        return Response('DB Failure', status=400)

    result = engine.execute(select([records.c.content]).where(
        (records.c.domain_id == domain_id) &
        (records.c.type == record_type) &
        (records.c.name == name)
    ))
    return Response(result.first()[0], status=200)


@mtj_pdns.route('/<int:domain_id>/A/<name>', methods=['POST'])
def update_a(domain_id, name):
    content = request.form.get(
        'ip', request.headers.get(
            'X-Forwarded-For', request.remote_addr))
    try:
        socket.inet_pton(socket.AF_INET, content)
    except socket.error:
        return Response('Invalid A Record: %s' % content, status=400)
    return update_record(domain_id, 'A', name, content)


@mtj_pdns.route('/<int:domain_id>/AAAA/<name>', methods=['POST'])
def update_aaaa(domain_id, name):
    content = request.form.get(
        'ip', request.headers.get(
            'X-Forwarded-For', request.remote_addr))
    try:
        socket.inet_pton(socket.AF_INET6, content)
    except socket.error:
        return Response('Invalid AAAA Record: %s' % content, status=400)
    return update_record(domain_id, 'AAAA', name, content)


@mtj_pdns.before_request
def auth():
    token = os.environ.get('MTJ_PDNS_TOKEN', None)
    if not token:
        # no authentication used
        return
    if request.headers.get('Authorization') == 'Bearer %s' % token:
        return
    abort(403)
