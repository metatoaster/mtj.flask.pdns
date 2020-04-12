mtj.flask.pdns
==============

A very simple Flask front-end for PDNS.  Requires a database backend.

Only a single update endpoint is provided to update a specific existing
record in the records table.

Test by running:

.. code:: console

    $ MTJ_PDNS_DB=postgresql+psycopg2://user:pass@localhost/db python -m mtj.flask.pdns
